# coding:utf-8
# python 3.5.2 , django 1.8
# P12


from selenium import webdriver


browser = webdriver.Chrome()

# Lily heard there is a application website
# She visit the homepage
browser.get('http://localhost:8000')

# User noticed the web title include word "To-Do"
assert 'To-Do' in browser.title

# 应用邀请她输入一个待办事项

# 她在一个文本框中输入了"Buy peacock feather's"

# Lily's hobby是使用假蝇做饵钓鱼

# 她按回车键,页面更新了

# 待办事项表格中显示了"1: Buy peacock feathers"

# 页面中又显示了一个文本框,可以输入其他的待办事项

# 她输入了"Use peacock feathers to make a fly"

# Lily做事很有条理

# 页面再次更新,她的清单中显示了这两个待办事项

# Lily想知道这个网站是否会记住她的清单

# 她看到网站为她生成了一个唯一的URL
# 而且页面中有一些文字解说这个功能

# 她访问那个URL,发现她的待办事项列表还在

# 她很满意,去睡觉了

browser.quit()    # close browser
