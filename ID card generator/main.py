import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
# دستورات اجرای کد دانشجویی
last_year = datetime.now().year % 100
unique_number = f"{random.randrange(99999):05d}"
control_number = str(last_year) + str(unique_number)
total = 0
for i in control_number:
    total += int(i)
control_number = total % 10
id_generator = f"{last_year}{unique_number}{control_number}"

#دستورات دریافت اطلاعات شخصی دانشجو 
first_name = input("Please enter you'r name: ")
last_name = input("Please enter you'r LastName: ")
major = input("Please enter you'r major: ")

#مسیر عکس مورد نظر (خام)
image_path = "C:\\Users\\Parsan Afzar\\Desktop\\ID card generator\\image1.png"

#باز کردن تصویر
img = Image.open(image_path)

#انتخاب فونت برای عکس 
font = ImageFont.load_default()

# تنظیمات عکس
img_with_text = img.copy()
draw = ImageDraw.Draw(img)

#محل قرار گیری اطلاعات
text_position1 = (500, 150)   
text_position2 = (500, 390)  
text_position3 = (500, 560)
  
# تنظیمات نوشتاری
font_size = 36
font = ImageFont.truetype("arial.ttf", font_size)

# نوشتن اطلاعات در تصویر
draw.text(text_position1, f"{id_generator}", fill=(0, 0, 0), font=font)
draw.text(text_position2, f"{first_name} {last_name}", fill=(0, 0, 0), font=font)
draw.text(text_position3, f"{major}", fill=(0, 0, 0), font=font)


#دخیره تصویر
output_image_path = "output_image.png"
img.save(output_image_path)

#چاپ خروجی
print(f"Student ID Card has been generated. Saved as {output_image_path}")