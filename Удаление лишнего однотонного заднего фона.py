from PIL import Image

im = Image.open('image.png')
pixels = im.load()
x, y = im.size
x1, y1, x2, y2 = x - 1, y - 1, 0, 0
background_rgb = pixels[0, 0]

for i in range(x):
    for j in range(y):
        if pixels[i, j] != background_rgb:
            if i < x1:
                x1 = i
            if i > x2:
                x2 = i
            if j < y1:
                y1 = j
            if j > y2:
                y2 = j
im.crop((x1, y1, x2 + 1, y2 + 1)).save('res.png')
