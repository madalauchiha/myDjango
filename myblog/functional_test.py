from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:8000')

assert '欢迎光临我的博客' in browser.title
