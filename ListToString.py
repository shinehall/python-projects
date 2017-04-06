# coding=utf-8

#将列表的数据用逗号分割转成字符串
def list2String(span):
    if(span is None):
        return "error! span is null"
    rs = ""
    for i in range(len(span)):
        if(i == len(span) - 2):
            rs += span[i] + " and "
        else:
            rs += span[i] + ","
    rs = rs[0:len(rs) - 1]
    print(rs)

span = ["aaa", "bbb", "ccc", "ddd"]

list2String(span)