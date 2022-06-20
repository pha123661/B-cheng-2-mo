from PIL import Image
from sys import argv
from os.path import basename

try:
    img_name = argv[1]
except IndexError:
    print("請把檔案直接拖放到執行檔上！")
    input("按下Enter鍵繼續...")


img = Image.open(img_name)
ori_size = img.size

new_img = img.resize((32, 32))
new_img = new_img.resize(ori_size)

new_img_name = basename(img_name).split('.')
new_img_name = f"{''.join(new_img_name[:-1])}_low_res.{new_img_name[-1]}"
new_img.save(new_img_name)
print(f"檔案：{new_img_name} 已經被逼成惡魔了")
input("按下Enter鍵繼續...")
