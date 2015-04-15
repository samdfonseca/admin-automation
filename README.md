# Bypass Admin Automated Testing

### Requirements
  - Python2
  - [Google Chrome](https://www.google.com/chrome/)
  - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home)
  - [PhantomJS](http://phantomjs.org/)
  - [Selenium Server](http://www.seleniumhq.org/download/)

### Setup
- Setup virtualenv.

```
$ [sudo] pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

- Install package in develop mode.

```
$ python setup.py develop
```

- Set environment variables.

```
$ export TESTRAIL_URL='https://bypassmobile.testrail.com'
$ export TESTRAIL_USER='someone@bypassmobile.com'
$ export TESTRAIL_PASSWORD='abcdefg12345'
$ export ADMIN_USER='someone@bypassmobile.com'
$ export ADMIN_PASSWORD='password1'
$ export SELENIUM_SERVER_URL='http://127.0.0.1:4444/wd/hub'
```

- Setup selenium server.

```
$ bin/selenium-server start
```

- Run tests.

 - All tests

 ```
$ nosetests tests
 ```

 - Individual modules
 
 ```
$ nosetests tests/login_test.py
 ```
 
 - Individual tests
 
 ```
$ nosetests ./testthetests/test_api_items.py:test_get_items_nondefault_user
 ```
