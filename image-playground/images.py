from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save("thumbnail_astro.jpg")

# converted_img = img.convert("L")
# box = (100, 100, 400, 400)
# region = converted_img.crop(box)
# region.save("crop.png", "png")

# converted_img = img.convert("L")
# resize = converted_img.resize((300, 300))
# resize.save("resize_300.png", "png")

# converted_img = img.convert("L")
# rotate = converted_img.rotate(90)
# rotate.save("rotate.png", "png")

# converted_img = img.convert("L")
# converted_img.save("grey.png", "png")
# converted_img.show()

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", "png")

# print(dir(img))
# print(img.format)
# print(img.size)
# print(img.mode)
