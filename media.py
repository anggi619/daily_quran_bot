import requests
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter


class Media:
    def download_image(self):
        url = 'https://picsum.photos/720/1280/?random'
        r = requests.get(url=url)
        with open("downloaded_bg.png", 'wb') as f:
            f.write(r.content)
        print("download finished")

    def process_image(self, text, author, ayah_num):
        text = textwrap.fill(text, width=35)
        image = Image.open("downloaded_bg.png").filter(ImageFilter.GaussianBlur(10))
        image = ImageEnhance.Brightness(image)
        image.enhance(0.5).save('image.png')
        image = Image.open('image.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('Raleway-Regular.ttf', size=28)
        w, h = draw.textsize(text, font=font)
        draw.text(((720 - w) / 2, (1280 - h) / 2), text, (255, 255, 255), align="center", font=font)
        if author is not None:
            # _author = '@%s' % str(author)
            _author = author + " : " + ayah_num
            x, y = draw.textsize(_author, font=font)
            font = ImageFont.truetype('Raleway-Bold.ttf', size=28)
            print((str(x)))
            draw.text(((720 - x) / 2, ((1280 / 2) + h)), _author, (255, 255, 255), font=font, align="bottom")
        image.save('ready.png')

