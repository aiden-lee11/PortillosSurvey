#Failed attempt using Clicknium because it cant dynamically find the xpath of the bubbles because each time there is different prompts

from clicknium import clicknium as cc, locator
import time

# Define the locator for the XPath expression
locator.mine = "//*[starts-with(@id, 'FNSR0')]"

#code = input("Code # Input with Spaces: ")
code = "160 007 500 050 010 298 70"
user_boxes = code.split(" ") 

if code != "":
    tab = cc.edge.open("https://portillos.com/survey")
    tab.find_element(locator.smg.tellportillos.text_input_digits_1_through_3_of_the_coupon_code).set_text(user_boxes[0])
    tab.find_element(locator.smg.tellportillos.text_input_digits_4_through_6_of_the_coupon_code).set_text(user_boxes[1])
    tab.find_element(locator.smg.tellportillos.text_input_digits_7_through_9_of_the_coupon_code).set_text(user_boxes[2])
    tab.find_element(locator.smg.tellportillos.text_input_digits_10_through_12_of_the_coupon_code).set_text(user_boxes[3])
    tab.find_element(locator.smg.tellportillos.text_input_digits_13_through_15_of_the_coupon_code).set_text(user_boxes[4])
    tab.find_element(locator.smg.tellportillos.text_input_digits_16_through_18_of_the_coupon_code).set_text(user_boxes[5])
    tab.find_element(locator.smg.tellportillos.text_input_digits_19_through_20_of_the_coupon_code).set_text(user_boxes[6])
        
    time.sleep(1)
    
    tab.find_element(locator.smg.tellportillos.submit_nextbutton).click()
    time.sleep(1)
    tab.find_element(locator.smg.tellportillos.first_page).click()
    tab.find_element(locator.smg.tellportillos.submit_nextbutton1).click()
    time.sleep(1)
    tab.find_element(locator.smg.tellportillos.dine_in).click()
    tab.find_element(locator.smg.tellportillos.submit_nextbutton2).click()
    time.sleep(2)
    
    # Locate the element with a dynamic ID using XPath directly
    partial_id = "FNSR0"
    xpath = f"//*[starts-with(@id, '{partial_id}')]"

    elements = tab.find_elements(xpath)
    # Perform actions on the elements
    for element in elements:
        element.click()
        time.sleep(1)

    time.sleep(1)
    
# //*[@id="FNSR000012"]/td[3]/label
# //*[@id="FNSR000239"]/td[3]/label
# //*[@id="FNSR000237"]/td[3]/label