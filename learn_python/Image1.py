#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Image

#打开一个jpg图像文件
im = Image.open('G:\python27\learn_python\Penguins.jpg')
#获得图像尺寸：
w, h = im.size
#缩放到50%：
im.thumbnail((w//2, h//2))
#把缩放后的图像用jpeg合适保存：
im.save('G:\python27\learn_python\\thumbnail2.jpg','jpeg')