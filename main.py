from PIL import Image
from sys import argv
from os.path import basename

img_name = argv[1]

img = Image.open(img_name)
ori_size = img.size

new_img = img.resize((32, 32))
new_img = new_img.resize(ori_size)

new_img_name = basename(img_name).split('.')
new_img_name = f"{''.join(new_img_name[:-1])}_low_res.{new_img_name[-1]}"
new_img.save(new_img_name)
print(f"檔案已儲存：{new_img_name}")
