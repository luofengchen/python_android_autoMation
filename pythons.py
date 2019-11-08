#!/usr/bin/python
# coding=utf-8
import os
import time
import random


def click(x, y):
    cmd = "adb shell input tap {x1} {y1}".format(x1=x, y1=y)
    os.system(cmd)


def backapi():
    # 61 160
    click(61, 160)


def canscroll():
    x2 = 200+random.randint(0, 4)
    y2 = 400+random.randint(0, 4)
    x1 = 340+random.randint(4, 9)
    y1 = 830+random.randint(4, 9)
    t = 200+random.randint(0, 9)
    print("输出测试输出的内容:", x1, x2, y1, y2,t)
    cmds = "adb shell input swipe {x1} {y1} {x2} {y2} {t}".format(
        x1=x1, y1=y1, x2=x2, y2=y2, t=t)
    os.system(cmds)
    # for vals in cmds:
    #     print("输出??", str(vals))
    #     os.system(vals)


def click_ok(idx):
    count = 0
    # click(880, 1353)
    click(900, 1716)#//0/20的点击点 此处设置点击位置
    # 900 1716
    time.sleep(1)
    print("输出内容"+str(idx))
    idxs = 20 + random.randint(0,7)
    for idx in range(idxs):
        print("输出测试内容11==>>:", idx)
        canscroll()
        time.sleep(1)
        count = count+1
        if count >= idxs:
            backapi()
            time.sleep(3)

    # time.sleep(30)
    #
    # time.sleep(3)


def main():
    # click_ok()
    for idx in range(20):
        # print("测试???:", str(idx))
        click_ok(int(idx))


if __name__ == "__main__":
    print("测试???11")
    main()
    # canscroll()
