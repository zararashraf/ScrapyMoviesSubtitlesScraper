# Scrapy Movie Subtitles Scraper

## Description
The Scrapy Movie Subtitles Scraper is a Python-based project using Scrapy, a popular web crawling and web scraping framework. The project is designed to extract movie data, including titles, plots, and scripts, from the website subslikescript.com. The extracted data can be stored in either a MongoDB Atlas database or a SQLite database, showcasing the data dumping capabilities of the project.

## Installation
1. Clone this repository: `git clone https://github.com/zararashraf/ScrapyMoviesSubtitlesScraper.git`
2. Install the required libraries: `pip install scrapy pymongo`
3. Configure the MongoDB connection string and the SQLite database settings in the pipelines.

## Usage
1. Run the spider by executing the command: `scrapy crawl transcripts`
2. Check the output data in the configured MongoDB Atlas or SQLite database.

## Project Structure
The project consists of the following key components:

- `spiders/transcripts.py`: Contains the Scrapy spider for scraping movie data from subslikescript.com.
- `pipelines.py`: Includes two pipelines for dumping the scraped data into a MongoDB Atlas database and a SQLite database.
- `requirements.txt`: Lists all the required dependencies for the project.

## Images
The Website in question.
![image (3)](https://github.com/zararashraf/ScrapyMoviesSubtitlesScraper/assets/36181292/199acda7-c2e9-45cd-8ac5-44bbb4a1bbf6)

Data in SQLite DB
![image (2)](https://github.com/zararashraf/ScrapyMoviesSubtitlesScraper/assets/36181292/703b6491-355f-4015-b626-fe0ca050f407)

Data in MongoDB Atlas
![image](https://github.com/zararashraf/ScrapyMoviesSubtitlesScraper/assets/36181292/4adcf6db-3004-485c-8695-9846101e1e86)
![image (1)](https://github.com/zararashraf/ScrapyMoviesSubtitlesScraper/assets/36181292/477a0458-cef6-4f6e-a8f7-8744a666f7c9)


## Libraries and Technologies Used
- Python 3.x
- Scrapy for web scraping
- pymongo for interacting with MongoDB
- sqlite3 for working with SQLite databases

## Code Repository
The source code for this project can be found on [GitHub](https://github.com/zararashraf/ScrapyMoviesSubtitlesScraper).

## Credits
- Scrapy: [https://scrapy.org/](https://scrapy.org/)
- pymongo: [https://pypi.org/project/pymongo/](https://pypi.org/project/pymongo/)
- SQLite: [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html)

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as needed.
