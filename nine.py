from PIL import Image

#返回要粘贴照片长度，和空白照片
def crop_equalization(image_path):
    image = Image.open(image_path)

    width, heigh = image.size

    new_long = heigh if width > heigh else width
    print(new_long)
    re = image.crop((0, 0, new_long, new_long))
    return new_long, re

#在空白照片上粘贴上九张照片，形状为心形的
def create_new_pic(image_path):
    new_long, min_pic = crop_equalization(image_path)
    new_image = Image.new("RGBA", (new_long * 9, new_long * 9), color='white')
    for i in range(13):
        if i <= 3: continue
        if i <= 8:
            new_image.paste(min_pic, (new_long * (i - 4), new_long * i))

        else:
            new_image.paste(min_pic, (new_long * (i - 4), (17 - i) * new_long - new_long))

    for i in range(9):
        if i <= 2:
            new_image.paste(min_pic, (new_long * i, new_long * (3 - i)))
        if i == 3:
            new_image.paste(min_pic, (new_long * i, new_long))
        if i == 4:
            new_image.paste(min_pic, (new_long * i, 2 * new_long))
        if i == 5:
            new_image.paste(min_pic, (new_long * i, new_long))
        if i >= 6:
            new_image.paste(min_pic, (new_long * i, new_long * (i - 5)))

    new_image.show()
    new_image.save('mumunine.png')

#剪切成九份
def cut_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    print(image_list)

    return save_images(image_list)

#保存照片
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    cut_image('mumunine.png')
