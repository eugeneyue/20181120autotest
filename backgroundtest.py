from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://baidu.com')                              #打开百度首页，可以更换引号内的网址实现打开任一网址
print(driver.title)                                          #在编辑器的终端可以看到网站的标题打印出来
driver.quit()                                               #关闭Chrome浏览器，如果不写这句话浏览器就会停留在百度首页在后台运行不会关闭浏览器
