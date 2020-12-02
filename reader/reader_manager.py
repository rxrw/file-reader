# 管理器
from utils import mapper
import os
import reader


class ReaderManager(object):

    registered_map = {
        "txt": reader.RegexReader,
        "csv": reader.CsvReader,
        "sql": reader.RegexReader,
        "xls": reader.ExcelReader,
        "xlsx": reader.ExcelReader,
    }

    instance = None

    filename = None

    table_name = None

    header = None

    pattern = None

    def __init__(self, filename, table_name, header=None, pattern=None):
        self.filename = filename
        self.table_name = table_name
        self.header = header
        self.pattern = pattern

    def check(self):
        ext = os.path.splitext(self.filename)[1].lstrip('.')
        self.instance = self.registered_map[ext](self.filename)
        return self

    def get_tablename(self):
        if self.table_name is None:
            self.table_name = os.path.splitext(os.path.basename(self.filename))[0]
        return self.table_name

    def run(self):
        try:
            return self.instance.yield_reader(header=self.header, pattern=self.pattern)
        except BaseException as e:
            print(e)
            pass
