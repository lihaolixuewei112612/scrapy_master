# import pytesseract
# from PIL import Image
# import cv2
# import os
#
# import pytesseract
# from PIL import Image
# img = Image.open('captcha.jpg')
# Img = img.convert('L')
# threshold = 175
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(1)
#     else:
#         table.append(0)
# # 图片二值化
# photo = Img.point(table, '1')
# # 最后保存二值化图片
# photo.save("binaryzation.jpg")
# text = pytesseract.image_to_string(Image.open('binaryzation.jpg'),lang='eng')
# actualname = text.strip()  # 清除字符串前后空格
# print(actualname)
#
#
