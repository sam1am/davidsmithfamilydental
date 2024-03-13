# README.md for David Smith Family Dental Website Project

## 🦷 Project Description
Welcome to the repository for the David Smith Family Dental website project! This project aims to create an interactive, informative, and accessible online presence for a local dental clinic. Leveraging markdown for articles, a Python script to build static HTML pages, and the styling finesse of Tailwind CSS, we're crafting a user-friendly experience that highlights services, staff profiles, and dental education.

The website covers various aspects of dental services, including General Dentistry, Cosmetic Dentistry, Orthodontics, and Specialty Services. Our structured approach ensures that each service is clearly presented, easily navigable, and SEO optimized to reach the Salt Lake City community effectively.

## 🛠 Installation

Before you get started, make sure you have Python and Node.js installed on your system. Our build script relies on Python, and Tailwind CSS requires Node.js for its build process.

To install the project, follow these steps:
1. Clone the repository to your local machine.
   ```
   git clone https://github.com/your-username/david-smith-dental.git
   cd david-smith-dental
   ```
2. Install the required Python dependencies.
   ```
   pip install -r requirements.txt
   ```
3. Install the Node.js dependencies required for Tailwind CSS.
   ```
   npm install
   ```

## 🚀 Usage

To generate the static website:
1. Run the build script.
   ```
   python build.py
   ```
   This script will convert markdown files into HTML, build the CSS with Tailwind, and place all the necessary assets into the `build` directory.

2. To view the website, you can open the `index.html` file located in the `build` directory with your web browser.

### Project Structure
- `articles/`: Markdown files organized by dental service category.
- `build/`: The output directory for the built static website, including HTML, CSS, and images.
- `css/`: Custom CSS and the configuration for Tailwind CSS.
- `docs/`: Documentation including project requirements and style guide.
- `images/`: Image assets used throughout the website.
- `templates/`: HTML templates for pages like the homepage, contact, services, and more.

## 🙏 Acknowledgements
We'd like to extend our gratitude to:
- The David Smith Family Dental staff for their collaboration and expertise.
- [Theme Freesia](https://themefreesia.com/) for design inspiration.
- Everyone in the dental community who shared insights and feedback.

## 📜 License
This project is licensed under the [MIT License](LICENSE). Feel free to branch, fork, and adapt for your dental clinic's needs! Remember to provide attribution back to this original repository as courtesy. 

Happy Smiles! 😄🦷