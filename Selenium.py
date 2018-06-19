#!/usr/local/bin/python3

# from selenium import webdriver
# import time
# browser = webdriver.Firefox()
#
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys('ipad')
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# print(input_str)


from selenium import webdriver
import time

brower = webdriver.Firefox()

brower.get('http://www.zol.com.cn')

brower.find_element_by_id('search_article').click()

input = brower.find_element_by_id('keyword')
input.clear()
input.send_keys('iPhone X')
brower.find_element_by_class_name('search-btn').click()

brower.switch_to.window(brower.window_handles[1])
time.sleep(2)
input2 = brower.find_element_by_class_name('search-key')
input2.clear()
input2.send_keys('iPhone 8')
brower.find_element_by_class_name('search-btn').click()

news = brower.find_elements_by_css_selector('.item-title a')
first = news[5]
first.click()

brower.switch_to.window(brower.window_handles[2])

time.sleep(3)

login = brower.find_element_by_class_name('sitenav-login-link')

login.click()

brower.switch_to.frame('zol-login-framebox')
time.sleep(5)
h3 = brower.find_elements_by_css_selector('h3')
h3[0].click()
time.sleep(2)
login_input = brower.find_element_by_id('loginUser')
mima_input  = brower.find_element_by_id('loginPwd')
login_input.clear()
mima_input.clear()
login_input.send_keys('xxxxxx')
mima_input.send_keys('xxxxxxx')
time.sleep(2)
brower.find_element_by_id('loginButton').click()
time.sleep(1)
brower.switch_to.window(brower.window_handles[2])
brower.refresh()
time.sleep(2)

brower.execute_script('window.scrollTo(0,3543)')
time.sleep(1)
brower.switch_to.frame('commentsiframe')

comment = brower.find_element_by_id('content1')
comment.click()
comment.send_keys('我来看看!呵呵呵呵')

brower.find_element_by_id('post_comment').click()


print('评论成功')