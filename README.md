# Flight Price Tracker

This project is a simple Python script that uses **Selenium** to scrape the price of a flight from a specific URL and save it to a `.txt` file. The script is also scheduled to run every two weeks using the **schedule** library.

## Features
- Scrapes flight price from a URL.
- Saves the price to a file (`price.txt`).
- Runs the script automatically every 2 weeks.

## Requirements
- Python 3.x
- Selenium
- WebDriver for Chrome (ChromeDriver)
- Schedule
- Time module

## Installation

1. **Install Python dependencies**:
   You need to install the necessary Python libraries to run the script:
   ```bash
   pip install selenium schedule
