from selenium import webdriver
import time
import math

# Задачи раздела 2.2
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Устанавливаем x и рассчитываем
    box = browser.find_element_by_tag_name('img')
    x = box.get_attribute('valuex')
    y = calc(x)

    # Вставляем полученное значене
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    time.sleep(1)

    # Галочка и выбор
    robot = browser.find_element_by_id('robotCheckbox')
    robot.click()
    rule = browser.find_element_by_id("robotsRule")
    rule.click()
    time.sleep(1)
    submit_btn = browser.find_element_by_tag_name('button')
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


