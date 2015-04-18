import Image, ImageFilter

im = Image.open('G:\python27\learn_python\Penguins.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('G:\python27\learn_python\\blur.jpg', 'jpeg')

