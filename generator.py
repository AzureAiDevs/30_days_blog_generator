"""
Python app to read a blog.yaml and generate a blog file structure
and index.md markdown file from a template
"""

import datetime
import os
import pathlib
import argparse
import shutil
import jinja2   # https://pypi.org/project/Jinja2/
import oyaml as yaml
import banner_1080p


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder_item")
parser.add_argument("-w", "--website_folder")
parser.add_argument("-c", "--content_name")


TEMPLATE_FILE = "template.md"
DAYS_FILE = "blog.yaml"

banner = banner_1080p.Banner1080p("authors.yml")


def path_exists(path):
    """ This function is used in the template to check if a file exists """

    return os.path.exists(path)

def copy_media_files(folder_name, output_folder):
    """Copy project assets to MS Learning format"""

    # check if the media folder exists
    src = os.path.join('./content', folder_name, 'media')

    if os.path.exists(src):
        # Copy all the media files to the media folder
        dst = os.path.join(output_folder, 'media')
        shutil.rmtree(os.path.join(dst), ignore_errors=True)
        shutil.copytree(src, dst)


def create_content_folder(content_folder):
    """Create the content folder structure"""

    # create the content folder
    print(f"Creating content folder {content_folder}.")
    pathlib.Path(content_folder).mkdir(parents=True, exist_ok=True)

    # create the media folder
    media_folder = os.path.join(content_folder, "media")
    pathlib.Path(media_folder).mkdir(parents=True, exist_ok=True)

    filename = os.path.join(content_folder, 'media', 'README.txt')
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('Add all your media files to media directory.')

    # create the a intro.md file
    filename = os.path.join(content_folder, 'intro.md')
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('[//]: # (Add your blog markdown introduction here)\n')

    # create the a covered.md file
    filename = os.path.join(content_folder, 'covered.md')
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('[//]: # (Add the main areas covered as markdown bullet points.)\n')

    # create the a references.md file
    filename = os.path.join(content_folder, 'references.md')
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('[//]: # (Add tagged references to docs/learn/tech as markdown bullet points)\n')


    filename = os.path.join(content_folder, 'body.md')
    with open(filename, encoding='utf8', mode='w') as file:
        file.write('[//]: # (This is where you write the body of the blog post in markdown)\n')


def validate_data(data):
    """Validate the yaml file."""

    previous_date = None

    if 'campaign' not in data:
        print("Missing campaign in yaml file")
        return False
    # if 'slug' not in data['campaign']:
    #     print("Missing slug in yaml file")
    #     return False
    if 'name' not in data['campaign']:
        print("Missing name in yaml file")
        return False
    if 'daily_blog_url' not in data['campaign']:
        print("Missing daily_blog_url in yaml file")
        return False

    for item in data['campaign']['days']:
        if 'folder' not in item:
            print("Missing folder in yaml file")
            print(item)
            return False
        if 'title' not in item:
            print("Missing title in yaml file")
            print(item)
            return False
        if 'description' not in item:
            print("Missing description in yaml file")
            print(item)
            return False
        if 'authors' not in item:
            print("Missing authors in yaml file")
            print(item)
            return False
        if 'audience' not in item:
            print("Missing audience in yaml file. Audience is used for banner generation")
            print(item)
            return False

        try:

            item_date = datetime.datetime.strptime(
                item['folder'][:10], '%Y-%m-%d').date()

            # compare the date with the previous date
            if previous_date is not None and item_date < previous_date:
                print("Dates are not in order")
                print(item)
                return False

            previous_date = item_date

        except ValueError:
            print(
                "Invalid date in yaml file - the folder name must be in the format YYYY-MM-DD and optionally, followed with a dash and short description.")
            print(item)
            return False

        ## check if the folder exists
        content_folder = os.path.join('./content', item['folder'])
        if not os.path.exists(content_folder):
            create_content_folder(content_folder)

    return True


def main(website_folder, content_name, folder_item):
    """Generate blog items from yaml file."""

    blog_folder = os.path.join(website_folder, content_name) if website_folder else 'blog'
    static_image_folder = os.path.join(website_folder, "static", "img", content_name) if content_name else 'img'

    pathlib.Path(blog_folder).mkdir(parents=True, exist_ok=True)
    pathlib.Path(static_image_folder).mkdir(parents=True, exist_ok=True)

    day = 0
    week = 0

    # Read the yaml file
    with open(DAYS_FILE, encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.Loader)

    if not validate_data(data):
        print("Error in yaml file")
        return

    # Read the template file
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)

    template_env.filters['path_exists'] = path_exists

    template = template_env.get_template(TEMPLATE_FILE)

    for item in data['campaign']['days']:
        day += 1
        item['day'] = day
        item['campaign'] = data['campaign']['name']
        item['static_img_folder'] = data['campaign']['static_img_folder']
        item['static_img_path'] = data['campaign']['static_img_path']
        item['daily_blog_url'] = data['campaign']['daily_blog_url']
        item['social_tags'] = data['campaign']['social_tags']

        if folder_item and item['folder'] != folder_item:
            continue

        output_text = template.render(item)

        folder_name = os.path.join(blog_folder, item['folder'])

        pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
        filename = os.path.join(folder_name, 'index.md')

        with open(filename, 'w', encoding='utf8') as f:
            f.write(output_text)

        copy_media_files(item['folder'], folder_name)

        # add an value to the item dictionary

        item['folder_name'] = folder_name
        item['folder_count'] = len(data['campaign']['days'])
        item['static_image_folder'] = static_image_folder
        item['day'] = day
        item['date'] = item['folder'][:10]

        recap_filename = os.path.join('./content', item['folder'], 'recap.md')

        if os.path.isfile(recap_filename):
            week += 1
            item['recap'] = week



        banner.create_banner(item)

        # return

    print("Done")


if __name__ == '__main__':

    args = parser.parse_args()

    main(args.website_folder, args.content_name, args.folder_item)
