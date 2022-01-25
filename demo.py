import random
import time
import cv2
import numpy as np
import math
import uiautomator2 as u2
from mss import mss # Python-mss模块是最快的模块 https://blog.csdn.net/weixin_34530727/article/details/112248546
from mss.darwin import MSS
from PIL import Image
import os,inspect
import adbutils
import websocket

'''
UI Automation Framework for Games and Apps
https://github.com/AirtestProject/Airtest
'''


debug=False
sign=False
start_x=0
start_y=0
end_x=0
end_y=0
distance=0
device = (500,1020)
input_filename = 'monitor-1.png'

d = u2.connect("b8477fa8")
font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式
kernel = np.ones((5, 5), np.uint8)  # 卷积核

postIndex = 1
mode = 'phone' # pc Or phone

def get_screenshot():
    start_time = time.time()
    if mode == 'pc':
        monitor = {"top": 160, "left": 20, "width": 360, "height": 700}
        with MSS() as sct:
            screenshot = np.array(sct.grab(monitor))
            # screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
            cv2.imwrite(input_filename, screenshot)
    if mode == 'phone':
        # d.screenshot(input_filename)
        cv2.imwrite(input_filename, d.screenshot(format='opencv'))
    end_time = time.time()
    print("消耗时间 {}".format(end_time-start_time))

def jump(distance):
    # 设置按压时间,系数为1.35
    press_time = int(distance * 2.59) # 2.59

    # 生成随机手机屏幕模拟触摸点,防止成绩无效
    # 生成随机整数(0-9),最终数值为(0-90)
    rand = random.randint(0, 9) * 10

    # adb长按操作,即在手机屏幕上((320-410),(410-500))坐标处长按press_time毫秒
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) % (320 + rand, 410 + rand, 320 + rand, 410 + rand)

    # 输出adb命令
    print(cmd)

    # 执行adb命令
    os.system(cmd)

def get_point(event, x, y, flags, param):
    # 鼠标单击事件
    global sign
    global start_x
    global start_y
    global end_x
    global end_y
    global distance
    if event == cv2.EVENT_LBUTTONDOWN:
        # 输出坐标
        print('坐标值: ', x, y)
        # 在传入参数图像上画出该点
        #cv2.circle(param, (x, y), 1, (255, 255, 255), thickness=-1)
        img = param.copy()
        # 输出坐标点的像素值
        print('像素值：',param[y][x]) # 注意此处反转，(纵，横，通道)
        # 显示坐标与像素
        text = "("+str(x)+','+str(y)+')'+str(param[y][x])
        # 说明是第一次
        if(sign ==False):
            start_x=x
            start_y=y
            sign = True
        else:
            end_x=x
            end_y=y
            distance=((start_x-end_x)**2 +(start_y-end_y)**2)**0.5
            print("distance0"+str(distance))
            jump(distance)
            sign = False

def start(target):
    # 作为模板图片，为脚部分。通过模板匹配，该函数返回脚坐标值 图像模板匹配(Match Template)
    template = cv2.imread("images/h.png")
    theight, twidth = template.shape[:2]
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return (min_loc[0] + twidth // 2, min_loc[1] + theight // 2)

#该函数功能是找到降落点中心位置并与脚坐标值计算求出两点间距离
def get_site(img):
    point_x =[]
    point_y= []
    point = []
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([14, 40, 114])
    upper = np.array([58, 106, 255])
    imgray = cv2.inRange(hsv, lower, upper)
    cv2.imshow("1", imgray)
    ret, thresh = cv2.threshold(imgray, 100, 255, cv2.THRESH_BINARY)  # 127,255
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)  # contours为轮廓集，可以计算轮廓的长度、面积等
    for cnt in contours:
        if len(cnt) > 120:
            S1 = cv2.contourArea(cnt)
            ell = cv2.fitEllipse(cnt)
            S2 = math.pi * ell[1][0] * ell[1][1]
            if (S1 / S2) > 0.2:  # 面积比例，可以更改，根据数据集。。。0.2
                img = cv2.ellipse(img, ell, (255, 0, 0), 2) # 绘制椭圆
                print("=>"+ str(S1) + "    " + str(S2) + "   " + str(ell[0][0]) + "   " + str(ell[0][1]))
                point_x.append(int(ell[0][0]))
                point_y.append(int(ell[0][1]))
                point.append((int(ell[0][0]), int(ell[0][1])))
    if len(point) == 2: # 刚刚画出两个对象(一个是自己， 一个是目标)
        start_point = start(refer)
        distance = ((start_point[0]- point[1][0]) ** 2 + (start_point[1]- point[1][1]) ** 2) ** 0.5 #0.5
        cv2.line(img, (start_point[0],start_point[1]), (point[1][0],point[1][1]), (0,255,127), 2, 4) # 绿色折线
        print("开始坐标 {} 目标坐标".format(start_point), end='')
        print((point[1][0],point[1][1]))
    else: # 错误的情况
        start_point = start(refer)
        print("X: {} - Y: {}".format(point_x, point_y))
        if len(point_x) == 0:
            exit()
        if point_x:
            distance = ((start_point[0] - point_x[point_y.index(min(point_y))]) ** 2 + (start_point[1] - min(point_y)) ** 2) ** 0.5
            cv2.line(img, (start_point[0], start_point[1]), (point_x[point_y.index(min(point_y))], min(point_y)), (255, 0, 0), 2, 4)
        else:
            cv2.imwrite('output/error.png', img)

    try:
        jump(distance)
    except Exception as e:
        exit(0)
    print("距离: "+str(distance))
    if debug:
        cv2.imshow('渲染图片', img)
    else:
        cv2.imwrite('output/{}-post.png'.format(postIndex), img)


if __name__ == "__main__":
    # 定义两幅图像
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Demo1

    while True:
        get_screenshot()
        image = cv2.imread(input_filename)
        image=cv2.resize(image, device)
        refer = image.copy()
        get_site(image)
        postIndex += 1
        if debug:
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        # isPaas = input("是否继续?")
        time.sleep(0.71)

    # Demo2
    # image = cv2.imread('01.png')
    # image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # # # 定义两个窗口 并绑定事件 传入各自对应的参数
    # cv2.namedWindow('image')
    # cv2.setMouseCallback('image', get_point, image)
    # cv2.resizeWindow("image",500,1020)
    # cv2.putText(image, "FPS: "+ str(round(1.0 / (time.time() - start_time),1)), (50, 50), font, 1, (180, 100, 255), 2, cv2.LINE_AA)
    # cv2.imshow('Post', image)














