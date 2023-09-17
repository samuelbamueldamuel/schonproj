import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def scrape(name):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()  # webdriver to access web. Chrome Driver in scripts

    driver.get("https://www.spglobal.com/esg/scores/results?cid=4004205")  # url to scrape
    driver.maximize_window()
    time.sleep(1)

    search_bar = driver.find_element(By.XPATH, """/html/body/div[3]/div[1]/div[3]/div/div/div[2]/div[1]/input""")
    search_bar.click()
    time.sleep(1)
    search_bar.send_keys(name)
    time.sleep(1)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(1)

    element2022 = driver.find_element(By.CLASS_NAME, "scoreModule__score")

    driver.execute_script("arguments[0].scrollIntoView();", element2022)

    element2021 = driver.find_element(By.CLASS_NAME, "scoreModule__subtitle")

    data2022 = element2022.text
    minus = element2021.text.split()[0]

    data2021 = int(data2022) + abs(int(minus))

    return data2021, int(data2022)








