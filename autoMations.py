#!/usr/bin/python
# coding=utf-8
import os
import time


def click(x, y):
    cmd = "adb shell input tap {x1} {y1}".format(x1=x, y1=y)
    os.system(cmd)


def backapi(args):
    # 61 160
    click(61, 160)


def click_ok(idx):
    click(907, 1849)
    time.sleep(1)
    print("输出内容"+str(idx))
    time.sleep(16)
    backapi()


def main():
    # click_ok()
    for idx in range(20):
        print("测试???:", str(idx))
    # click_ok(int(idx))



if __name__ == "__main__":
    main()
