# coding: utf8

import os, datetime, time
import re
from subprocess import getstatusoutput


def is_file(filepath):
    return os.path.isfile(filepath)


def cmd(cmd):
    status, output = getstatusoutput(cmd)
    return output.split("\n")


def list_to_file(list1, file):
    with open(file, 'w') as fw:
        for line in list1:
            fw.write("%s\n" % line)


def file_to_list(file):
    with open(file, 'r') as fr:
        return [line.strip() for line in fr.readlines()]


def mkdir(dir1):
    cmd = "mkdir -p %s" % dir1
    getstatusoutput(cmd)


def now_str():
    return dt_to_str(datetime.datetime.now())


def str_to_dt(str1):
    return datetime.datetime.strptime(str1, "%Y-%m-%d %H:%M:%S")


def dt_to_str(dt1):
    return datetime.datetime.strftime(dt1, "%Y-%m-%d %H:%M:%S")


def datestr_to_dt(str1):
    return datetime.datetime.strptime(str1, "%Y-%m-%d")


def dt_to_datestr(dt1):
    return datetime.datetime.strftime(dt1, "%Y-%m-%d")


def ts_to_dttime(timestamp):
    time_struct = time.localtime(timestamp)
    return dt_to_str(time_struct)


def is_today_change(file):
    if os.path.exists(file) and os.path.getctime(file)>datestr_to_dt(dt_to_datestr(datetime.datetime.now())).timestamp():
        return True
    return False
    pass



if __name__ == "__main__":
    is_today_change("/home/wangdawei/test/t1.txt")
    pass
