# Scrape Master

Scrape Master is a web scraping project designed to scrape data from a sample e-commerce website. This documentation provides an overview of the project structure, usage instructions, and details on the components included.

## Table of Contents

- [Scrape Master](#scrape-master)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [File Structure](#file-structure)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Output](#output)
  - [Contributing](#contributing)
  - [License](#license)

## Project Overview

Scrape Master is a web scraping project aimed at extracting data from a sample e-commerce website. The website serves as a test bed for the scraping script, which retrieves product information such as name, price, details, and reviews. The website is hosted here on GitHub, https://markcarcillar.github.io/scrape_master/. The data can be saved in various formats, including JSON, XML, and CSV.

## File Structure

The project's file structure is organized as follows:

- `index.html`: Sample website used for scraping.
- `img/`: The folder containing images.
- `main.py`: The main script for web scraping.
- `output/`: The folder where the script's results are saved in JSON, XML, or CSV format.
- `.gitignore`: Configuration file to ignore files when using Git.
- `requirements.txt`: A list of Python module requirements for the project.

## Getting Started

To get started with Scrape Master, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/markcarcillar/scrape_master.git
   ```

2. Install the required Python modules:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The primary functionality of Scrape Master is to scrape data from the sample e-commerce website. To use it, follow these steps:

1. Ensure you have completed the "Getting Started" section.

2. Run the scraping script `main.py`:

   ```bash
   python main.py
   ```

3. The script will prompt you to choose the output format (JSON, XML, CSV).

4. The scraped data will be saved in the `output/` folder.

## Output

The script provides options to save the scraped data in different formats:

- JSON: Use the `products.json` file.
- XML: Use the `products.xml` file.
- CSV: Use the `products.csv` file.

## Contributing

Contributions to Scrape Master are welcome! If you have ideas for improvements or bug fixes, please submit issues and pull requests on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

By using Scrape Master, you can easily scrape data from a sample e-commerce website and save it in various formats for further analysis or integration into other projects. Feel free to explore the code and customize it to your specific needs.

**Happy scraping!**