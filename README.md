# Bypass Admin Automated Testing

The goal of this repo is to begin automating test cases from the Admin test suite. Written in Python, Selenium-Webdriver is used as the browser automation framework, Chrome or Firefox for full browser testing, and PhantomJS for headless browser testing.


### Differences vs. Other Attempted Automation Projects
Compared to previous attempts at automated testing, there are several differences in this project, mainly:

  - Written in Python, instead of Java
  - Highly abstracted page objects
  - Element location logic seperate from pages/tests
  - Test data read from input files, not hardcoded
  
These changes will help to solve the two main issues other attempts at test automation projects have run into, translating of manual test cases and updating to support changes to Admin.


### Requirements
  - Python2
  - Google Chrome
  - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home)
  - [PhantomJS](http://phantomjs.org/)
  - Python Modules: `pip install -r requirements.txt`
