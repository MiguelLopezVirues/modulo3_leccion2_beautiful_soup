# 🛒 Atrezzo Vazquez Web Scraping Project

<div style="text-align: center;">
  <img src="assets/webscraping.jpg" alt="project-cover" />
</div>

## 📝 Project Overview

This project involves scraping product data from the **Atrezzo Vazquez** website, a supplier of creative props for film and media production. The goal is to extract detailed product information such as names, categories, descriptions, and images, allowing the company to better analyze its inventory.

The scraped data is used to improve product listings, assist in inventory management, and support marketing efforts for a film production company offering props for a paranormal prank reality TV show.

Key objectives:

1. Extract detailed product information across multiple pages.
2. Organize the data into a structured format (pandas DataFrame).
3. Support data-driven decisions for product listings and marketing.

## 📁 Project Structure

```bash
atrezzo-scraping/
├── data/                # Folder to store extracted data
│   └── atrezzo_data.csv
├── notebooks/           # Jupyter notebook with the scraping process
│   └── atrezzo_notebook.ipynb
├── src/                 # Web scraping and data extraction scripts
│   └── atrezzo_scraping.py
├── Pipfile              # Dependency management file
├── Pipfile.lock         # Lockfile for exact versions of dependencies
└── README.md            # Project documentation (this file)
```

## 🛠️ Installation and Requirements

To run this project, you will need the following tools and libraries:

- Python 3.8+
- pandas
- numpy
- BeautifulSoup4
- requests

**Documentation Links:**
- [pandas Documentation](https://pandas.pydata.org/)  
- [NumPy Documentation](https://numpy.org/)  
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests Documentation](https://docs.python-requests.org/en/master/)

#### Setting up the Environment with Pipenv

Clone this repository by running the following commands:
```bash
git clone https://github.com/YourGitHubUsername/atrezzo-scraping
```

To replicate the project's environment, use Pipenv with the included ``Pipfile.lock``:
```bash
pipenv install
pipenv shell  
```

Alternatively, install the dependencies from ``requirements.txt``:
```bash
pip install -r requirements.txt  
```

## 📊 Results and Conclusions

For detailed results, please check the ``atrezzo_notebook.ipynb`` notebook, which contains the process of extracting and analyzing the product data from the website.

## 🔄 Next Steps

- Expand the scraping to cover more pages and categories.
- Improve error handling for better robustness during extraction.

## 🤝 Contributions

Contributions are welcome! Feel free to open a pull request or an issue for any suggestions or improvements.

## ✒️ Authors

Miguel López Virues - [GitHub Profile](https://github.com/MiguelLopezVirues)  

## 📜 License

This project is licensed under the MIT License.