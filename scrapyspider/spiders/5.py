# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# from PIL import Image
# import os
#
#
# # 二值化处理 灰度阈值设为35，高于这个值的点全部填白色
# def two_value(threshold=35):
#     for i in range(0, 3000):
#         # 打开文件夹中的图片
#         image = Image.open('code.jpg')
#         # 灰度图 模式“L” 每个像素用8个bit表示，0表示黑，255表示白
#         # 公式 L = R * 299/1000 + G * 587/1000+ B * 114/1000
#         lim = image.convert('L')
#         table = []
#         for j in range(256):
#             if j < threshold:
#                 # 填黑色
#                 table.append(0)
#             else:
#                 # 填白色
#                 table.append(1)
#                 # 对图像像素操作 模式“1” 为二值图像，非黑即白。但是它每个像素用8个bit表示，0表示黑，255表示白
#         bim = lim.point(table, '1')
#         path = 'D:/workespace/workspace/scrapy-tutorial-master/scrapy-tutorial-master/scrapyspider/spiders/demo/'
#         isExists = os.path.exists(path)
#         if not isExists:
#             os.makedirs(path)
#             # 保存图片
#         bim.save(path+str(i) + '.jpg')
# if __name__ == "__main__":
#     two_value()
