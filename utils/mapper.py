# !/usr/bin/python
# 中文映射为英文
from pypinyin import lazy_pinyin
_map = {
    "姓名": "name",
    "名字": "name",
    "昵称": "nickname",
    "用户名": "username",
    "联系人": "contact_name",
    "联系方式": "tel",
    "座机电话": "phone",
    "企业名称": "company_name",
    "企业地址": "company_address",
    "省份城市": "province_and_city",
    "省份": "province",
    "省": "province",
    "市": "city",
    "城市": "city",
    "行业关键词": "company_keyword",
    "身份证号码": "card_no",
    "身份证": "card_no",
    "手机号码": "tel",
    "手机号": "tel",
    "手机": "tel",
    "电话": "phone",
    "地址": "address",
    "电子邮箱": "email",
    "邮箱": "email",
    "出生日期": "birthday",
    "性别": "gender",
    "邮编": "post_no",
    "行业": "work",
    "月薪": "salary",
    "婚姻": "married",
    "婚姻状况": "married",
    "教育": "education_level",
    "BRAND": "brand",
    "车系": "car_series",
    "车型": "car_model",
    "颜色": "color",
    "发动机号": "engine_no",
    "车架号": "car_struct_no",
}


def get_keyname(h):
    value = _map[h] if h in _map else "_".join(lazy_pinyin(h))

    return value
