# import ddddocr
# from PIL import Image
# ocr = ddddocr.DdddOcr(old=True)
#
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
# with open("binaryzation.jpg", 'rb') as f:
#     image = f.read()
#
# res = ocr.classification(image)
# print('----------------')
# print(res)