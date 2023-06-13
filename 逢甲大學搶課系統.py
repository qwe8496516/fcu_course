from selenium import webdriver
import logging
import ddddocr
import json


# 透過 ddddocr 解析驗證碼
def Ocr(file_name):
    # 消除日誌
    logging.getLogger().setLevel(logging.ERROR)

    ocr = ddddocr.DdddOcr()

    with open(file_name, 'rb') as f:
        image_bytes = f.read()

    return ocr.classification(image_bytes)
    

# 登入目標網頁
def Login():

    # 指定 Json 路徑並讀取帳號以及密碼
    json_file_path = "account.json"

    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)

    account = json_data["account"]
    password = json_data["password"]


    # 定位到驗證碼
    ocr_url = "vcode.jpg"
    element = browser.find_element_by_id('ctl00_Login1_Image1')
    element.screenshot(ocr_url)
    res = Ocr(ocr_url)


    # 輸入帳號、密碼及驗證碼
    browser.find_element_by_id('ctl00_Login1_UserName').send_keys(account)
    browser.find_element_by_id('ctl00_Login1_Password').send_keys(password)
    browser.find_element_by_id('ctl00_Login1_vcode').send_keys(res)
    browser.find_element_by_id('ctl00_Login1_LoginButton').click()




if __name__ == '__main__':
    # 建立 Web driver 開啟網頁
    browser = webdriver.Chrome()
    browser.get('https://course.fcu.edu.tw/')
    browser.maximize_window()
    Login()





