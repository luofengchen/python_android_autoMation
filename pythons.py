#!/usr/bin/python
# coding=utf-8
import os
import time


def click(x, y):
    cmd = "adb shell input tap {x1} {y1}".format(x1=x, y1=y)
    os.system(cmd)


def backapi():
    # 61 160
    click(61, 160)


def canscroll():
    count = 0
    x1 = 101
    y1 = 201
    x2 = 148
    y2 = 230
    t = 2
    cmds = "adb -s %s shell input swipe {x1} {y1} {x2} {y2} {t}".format(
        x1=x1, y1=y1, x2=x2, y2=y2, t=t)
    os.system(cmds)
    # for vals in cmds:
    #     print("输出??", str(vals))
    #     os.system(vals)


def click_ok(idx):
    click(907, 1849)
    time.sleep(1)
    print("输出内容"+str(idx))
    canscroll()
    # time.sleep(30)
    # backapi()
    # time.sleep(3)


def main():
    # click_ok()
    for idx in range(20):
        # print("测试???:", str(idx))
        click_ok(int(idx))


if __name__ == "__main__":
    print("测试???11")
    canscroll()
