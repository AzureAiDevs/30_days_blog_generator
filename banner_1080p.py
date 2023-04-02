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

SUPERHERO_URL = 'https://raw.githubusercontent.com/AzureAiDevs/30_days_blog_generator/main/assets/superheros/superhero-{hero}.png'


class BANNER_1080p:
    """Load YAML file"""

    def __init__(self, file_path, blog_url):
        random.seed()
        self.used_heroes = []

        self.blog_url = blog_url

        self.font_folder = '/System/Library/Fonts/Supplemental'
        self.font_name = 'Arial.ttf'
        self.font_bold_name = 'Arial Bold.ttf'

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

        draw = ImageDraw.Draw(output)
        draw.ellipse((0, 0) + size, fill=None, outline='black', width=4)

        output.putalpha(mask)



        return output.resize((240, 240))
    
    def __add_text(self, draw, text, loc, font_size, font_name, color):
        """Add text to the image"""
        font = ImageFont.truetype(os.path.join(self.font_folder, font_name), font_size)
        draw.text(loc, text, font=font, fill=color)

    def __add_banner_text(self, draw, audience, title, day, date):
        """Add text to the banner image"""
        audience_loc = (310, 180)
        date_loc = (50, 305)
        day_loc = (50, 221)
        divider_loc = (236, 150)
        title_loc = (310, 312)

        audience_font_size = 110
        date_font_size = 55
        day_font_size = 80
        divider_font_size = 220
        title_font_size = 80


        printable = set(string.printable)
        audience = ''.join(filter(lambda x: x in printable, audience))
        title = ''.join(filter(lambda x: x in printable, title))

        date_string = datetime.datetime.strptime(date, '%Y-%m-%d')
        date = date_string.strftime('%b %d')

        self.__add_text(draw, date_string.strftime('%a'), day_loc, day_font_size, self.font_bold_name, (111, 61, 212))
        self.__add_text(draw, date, date_loc, date_font_size, self.font_bold_name, (111, 61, 212))
        self.__add_text(draw, "|", divider_loc, divider_font_size, self.font_name, (0, 0, 0))

        # self.__add_text(draw, 'DAY', (45, 307), 30, self.font_name, (0, 0, 0))
        # self.__add_text(draw, "{:d}".format(day), day_loc, day_font_size, self.font_name, (0, 0, 0))

        self.__add_text(draw, audience, audience_loc, audience_font_size, self.font_bold_name, (0, 0, 0))
        self.__add_text(draw, title, title_loc, title_font_size, self.font_bold_name, (111, 61, 212))


    def __add_profile_image(self, img, draw, item, name, tag, image_url):
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
            output = self.__get_image_circle(image_url)
            img.paste(output, image_loc[item], output)
        except BaseException as e:
            print(e)

    def __add_keyword_image(self, img, draw, keywords):
        """Add keyword image to the banner image"""
        keyword_loc = [(320, 800), (520, 800), (720, 800), (920, 800),
                       (1120, 800), (1320, 800), (1520, 800), (1720, 800)]
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

        folder_count = banner_definition["folder_count"]
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
        
        if item == 1:
            # write code to generate a random ai superhero between 1 and 30 (inclusive) check if the number has been used before

            hero = random.randint(1, folder_count)
            # has this hero been used before?
            if hero in self.used_heroes:
                # if so, generate a new hero
                while hero in self.used_heroes:
                    hero = random.randint(1, folder_count)
            # add the hero to the list of used heroes
            self.used_heroes.append(hero)
            # generate the url
            hero_url = SUPERHERO_URL.format(hero = hero)

            self.__add_profile_image(img, draw, 1, "AI Superhero", "#dalle2 art", hero_url)
 

        # filename = os.path.join(banner_definition["blog_folder"], 'banner.png')
        # img.save(filename)

        # The open_graph_folder is the folder where static images will be stored for the open graph image for use on twitter and facebook

        filename = os.path.join(
            banner_definition["static_image_folder"], f'banner-day{banner_definition["day"]}.png')
        img.save(filename)
