# eBay Transaction Automator

This project automates eBay transactions using Selenium, helping to search for items, fill out forms, and perform other tasks on eBay. The script interacts with the eBay website, performing actions like searching for items and clicking buttons based on element patterns.

### Features

- Automates eBay search functionality
- Clicks buttons and inputs text into search boxes
- Handles page load retries for more robust automation
- Searches for elements by pattern matching attributes or text

### Requirements

- Python 3.x
- Selenium WebDriver (e.g., for Firefox, Chrome)
- Geckodriver or Chromedriver installed based on your browser choice

### How to Run the Automation Script

1. Install the required dependencies:
    ```bash
    pip install selenium
    ```
2. Make sure to have the appropriate WebDriver for your browser (e.g., **geckodriver** for Firefox or **chromedriver** for Chrome).
3. cd src
4. Open the script and modify it as needed (e.g., search terms, element patterns).
5. Run the script to automate eBay transactions:
    ```bash
    python3 ebay.automator.py
    ```

### Script Flow

- The script starts by opening eBay's homepage.
- It searches for the specified search term in the search box.
- After entering the search term, it clicks the "Find" button.
- The script is customizable to handle more complex transactions.

### Notes

- This script uses `webdriver.Firefox()` by default. You can switch it to another browser like Chrome if needed by changing the WebDriver.
- The script currently uses the `Nach irgendetwas suchen` search box and the `Finden` button on the eBay German site (`ebay.de`), but this can be adjusted for different eBay sites or page structures.
