# Bypass Admin Automated Testing

### Requirements
  - Python2
  - Google Chrome
  - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home)
  - [PhantomJS](http://phantomjs.org/)
  - [Selenium Server](http://repo1.maven.org/maven2/org/seleniumhq/selenium/selenium-server/)

### Setup
- Setup virtualenv.

```
~/admin-automation $ [sudo] pip install virtualenv
~/admin-automation $ virtualenv venv
~/admin-automation $ source venv/bin/activate
```

- Install package in develop mode.

```
~/admin-automation $ python setup.py develop
```

- Set environment variables.

```
~/admin-automation $ export TESTRAIL_URL='https://bypassmobile.testrail.com'
~/admin-automation $ export TESTRAIL_USER='someone@bypassmobile.com'
~/admin-automation $ export TESTRAIL_PASSWORD='abcdefg12345'
~/admin-automation $ export SELENIUM_SERVER_URL='http://127.0.0.1:4444/wd/hub'
```

- Setup selenium server. (Only if using local machine to run tests)

```
~/admin-automation $ cd bin
~/admin-automation/bin $ wget http://selenium-release.storage.googleapis.com/2.44/selenium-server-standalone-2.44.0.jar
~/admin-automation/bin $ wget http://chromedriver.storage.googleapis.com/2.14/chromedriver_mac32.zip
~/admin-automation/bin $ unzip chromedriver_mac32.zip && rm chromedriver_mac32.zip
~/admin-automation/bin $ wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.0.0-macosx.zip
~/admin-automation/bin $ mv phantomjs-2.0.0-macosx/bin/phantomjs . && rm -rf phantomjs-2.0.0-macosx
~/admin-automation/bin $ export PATH="$(pwd):$PATH"
~/admin-automation/bin $ java -jar selenium-server-standalone-2.44.0.jar
```

- Run tests.

 - All tests

 ```
 ~/admin-automation $ nosetests tests
 ```

 - Select test modules
 
 ```
 ~/admin-automation $ nosetests tests/login_test.py
 ```
