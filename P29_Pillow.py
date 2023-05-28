from PIL import Image, ImageDraw

img = Image.open('CENG.jpg')
img.save('CENG.png')
new = img.resize((600,400))
print(new.size)
Text = ImageDraw.Draw(img)
Text.text((130,140), "Computer engineer", fill = (0, 0, 0))
img.show()

# rotated_img = img.rotate(35)
# rotated_img.show()

# box = (150,200,600,500)
# cropped_image = img.crop(box)
# cropped_image.save('CENG_Crope.png')
# cropped_image.show()




