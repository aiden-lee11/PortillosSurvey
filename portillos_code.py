from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver_opts = Options()
driver_opts.binary_location = r"C:\Program Files\Mozilla Firefox/firefox.exe"

code = "160 007 500 050 010 298 70"
#code = input("What's your code? ")
user_boxes = code.split(" ")

driver = webdriver.Firefox(options=driver_opts)


def next():
    driver.find_element(By.ID, "NextButton").click()
    sleep(0.01)

def get_dat_code():
    driver.get("https://tellportillos.smg.com/")
    # Page 1
    for i in range(len(user_boxes)):
        driver.find_element(By.ID, f"CN{i + 1}").send_keys(user_boxes[i])
    next()

    # Page 2
    driver.find_element(
        By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[3]/label"
    ).click()
    next()

    # Page 3
    driver.find_element(By.XPATH, '//*[@id="textR000006.1"]').click()
    next()

    # Page 4
    progress_bar = driver.find_element(By.ID, "Progress")
    action = ActionChains(driver)
    action.move_to_element_with_offset(progress_bar, 0, -100).click().perform()
    # 200 pixels from bottom button to top,   110 between bar and center bubble
    for i in range(4):
        action.move_by_offset(0, -50).click().perform()
    next()

    # Page 5
    progress_bar = driver.find_element(By.ID, "Progress")
    action = ActionChains(driver)
    action.move_to_element_with_offset(progress_bar, 0, -100).click().perform()
    # 200 pixels from bottom button to top,   110 between bar and center bubble
    for i in range(4):
        action.move_by_offset(0, -50).click().perform()
    next()

    # Page 6
    progress_bar = driver.find_element(By.ID, "Progress")
    action = ActionChains(driver)
    action.move_to_element_with_offset(progress_bar, 0, -100).click().perform()
    # 200 pixels from bottom button to top,   110 between bar and center bubble
    action.move_by_offset(0, -50).click().perform()
    next()

    # Page 7
    driver.find_element(
        By.XPATH, "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label"
    ).click()
    next()
    # Page 8
    driver.find_element(
        By.XPATH, "/html/body/div[1]/main/div[2]/form/div/fieldset/div/div/div[4]/span/span"
    ).click()
    next()

    # Page 9
    highly_likely_bar = driver.find_element(By.ID, "HighlyLikelyDESC5")
    action = ActionChains(driver)
    action.move_to_element_with_offset(highly_likely_bar, 0, 40).click().perform()
    action.move_by_offset(0, 50).click().perform()
    next()

    # Page 10
    next_button = driver.find_element(By.ID, "NextButton")
    action = ActionChains(driver)
    action.move_to_element_with_offset(next_button, 0, -100).click().send_keys(
        "My experience was okay but I have had better"
    ).perform()
    next()

    # Page 11
    driver.find_element(By.XPATH, '//*[@id="textR000031.1"]').click()
    next()

    # Page 12
    driver.find_element(By.XPATH, '//*[@id="textR000032.2"]').click()
    next()

    # Page 13
    driver.find_element(By.XPATH, '//*[@id="textR000034.8"]').click()
    next()

    # Page 14
    try:
        driver.find_element(By.XPATH, '//*[@id="textR000218.2"]').click()
        next()
    except:
        pass
    try:
        strongly_agree = driver.find_element(By.ID, "AgreeDESC5")
        action = ActionChains(driver)
        action.move_to_element_with_offset(strongly_agree, 0, 40).click().perform()
        # 200 pixels from bottom button to top,   110 between bar and center bubble
        for i in range(3):
            action.move_by_offset(0, 50).click().perform()
        next()
    except:
        pass

    # Page 15
    try:
        driver.find_element(By.XPATH, '//*[@id="textR000218.2"]').click()
        next()
    except:
        pass
    try:
        select = Select(
            driver.find_element(By.XPATH, '//*[@id="R000037"]')
        ).select_by_value("2")
        try:
            select = Select(
                driver.find_element(By.XPATH, '//*[@id="R000036"]')
            ).select_by_value("2")
            select = Select(
                driver.find_element(By.XPATH, '//*[@id="R000038"]')
            ).select_by_value("2")
            next()
        except:
            pass
        next()
    except:
        pass

    # Page 16
    try:
        driver.find_element(By.XPATH, '//*[@id="textR000218.2"]').click()
        next()
    except:
        pass
    try:
        select = Select(
            driver.find_element(By.XPATH, '//*[@id="R000037"]')
        ).select_by_value("2")
        try:
            select = Select(
                driver.find_element(By.XPATH, '//*[@id="R000036"]')
            ).select_by_value("2")
            select = Select(
                driver.find_element(By.XPATH, '//*[@id="R000038"]')
            ).select_by_value("2")
            next()
        except:
            pass
        next()
    except:
        pass

    # Page 17
    val_code = driver.find_element(By.CLASS_NAME, "ValCode")
    return val_code.text

if __name__ == "__main__":
    codes = []
    num = int(input("How many of these bitches you want?????????????????? "))
    for i in range(num):
        codes.append(get_dat_code())
        
    print(codes)
