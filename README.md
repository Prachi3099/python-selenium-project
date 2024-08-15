
# Selenium Automation Python Project

This project automates the demo ecommerce website using Selenium webdriver and Pytest.



## Technologies Used

1. Python
2. Selenium WebDriver
3. Pytest
4. ChromeDriver
## Project Structure

1. tests/:contains test files using Pytest.
2. TestData/:contains data to be used in website.
3. utilities/:contains base class with details
    logs, waits etc.
4. pageObjects/:contains page object files 
    website interactions
## Setup Instructions

1. Install Python 3.x and pip
2. Install Selenium WebDriver using pip install
    selenium
3. Install Pytest using pip install pytest.
4. Install ChromeDriver using pip install
    webdriver-manager
5. Clone the repository and navigate to the
    project directory
## Running Tests

1. Run py.test --browser_name chrome 
    --html=reports/report1.html to run the tests
    on chrome and generate report in reports
    folder.

## Fixtures

1. Use conftest.py containing the fixtures.
2. Contains setup and teardown methods
3. contains report method to generate on failure.
## Tests

1. test_HomePage:tests home page functionality
2. test_e2e:tests end to end functionality
## pageObjects

1. HomPage:Contains home page interactions
2. CheckoutPage:Contains shop and checkout page 
    interactions
3. ConfirmPage:Contains the confirmation and
    purchase interactions
## References

1. Selenium Webdriver with Python from Scratch
    and Frameworks by Rahul Shetty
2. Selenium Python by Software Testing Mentor
