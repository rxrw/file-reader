# !/usr/bin/python
# -- coding:utf8 --
from abc import ABCMeta, abstractmethod, abstractstaticmethod
import re
from utils.configs import get_config

from redis import Redis

from utils import mapper
from utils import strings


class AbstractReader(metaclass=ABCMeta):

    redis_ins = Redis(host=get_config('REDIS_HOST', 'redis'), port=get_config(
        'REDIS_PORT', '6379'), password=get_config('REDIS_PASS', 'password'))

    fp = None  # 句柄

    redis = None

    filename = None

    # 看能不能用 可以的话返回带句柄的实例
    @abstractstaticmethod
    def can_i_use(filename):
        pass

    @abstractmethod
    def get_line(self, line, splitor):
        pass

    @abstractmethod
    def read_content(self, possible_header=None, pattern=None):
        pass

    def yield_reader(self, header=None, pattern=None):
        item = self.read_content(header, pattern)
        return item

    def d2dict(self, struct_line: list, header: list, position):
        if(len(struct_line) != len(header)):
            print("ERROR {} 第{}位置长度不一致 {}".format(
                self.filename, position, struct_line))
        item = dict()
        for k in range(len(header)):
            if k >= len(struct_line):
                break
            item[header[k]] = struct_line[k]
        return item

    def get_header(self, struct_first_line, possible_header=None):
        header = None
        reset = False  # reset = true 表示跳过第一行
        # 参数是第一选项
        if possible_header is not None:
            print("{filename}存在header参数，尝试使用{header}".format(
                filename=self.filename, header=possible_header))
            header = self.judge_header(
                struct_first_line, possible_header.split(","))
        # 没有db配置 也没有手动输入 尝试自己解析
        if header is None:
            print("{filename}没有配置，使用文件第一行自动解析header,列内容：{line}".format(
                filename=self.filename, line=struct_first_line))
            header = self.__parse_header_by_first_line(struct_first_line)
            reset = True
        if header is None:
            # 没找到
            print("{filename}没有找到文件头，使用col1形式".format(filename=self.filename))
            self.col_header(struct_first_line)
        print("{filename}的header设定为{header}".format(
            filename=self.filename, header=header))
        return header, reset

    def __parse_header_by_first_line(self, struct_first_line):
        header = []
        # 不需要配置使用文件header的事情了
        for k in range(len(struct_first_line)):
            k_name = struct_first_line[k]
            if re.compile(r"^\d*$").match(str(k_name)):
                print("{filename} 在用第一行解析时发现了纯数字，不会是header".format(
                    filename=self.filename))
                return None
            header.append(mapper.get_keyname(
                strings.hump2underline(k_name)))
        print("{filename}转换驼峰和语言，转换结果{header}".format(
            filename=self.filename, header=header))
        return self.judge_header(struct_first_line, header)

    def judge_header(self, struct_first_line: list, header: list):
        print("判断{filename}首行{struct_first_line}与header{header}".format(
            filename=self.filename, struct_first_line=struct_first_line, header=header))
        if header is None or len(header) != len(struct_first_line):
            return None
        return header

    def col_header(self, struct_first_line):
        header = []
        for k in range(len(struct_first_line)):
            header.append("col{}".format(k+1))
        return header
