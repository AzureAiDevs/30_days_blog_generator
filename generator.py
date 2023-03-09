"""
Python app to read a blog.yaml and generate a blog file structure
and index.md markdown file from a template
"""

import datetime
import os
import pathlib
import jinja2   # https://pypi.org/project/Jinja2/
import oyaml as yaml
import argparse
import banner

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--blog_folder")
parser.add_argument("-f", "--blog_item")
parser.add_argument("-o", "--open_graph_folder")


TEMPLATE_FILE = "template.md"
DAYS_FILE = "blog.yaml"

banner = banner.BANNER("authors.yml", "https://aka-ms/ai-april")

# banner_definition = {
#     "folder": "assets/test",
#     "audience": "All AI Developers",
#     "title": "Introduction to Azure ML",
#     "day": "1",
#     "keywords": [ 'test', 'Azure-OpenAI-Services', 'Azure-Applied-AI-Services', 'Cognitive-Services', 'Custom-Vision', 'Azure-Applied-AI-Services' ],
#     "authors": [ 'Dave', 'Bea' ]
# }

# banner.create_banner(banner_definition)



def validate_data(data):
    """Validate the yaml file."""

    previous_date = None

    if 'campaign' not in data:
        print("Missing campaign in yaml file")
        return False
    if 'slug' not in data['campaign']:
        print("Missing slug in yaml file")
        return False
    if 'name' not in data['campaign']:
        print("Missing name in yaml file")
        return False
    if 'blog_url' not in data['campaign']:
        print("Missing blog_url in yaml file")
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

    return True


def main(blog_folder, blog_item, open_graph_folder):
    """Generate blog items from yaml file."""

    blog_folder = blog_folder if blog_folder else 'blog'
    open_graph_folder = open_graph_folder if open_graph_folder else 'img'

    pathlib.Path(open_graph_folder).mkdir(parents=True, exist_ok=True)

    day = 0

    # Read the yaml file
    with open(DAYS_FILE, encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.Loader)

    if not validate_data(data):
        print("Error in yaml file")
        return

    # Read the template file
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template(TEMPLATE_FILE)

    for item in data['campaign']['days']:
        day += 1
        item['day'] = day
        item['campaign'] = data['campaign']['name']
        item['slug'] = data['campaign']['slug']
        item['blog_url'] = data['campaign']['blog_url']
        item['site_url'] = data['campaign']['site_url']
        item['daily_blog_url'] = data['campaign']['daily_blog_url']
        item['social_tags'] = data['campaign']['social_tags']

        if blog_item and item['folder'] != blog_item:
            continue

        output_text = template.render(item)

        folder_name = os.path.join(blog_folder, item['folder'])

        pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
        filename = os.path.join(folder_name, 'index.md')

        with open(filename, 'w', encoding='utf8') as f:
            f.write(output_text)

        banner_definition = {
            "blog_folder": folder_name,
            "open_graph_folder": open_graph_folder,
            "audience": item["audience"],
            "title": item["title"],
            "day": day,
            "keywords": item['keywords'],
            "authors": item['authors']
        }

        banner.create_banner(banner_definition)

    print("Done")


if __name__ == '__main__':

    args = parser.parse_args()

    main(args.blog_folder, args.blog_item, args.open_graph_folder)
