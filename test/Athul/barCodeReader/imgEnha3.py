from PIL import Image, ImageEnhance

im = Image.open("brct.jpg")

enhancer = ImageEnhance.Sharpness(im)

factor = 1
im_s_1 = enhancer.enhance(factor)
im_s_1.save('original-image-1.jpg');

factor = 0.05
im_s_1 = enhancer.enhance(factor)
im_s_1.save('blurred-image.jpg');

factor = 20
im_s_1 = enhancer.enhance(factor)
im_s_1.save('sharpened-image.jpg');