"""Create a banner image with text and profile image"""

from io import BytesIO
import string
import os
import platform
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import oyaml as yaml
import datetime
import random

SUPERHERO_FILEPATH = 'assets/superheros/superhero-{hero}.png'
AUTHOR_FILEPATH = 'assets/authors/{author}.png'


class Banner1080p:
    """Load YAML file"""

    def __init__(self, file_path, blog_url):
        random.seed()
        self.hero_id = 1

        self.blog_url = blog_url

        self.font_folder = '/System/Library/Fonts/Supplemental'
        self.font_name = 'Arial.ttf'
        self.font_bold_name = 'Arial Bold.ttf'

        if platform.system() == 'Windows':
            self.font_folder = 'C:\\Windows\\Fonts'
            self.font_name = 'arial.ttf'
            self.font_bold_name = 'arialbd.ttf'

        # if platform.system() == 'Linux':
        #     self.font_folder = '/usr/share/fonts/truetype/dejavu'
        #     self.font_name = 'DejaVuSans.ttf'
        #     self.font_bold_name = 'DejaVuSans-Bold.ttf'

        with open(file_path, "r", encoding="utf8") as f:
            self.authors = yaml.load(f, Loader=yaml.Loader)

    def __get_image_circle(self, author_key, url, hero_id):
        """Get image from URL and convert to circle"""

        # get author from author folder cache
        if author_key:
            author_filename = AUTHOR_FILEPATH.format(author=author_key)
            # does author image exist in cache
            if os.path.exists(author_filename):
                response = open(author_filename, 'rb')
                image = Image.open(response)
                # fill in the background of the png file with white
                if image.mode in ("RGBA", "P"):
                    # fill with a vibrate blue color
                    # 69	116	199
                    background = Image.new(image.mode[:-1], image.size, (73, 161, 233))
                    background.paste(image, image.split()[-1])
                    image = background
            else:
                try:
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()  # Raise an HTTPError if status code >= 400
                    image = Image.open(BytesIO(response.content))
                    image.save(author_filename)
                except BaseException as error:
                    raise Exception("Failed to fetch image: " + str(error))
        else:
            if hero_id:
                hero_filepath = SUPERHERO_FILEPATH.format(hero = self.hero_id)
                response = open(hero_filepath, 'rb')
                image = Image.open(response)

        size = image.size
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))

        draw = ImageDraw.Draw(output)
        draw.ellipse((0, 0) + size, fill=None, outline='black', width=4)

        output.putalpha(mask)

        return output.resize((240, 240))

    def __add_text(self, draw, text, loc, font_size, font_name, color):
        """Add text to the image"""
        font = ImageFont.truetype(os.path.join(self.font_folder, font_name), font_size)
        draw.text(loc, text, font=font, fill=color)

    def __add_banner_text(self, draw, blog_item):
        """Add text to the banner image"""
        audience_loc = (380, 180)
        day_loc = (80, 180)
        date_loc = (70, 312)  
        divider_loc = (320, 150)
        title_loc = (380, 312)
        week_loc = (32, 180)
        week_number_loc = (174, 312)

        audience_font_size = 110
        date_font_size = 74
        day_font_size = 110
        divider_font_size = 220
        title_font_size = 74
        week_font_size = 110
        week_number_font_size = 74

        audience = blog_item.get("audience")
        title = blog_item.get("title")
        date = blog_item.get("date")

        printable = set(string.printable)
        audience = ''.join(filter(lambda x: x in printable, audience))
        title = ''.join(filter(lambda x: x in printable, title))

        date_string = datetime.datetime.strptime(date, '%Y-%m-%d')
        date = date_string.strftime('%b %d')

        if blog_item.get("recap"):
            self.__add_text(draw, 'Week', week_loc, week_font_size, self.font_bold_name, (96,	96,	96))
            # format the week number with four leading spaces
            self.__add_text(draw, '{:d}'.format(blog_item.get("recap")), week_number_loc, week_number_font_size, self.font_bold_name, (96,	96,	96))
            self.__add_text(draw, "|", divider_loc, divider_font_size, self.font_name, (0, 0, 0))

        else:
            self.__add_text(draw, date_string.strftime('%a'), day_loc, day_font_size, self.font_bold_name, (96,	96,	96))
            self.__add_text(draw, date, date_loc, date_font_size, self.font_bold_name, (96,	96,	96))
            self.__add_text(draw, "|", divider_loc, divider_font_size, self.font_name, (0, 0, 0))

        self.__add_text(draw, audience, audience_loc, audience_font_size, self.font_bold_name, (0, 0, 0))
        self.__add_text(draw, title, title_loc, title_font_size, self.font_bold_name, (111, 61, 212))


    def __add_profile_image(self, img, draw, item, author, name, tag, image_url, hero_id=None):
        """Add profile image to the banner image"""
        name_loc = [(580, 550), (1380, 550)]
        tag_loc = [(580, 606), (1380, 606)]
        image_loc = [(320, 500), (1120, 500)]
        font_size = 46

        if item > len(name_loc) - 1:
            return

        self.__add_text(draw, name, name_loc[item], font_size, self.font_name, (0, 0, 0))
        self.__add_text(draw, tag, tag_loc[item], font_size, self.font_name, (0, 0, 0))

        try:
            output = self.__get_image_circle(author, image_url, hero_id=hero_id)
            img.paste(output, image_loc[item], output)
        except BaseException as e:
            print(e)

    def __add_keyword_image(self, img, blog_item):
        """Add keyword image to the banner image"""
        keyword_loc = [(960, 815), (1160, 815), (760, 815), (1360, 815),
                       (560, 815), (1560, 815), (360, 815), (1760, 815)]
        keyword_count = 0

        keywords = blog_item.get("keywords")

        for keyword in keywords:

            if keyword_count > len(keyword_loc) - 1:
                break

            filename = 'assets/icons/' + keyword + '.png'
            if os.path.exists(filename):
                keyword_img = Image.open(filename)
                offset = 0 if len(keywords) % 2 == 1 else 100
                location = (keyword_loc[keyword_count][0] - round(keyword_img.size[0] / 2) - offset, keyword_loc[keyword_count][1])
                img.paste(keyword_img, location, keyword_img)
                keyword_count += 1
            else:
                print("Keyword image not found: " + filename)

    def __create_author_image(self, blog_item, img, draw):
        item = 0
        if blog_item.get("recap"):
            # check that there is more than one author
            if len(blog_item["authors"]) > 1:
                # remove all the banner authors except the first one
                blog_item["authors"] = blog_item["authors"][0:1]

        for author in blog_item["authors"]:
            author_item = self.authors.get(author)

            if not author_item:
                continue

            self.__add_profile_image(
                img, draw, item, author, author_item["name"], author_item["tag"], author_item["source_image_url"])
            item += 1

        if item < 2:
            self.__add_profile_image(img, draw, item, None, "AI Superhero", "#dalle2 art", None, self.hero_id)
            self.hero_id += 1

    def create_banner(self, blog_item):
        """Create the banner image"""

        img = Image.open('assets/banner-1080p.png')
        draw = ImageDraw.Draw(img)

        self.__add_banner_text(draw, blog_item)
        self.__add_keyword_image(img, blog_item)
        self.__create_author_image(blog_item, img, draw)

        filename = os.path.join(blog_item.get("static_image_folder"), f'banner-day{blog_item.get("day")}.png')
        img.save(filename)
