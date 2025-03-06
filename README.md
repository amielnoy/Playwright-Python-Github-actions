🎭 Playwright Python Example 🎭
twitter YouTube Channel dev run nightly Imports: isort Code style: black

📃 Articles written about this project
Test Automation - How To Use Custom User Agent in Selenium Python or Playwright Python to Avoid Security Bots
Test Automation - How to Use Dynamic Base URLs with Selenium And Playwright Python in GitHub Actions
Test Automation - Maximizing Browser Window With Playwright Python And Pytest
Test Automation - How to Bypass Re-Login With Playwright Python And Pytest
Test Automation - How To Perform Automated Accessibility Checks Using Playwright Python And Axe
Test Automation - How To Link Playwright Traces and Videos to Allure Report using GitHub Actions
Test Automation - Speeding Up Testing with Playwright Python using Local Storage
Test Automation - Efficient Element Selection with Playwright Python using Test IDs
Test Automation - Flexible Test Execution with Playwright Python and GitHub Actions
Test Automation - Accelerating Playwright Python Tests with Parallel Execution in GitHub Actions
Test Automation - How to Sync Playwright Versions Between Python and GitHub Actions
🛠️ Tech Stack
Tool	Description
allure-pytest	Allure reporting with your Pytest tests for better reporting
axe-playwright-python	Python library for running accessibility checks with Playwright
playwright	Python library to automate the Chromium, WebKit, and Firefox browsers through a single API.
pytest	Popular testing framework for Python
pytest-base-url	Pytest plugin for setting a base URL for your tests
pytest-playwright	Pytest plugin for Playwright integration for browser automation testing
pytest-split	Pytest plugin which splits the test suite to equally sized sub suites based on test execution time.
requests	Versatile library for making HTTP requests in Python
⚙️ Setup Instructions
Clone the project
git clone https://github.com/nirtal85/Playwright-Python-Example
cd playwright-python
Create and activate a virtual environment
For Windows:
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
For Mac:
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
Install Poetry
pip install poetry
Install Project Dependencies
poetry install --no-root
Install playwright
playwright install
🏃‍♂️ Running Tests
pytest
When no browser was selected then chrome will be used.

Run according to tags:
pytest -m <tag_name>
📊 Viewing Test Results
Install Allure Commandline To View Test results
For Windows:
Follow the instructions here to install Scoop.
Run the following command to install Allure using Scoop:

scoop install allure
For Mac:
brew install allure
View Results Locally:
allure serve allure-results
View Results Online:
View allure results via Github pages

View trace results:
Navigate to the Playwright Trace Viewer
Locate the trace file stored under the test-results folder. This file is generated after running your tests. Click on the 'Upload' button in the Playwright Trace Viewer and select your trace file.
After uploading, the trace viewer will display a detailed timeline of events that occurred during your test. This includes network requests, JavaScript execution, and browser interactions. You can click on individual events for more details.
ℹ️ View Help And Other CLI Options
pytest --help
Pre Commit
Run Pre Commit Checks Automatically
pre-commit install
pre-commit install --hook-type commit-msg
Bump Pre Commit Hooks Version
pre-commit autoupdate
Run Pre Commit Checks Manually On The Entire Project
pre-commit run --all-files
About
Playwright Python example project with pytest and Allure report

Topics
testing python3 pytest allure github-actions playwright playwright-python
Resources
 Readme
License
 Apache-2.0 license
Code of conduct
 Code of conduct
Security policy
 Security policy
 Activity
Stars
 72 stars
Watchers
 3 watching
Forks
 15 forks
Report repository
Releases
No releases published
Packages
No packages published
Contributors
4
@nirtal85
nirtal85 Nir Tal
@renovate[bot]
renovate[bot]
@dependabot[bot]
dependabot[bot]
@elias-shoursoh
elias-shoursoh
Deployments
500+
 github-pages 18 hours ago
+ more deployments
Languages
Python
100.0%
Footer
© 2025 GitHub, Inc.
Footer navigation
Terms
Privacy