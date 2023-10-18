import time

from selenium import webdriver
from selenium.webdriver.common.by import By

f = open("../../../../code/ant/AIGC/Claude2-PyAPI/mybot/book/out.txt", "a")


url = 'https://tw.avsohu.com/read/99610_060/77984652.html'

# 创建一个 Chrome 浏览器实例
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 使用无头模式
driver = webdriver.Chrome(options=options)

pre_title = ""
while "read" in url:
    start = time.time()
    # 访问指定的 URL
    driver.get(url)

    header = driver.find_elements(By.TAG_NAME, "header")
    title = header[-1].find_element(By.TAG_NAME, 'div')
    print("当前正在爬取 {} ...".format(title.text))
    if pre_title != title.text:
        f.write("\n\n")
        f.write(title.text)
        f.write("\n")
    pre_title = title.text

    # 提取网页中的文本信息
    div_element = driver.find_element(By.ID, 'content')

    texts = div_element.find_elements(By.TAG_NAME, 'p')
    for text in texts:
        if text.text == "":
            continue
        f.write(text.text)
        f.write("\n")

    # 查找 div 元素
    div_element = driver.find_element(By.CLASS_NAME, 'page')

    # 查找 div 元素内部的所有 a 元素
    a_elements = div_element.find_elements(By.TAG_NAME, 'a')

    # 遍历所有 a 元素，查找文本内容为“下一章”的元素
    for a in a_elements:
        if a.text == '下一章':
            # 获取元素的 href 属性值
            href = a.get_attribute('href')
            url = href
            break
    end = time.time()
    print('Time cost: {:.3f}s'.format(end - start))
    print("ok!")
    time.sleep(0.1)

# 关闭浏览器实例
driver.quit()
