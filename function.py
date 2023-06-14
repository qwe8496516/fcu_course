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
def Login(browser):

    # 指定 Json 路徑並讀取帳號以及密碼
    json_file_path = "./data/account.json"

    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)

    account = json_data["std_ID"]
    password = json_data["password"]


    # 定位到驗證碼
    ocr_url = "./image/vcode.jpg"
    element = browser.find_element_by_id('ctl00_Login1_Image1')
    element.screenshot(ocr_url)
    res = Ocr(ocr_url)


    # 輸入帳號、密碼及驗證碼
    browser.find_element_by_id('ctl00_Login1_UserName').send_keys(account)
    browser.find_element_by_id('ctl00_Login1_Password').send_keys(password)
    browser.find_element_by_id('ctl00_Login1_vcode').send_keys(res)
    browser.find_element_by_id('ctl00_Login1_LoginButton').click()


# 透過 webdriver 開啟瀏覽器
def Browser():
    browser = webdriver.Chrome()
    browser.get('https://course.fcu.edu.tw/')
    browser.maximize_window()
    Login(browser)


# 更新 Json 檔案中的學號、密碼
def update_account_data(new_account,new_password):
    with open("./data/account.json", 'r+') as file:
        data = json.load(file)

        # 更新 JSON 檔案中的帳號和密碼
        data["std_ID"] = new_account
        data["password"] = new_password

        # 將更新後的資料寫回 JSON 檔案
        file.seek(0)  # 移動回檔案開頭
        json.dump(data, file, indent=4)
        file.truncate()  # 截斷檔案，移除舊資料


# 確認 Json 檔案中的學號、密碼
def get_account():
    with open("./data/account.json", 'r') as file:
        data = json.load(file)
        return data["std_ID"],data["password"]
