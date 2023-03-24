"""Create a banner image with text and profile image"""

from io import BytesIO
import string
import os
import platform
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import oyaml as yaml
import datetime


class BANNER_1080p:
    """Load YAML file"""

    def __init__(self, file_path, blog_url):
        self.blog_url = blog_url

        self.font_folder = '/System/Library/Fonts/Supplemental'
        self.font_name = 'Verdana.ttf'
        self.font_bold_name = 'Verdana Bold.ttf'

        if platform.system() == 'Windows':
            self.font_folder = 'C:\\Windows\\Fonts'
            self.font_name = 'verdana.ttf'
            self.font_bold_name = 'verdanab.ttf'

        if platform.system() == 'Linux':
            self.font_folder = '/usr/share/fonts/truetype/dejavu'
            self.font_name = 'DejaVuSans.ttf'
            self.font_bold_name = 'DejaVuSans-Bold.ttf'

        with open(file_path, "r", encoding="utf8") as f:
            self.authors = yaml.load(f, Loader=yaml.Loader)

    def __get_image_circle(self, url):
        """Get image from URL and convert to circle"""

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError if status code >= 400
        except BaseException as error:
            raise Exception("Failed to fetch image: " + str(error))

        image = Image.open(BytesIO(response.content))

        size = image.size
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        # # Resize image to 100x100 px
        return output.resize((150, 150))
    
    def __add_text(self, draw, text, loc, font_size, font_name, color):
        """Add text to the image"""
        font = ImageFont.truetype(os.path.join(self.font_folder, font_name), font_size)
        draw.text(loc, text, font=font, fill=color)

    def __add_banner_text(self, draw, audience, title, day, date):
        """Add text to the banner image"""
        audience_loc = (310, 180)
        audience_font_size = 110
        day_loc = (120, 236)
        day_font_size = 100
        divider_loc = (236, 190)
        divider_font_size = 160
        title_loc = (310, 330)
        title_font_size = 70
        # Define the font size and font type


        printable = set(string.printable)
        audience = ''.join(filter(lambda x: x in printable, audience))
        title = ''.join(filter(lambda x: x in printable, title))

        date_string = datetime.datetime.strptime(date, '%Y-%m-%d')
        date = date_string.strftime('%b %d, %Y')


        self.__add_text(draw, audience, audience_loc, audience_font_size, self.font_bold_name, (127, 127, 127))
        self.__add_text(draw, 'DAY', (45, 307), 30, self.font_name, (127, 127, 127))
        self.__add_text(draw, "{:d}".format(day), day_loc, day_font_size, self.font_name, (127, 127, 127))
        self.__add_text(draw, "|", divider_loc, divider_font_size, self.font_bold_name, (127, 127, 127))
        self.__add_text(draw, title, title_loc, title_font_size, self.font_bold_name, (111, 61, 212))

        self.__add_text(draw, date, (45, 351), 30, self.font_name, (127, 127, 127))


    def __add_profile_image(self, img, draw, item, name, tag, image_url):
        """Add profile image to the banner image"""
        name_loc = [(500, 510), (500, 750)]
        tag_loc = [(500, 576), (500, 806)]
        image_loc = [(320, 515), (320, 750)]
        font_size = 46

        if item > len(name_loc) - 1:
            return

        self.__add_text(draw, name, name_loc[item], font_size, self.font_name, (127, 127, 127))
        self.__add_text(draw, tag, tag_loc[item], font_size, self.font_name, (127, 127, 127))

        try:
            output = self.__get_image_circle(image_url)
            img.paste(output, image_loc[item], output)
        except BaseException as e:
            print(e)

    def __add_keyword_image(self, img, draw, keywords):
        """Add keyword image to the banner image"""
        keyword_loc = [(1030, 520), (1230, 520), (1430, 520), (1630, 520),
                       (1030, 754), (1230, 754), (1430, 754), (1630, 754)]
        keyword_count = 0
        for keyword in keywords:

            if keyword_count > len(keyword_loc) - 1:
                break

            filename = 'assets/icons/' + keyword + '.png'
            if os.path.exists(filename):
                keyword_img = Image.open(filename)
                img.paste(keyword_img, keyword_loc[keyword_count], keyword_img)
                keyword_count += 1
            else:
                print("Keyword image not found: " + filename)

    def create_banner(self, banner_definition):
        """Create the banner image"""

        img = Image.open('assets/banner-1080p.png')
        draw = ImageDraw.Draw(img)
        item = 0

        self.__add_banner_text(
            draw, banner_definition["audience"], banner_definition["title"], banner_definition["day"], banner_definition["date"])
        self.__add_keyword_image(img, draw, banner_definition["keywords"])
        for author in banner_definition["authors"]:
            author_item = self.authors.get(author)

            if not author_item:
                continue

            self.__add_profile_image(
                img, draw, item, author_item["name"], author_item["tag"], author_item["image_url"])
            item += 1

        # filename = os.path.join(banner_definition["blog_folder"], 'banner.png')
        # img.save(filename)

        # The open_graph_folder is the folder where static images will be stored for the open graph image for use on twitter and facebook

        filename = os.path.join(
            banner_definition["static_image_folder"], f'banner-day{banner_definition["day"]}.png')
        img.save(filename)
