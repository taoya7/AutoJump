



### 如何启动



确保环境

- Python
- ADB

---



手机开启开发者选项, 然后电脑输入adb devices

```shell
➜  ~ adb devices
List of devices attached
b8477fa8	device
```



替换`demo.py`第30行

```shell
d = u2.connect("b8477fa8") # 复制上一步的设备ID
```



安装手机软件

```shell
pip install --pre -U uiautomator2 # 安装uiautomator2
python -m uiautomator2 init # 手机安装软件
```

![image-20220125175751543](http://alicdn.taoya.art/img/20220125175751.png)







开启游戏



执行`python demo.py`



![image-20220125175835504](http://alicdn.taoya.art/img/20220125175835.png)



---



### 截屏优化

http://doc.569781231.xyz/share/f6ac6f82-85a7-4b7c-a220-603aba50d880

- 使用uiautomator2截屏
- 工具
  - pycharm
  - adb
  - scrcpy
  - minicap
  - opencv


(*)  魔改自: https://github.com/hurance/autotytiao