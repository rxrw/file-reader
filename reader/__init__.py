import os
import re

from reader.abstract_reader import AbstractReader
import xlrd
import csv

# this class will parse regex


class RegexReader(AbstractReader):

    patterns = [
        re.compile(r'(\d{5,10})\-+(\d+)'),  # qq
        re.compile(r'(\S+)\s+(\S+)'),  # 微博
        re.compile(
            r'(\S+?)\-+(\S+?)\-+(\S+?)\-+(\S+?)\-+(\S+?)\-+(\S+?)\-+(\S+?)'),  # 京东
        re.compile(
            r"N\'(\S*?)\',\sN\'(\S*?)\',\sN\'(\S*?)\',\sN\'(\S*?)\',\sN\'(\S*?)\',\sN\'(\S*?)\'"),  # 顺丰
    ]

    def can_i_use(filename: str):
        filetype = os.path.splitext(filename)[1]
        if filetype in ['.txt', 'sql']:
            return RegexReader(filename)
        return False

    def __init__(self, filename):
        self.filename = filename
        self.fp = open(filename, 'r')  # 二进制只读访问

    # 返回格式化
    def get_line(self, line, pattern):
        # 没有pattern的话就拆分空格玩
        if pattern is None:
            # 拆分空格
            return ",".join(re.split('\s+', line)).strip(",").split(",")
        else:
            return pattern.findall(line)[0]

    # 一个迭代器 返回dict
    def read_content(self, possible_header=None, pattern=None):
        if pattern is None:
            pattern = self.which_pattern()
        else:
            pattern = re.compile(pattern)
        if pattern is None:
            raise Exception("No Suitable Pattern For " + self.fp.name)

        self.fp.seek(0)
        header, reset = self.get_header(self.get_line(
            self.fp.readline(), pattern), possible_header)
        position = self.redis_ins.get("POSITION:" + self.filename)
        if position is not None:
            if not reset:
                self.fp.seek(int(position))
            else:
                self.fp.seek(0)
        line = self.fp.readline()
        while line is not None and line != "":
            struct_line = self.get_line(line, pattern)
            if struct_line:
                yield self.d2dict(struct_line, header, self.fp.tell())
            line = self.fp.readline()
            self.redis_ins.set("POSITION:" + self.filename, self.fp.tell())

    def which_pattern(self):
        self.fp.readline()
        first_line = self.fp.readline()
        for pattern in self.patterns:
            if pattern.match(first_line):
                print("通过which_pattern和{s}找到正则规则：{p}".format(
                    s=first_line, p=pattern))
                return pattern
        print("没有找到pattern{s}".format(s=first_line))
        return None


class CsvReader(AbstractReader):

    def can_i_use(filename: str):
        filetype = os.path.splitext(filename)[1]
        if filetype in ['.csv']:
            return CsvReader(filename)
        return False

    def __init__(self, filename):
        self.filename = filename
        self.fp = open(filename, 'r')

    def get_line(self, line, splitor=None):
        return line

    def read_content(self, possible_header=None, pattern=None):

        position = self.redis_ins.get("POSITION:" + self.filename)
        if position is not None:
            position = int(position)
        else:
            position = 0
        current = 0

        header = possible_header or []
        for line in csv.reader(self.fp):
            if current == 0:
                header, reset = self.get_header(
                    self.get_line(line), possible_header)
                current += 1
                continue

            current += 1
            if current <= position:
                continue
            struct_line = self.get_line(line)
            yield self.d2dict(struct_line, header, current)
            self.redis_ins.set("POSITION:" + self.filename, current)

# ExcelReader只能使用pandas或者xlrd


class ExcelReader(AbstractReader):

    def can_i_use(filename: str):
        filetype = os.path.splitext(filename)[1]
        if filetype in ['.xls', '.xlsx']:
            return CsvReader(filename)
        return False

    def __init__(self, filename):
        self.filename = filename
        self.fp = xlrd.open_workbook(
            filename).sheet_by_index(0)  # 目前就支持打开第一张表吧

    def get_line(self, line, splitor=None):
        return line

    def read_content(self, possible_header=None, pattern=None):
        header, reset = self.get_header(self.get_line(
            self.fp.row_values(0)), possible_header)
        position = self.redis_ins.get("POSITION:" + self.filename) or 0
        if position is not None:
            if not reset:
                position = position
            else:
                position = 1
        for index in range(int(position), self.fp.nrows):
            line = self.fp.row_values(index)  # 这里得到的是字典
            item = self.d2dict(line, header, index)
            yield item
            self.redis_ins.set("POSITION:" + self.filename, index)
