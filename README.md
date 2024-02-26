# Selenium Automated Testing Script for E-commerce Website

## Overview

This Python script utilizes the Selenium WebDriver to automate testing of various functionalities on an e-commerce website. The script logs into the website, searches for a specific product, selects product options (size and color), adds the product to the cart, and verifies successful addition to the cart.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver


## Installation

1. nstall Python 3.x from the official website: Python.org
2. Install Selenium WebDriver using pip:
   ```bash
    pip install selenium
    ```
3. Download Chrome WebDriver compatible with your Chrome browser version from the official site.
4. Extract the chromedriver executable and add it to your system PATH or place it in the same directory as the script.

## Usage

1. Open the `config.py` file and update the following variables with your login credentials:

- `email`: Your email address for logging into the website.
- `password`: Your password for logging into the website.

Example:
   ```bash
    email = "your_email@example.com"
    password = "your_password"
   ```

2. Run the `test.py` script:
   ```bash
   python test.py
   ```

3. The script will automatically launch Google Chrome, navigate to the specified website, log in with the provided credentials, search for the "Radiant Tee" product, select size and color options, add the product to the cart, and verify successful addition to the cart.

4. Once the script execution is complete, you will see a success message printed in the console indicating that the product has been successfully added to the cart.

## Notes

- Ensure that the Chrome WebDriver (`chromedriver`) is compatible with your Chrome browser version. You may need to update the `chromedriver` if you encounter any compatibility issues.

## Troubleshooting

- If you encounter any issues or errors while running the script, please ensure that all dependencies are properly installed and configured. Additionally, verify that the provided login credentials are correct and that the website structure has not changed.
