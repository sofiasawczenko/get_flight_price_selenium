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

### 1. Install Python dependencies:
   You need to install the necessary Python libraries to run the script:
   ```bash
   pip install selenium schedule
```

### 2. Install ChromeDriver: The script uses ChromeDriver to interact with the Chrome browser. Make sure you have the appropriate version of ChromeDriver installed for your version of Google Chrome.

You can download it from here: ChromeDriver.

Alternatively, you can use webdriver-manager to automatically manage the WebDriver:

```bash
pip install webdriver-manager
```
### How It Works
The script opens the URL provided (a Google Flights page in this case).
It scrapes the flight price using Selenium's find_element method.
The extracted price is saved to a text file named price.txt.
The script is scheduled to run every two weeks using the schedule library, which allows for periodic execution.

### Running the Script
You can run the script manually or it will run automatically according to the schedule.

To start the script manually, simply run:

   ```bash
python flight_price_tracker.py
The script will scrape the price, save it to the file, and then wait for the next scheduled run in 2 weeks.
```
### Scheduling
The script is scheduled to run automatically every 2 weeks. You can adjust the scheduling frequency by modifying the schedule.every(2).weeks.do(get_flight_price) line in the code to other intervals, such as days, hours, or minutes.

### Notes
Make sure to have the Chrome browser installed on your machine and the appropriate ChromeDriver version.
You may need to configure additional options like headless mode or no-sandbox if you're running the script in environments without a graphical interface (like a server).

### Example Output
The price will be saved in price.txt, with each run appending the most recent price.

Example content in price.txt:
   ```bash
$200
```
