# Argentina properties web scraper

## Table of contents
* [General info](#general-info)
* [Key components](#key-components)
* [Setup](#setup)
* [Links](#links)
* [Contact](#contact)

## General info
This application constitutes a tool to search for properties (departments, houses, etc) in the most popular argentinean websites. 
<br>It is also possible to replicate the idea for other countries and add new web pages with small effort. 

## Key components
- Main script that executes the app
- Objects folder, with side scripts used by main one to build the scraper
- Profiles folder, because each website has its own configuration (YAML used)
- Data folder, with output (CSV format) for each website
  
## Setup
### - General
Clone this repo locally or wherever you can run Python from. Dependencies are managed with Poetry, so having Python and a Poetry environment setup is a must.
<br>Libraries requirements:
- python = "^3.9"
- PyYAML = "^6.0"
- bs4 = "^0.0.1"
- pandas = "^1.5.3"
- cloudscraper = "^1.2.69"

**Note:** this project was developed using Pycharm. This tool is a little tricky in terms of configuring relative paths. If you try to execute the tool in another environment and throws errors due to missing libraries, not-working imports and such things, please, let me know!

### - With terminal (or Pycharm's terminal)
```bash
cd src
poetry run python3 main.py
```

### - With PyCharm
Select main script, right click on it and click on "run"

## Links
* [cloudscraper](https://github.com/venomous/cloudscraper) -> specially useful for Zonaprop's site use of CloudFlare
* [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) -> read the docs of this wonderful crawler
* [zona-prop-scraping](https://github.com/Sotrosca/zona-prop-scraper) -> scraper from where I took a lot of ideas

## Contact
> Mail: [alfredorivas.arg@gmail.com](alfredorivas.arg@gmail.com) &nbsp;&middot;&nbsp;
> GitHub: [@alfredorivas](https://github.com/alfredorivas) &nbsp;&middot;&nbsp;
> Twitter: [@alfioarg](https://twitter.com/alfioarg)
