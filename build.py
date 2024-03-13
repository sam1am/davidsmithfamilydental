import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader
import subprocess
from datetime import datetime

def load_markdown_files():
    # Load markdown files from the ./articles folder
    path = 'articles'
    articles = []
    for category in os.listdir(path):
        category_path = os.path.join(path, category)
        if os.path.isdir(category_path):
            for filename in os.listdir(category_path):
                file_path = os.path.join(category_path, filename)
                if os.path.isfile(file_path) and filename.endswith('.md'):
                    with open(file_path, 'r') as f:
                        content = f.read()
                        lines = content.split('\n')
                        title = lines[0].strip('#').strip()
                        slug = title.replace(' ', '_').lower()
                        creation_time = os.path.getctime(file_path)
                        articles.append({
                            'category': category,
                            'title': title,
                            'slug': slug,
                            'content': markdown.markdown('\n'.join(lines[1:])),
                            'creation_time': creation_time
                        })
    articles.sort(key=lambda x: x['creation_time'], reverse=True)
    return articles



def build_website():
    try:
        # rename build/ to build_old/
        if os.path.exists('docs'):
            shutil.move('docs', 'docs_old')

        # Create a Jinja2 environment
        env = Environment(loader=FileSystemLoader('templates'))

        # Load the processed markdown content
        articles = load_markdown_files()

        # Render the templates with the processed content
        pages = {
            'index.html': env.get_template('index.html').render(),
            'articles.html': env.get_template('articles.html').render(articles=articles),
            'contact.html': env.get_template('contact.html').render(),
            'insurance.html': env.get_template('insurance.html').render(),
            'services.html': env.get_template('services.html').render(),
            'staff.html': env.get_template('staff.html').render(),
            # Add other pages here...
        }

        # Create the build folder if it doesn't exist
        os.makedirs('docs', exist_ok=True)

        # Save the generated HTML files to the build folder
        for filename, content in pages.items():
            with open(os.path.join('docs', filename), 'w') as f:
                f.write(content)

        # Generate individual article pages
        article_template = env.get_template('article.html')
        for article in articles:
            slug = article['title'].replace(' ', '_').lower()
            filename = f"{slug}.html"
            content = article_template.render(article=article)
            category_path = os.path.join('docs', 'articles', article['category'])
            os.makedirs(category_path, exist_ok=True)
            with open(os.path.join(category_path, filename), 'w') as f:
                f.write(content)

        # Copy static assets to the build folder
        shutil.copytree('css', 'docs/css', dirs_exist_ok=True)
        shutil.copytree('images', 'docs/images', dirs_exist_ok=True)
        # Copy other static assets as needed...

        subprocess.run(['npx', 'tailwindcss', '-i', 'css/tailwind.css', '-o', 'build/css/tailwind.css'])

        print('Website built successfully!')
        if os.path.exists('docs_old'):
            shutil.rmtree('docs_old')

    except Exception as e:
        print('An error occurred while building the website:')
        print(e)
        # If an error occurs, restore the old build folder
        if os.path.exists('docs_old'):
            shutil.move('docs_old', 'docs')



if __name__ == '__main__':
    build_website()
