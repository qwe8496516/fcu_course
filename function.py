from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import ddddocr
import json
from time import sleep


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


# 開始搶課
def rob(browser,click_interval):    
    # ------------------------------------------------------------------------------------------ 未知
    try:
        browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_Label3').click()

        while(True):
            
            # 取得課程代號列表
            Course_List = get_current_course()
            print(Course_List,len(Course_List))

            if (Course_List[0] == ""):
                print("課程代碼已清空，結束程式")
                break
            
            browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_tbSubID').send_keys(Course_List[0])
        
            try:

                # 取得課程資訊
                table_text= browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_PanelTop').text

                # 判斷是否加選
                if '退選' in table_text:
                    table_id = 'ctl00_MainContent_TabContainer1_tabSelected_gvToDel'
                else:
                    table_id = 'ctl00_MainContent_TabContainer1_tabSelected_gvToAdd'
                

                print("test" + browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').text)

                if  browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').text == "":
                    # 如果 table_id 為 Add 則點擊加選按鈕
                    if (table_id == 'ctl00_MainContent_TabContainer1_tabSelected_gvToAdd'):
                        browser.find_element_by_css_selector("#ctl00_MainContent_TabContainer1_tabSelected_gvToAdd tr:nth-child(2) td:first-child input").click()
                        if browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text == '加選成功':
                            print(browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text)
                            remove_current_course()
                        else:
                            # 超修學分數
                            if browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text[2] == '超':
                                print(browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text)
                                remove_current_course()
                            else:
                                print(browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text)
                    # 代表已加選該課程要移除課程代碼
                    else:
                        remove_current_course()
                # 上課時間與其他課程衝堂
                elif browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text == '上課時間與其他課程衝堂':
                    print(browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text)
                    remove_current_course()
                # 本科目不開放網路選課
                elif browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text == '本科目不開放網路選課':
                    print(browser.find_element_by_id('ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').find_element_by_tag_name('span').text)
                    remove_current_course()

            except:
                browser.close()
                Browser(click_interval)

            # 控制點擊時長
            sleep(click_interval)
    except:
        print('',end='')
            


# 透過 webdriver 開啟瀏覽器
def Browser(click_interval):
    browser = webdriver.Chrome()
    browser.get('https://course.fcu.edu.tw/')
    browser.maximize_window()
    Login(browser)
    print(click_interval)
    rob(browser,click_interval)


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


# 更新課程代碼
def update_courser_info(course_ID1, course_ID2, course_ID3, course_ID4, course_ID5, course_ID6):
    with open("./data/course.json", 'r+') as file:
        data = json.load(file)

        # 更新 JSON 檔案中的帳號和密碼
        data["course_ID1"] = course_ID1
        data["course_ID2"] = course_ID2
        data["course_ID3"] = course_ID3
        data["course_ID4"] = course_ID4
        data["course_ID5"] = course_ID5
        data["course_ID6"] = course_ID6

        # 將更新後的資料寫回 JSON 檔案
        file.seek(0)  # 移動回檔案開頭
        json.dump(data, file, indent=4)
        file.truncate()  # 截斷檔案，移除舊資料


# 取得目前設定的課程代碼資訊
def get_current_course():
    with open("./data/course.json", 'r') as file:
        data = json.load(file)
        course_list = [data["course_ID1"],data["course_ID2"],data["course_ID3"],data["course_ID4"],data["course_ID5"],data["course_ID6"]]
        return course_list
    


# 清除已加選的課程代碼
def remove_current_course():
    with open("./data/course.json", 'r+') as file:
        data = json.load(file)

        # 將 course_ID1 的值設為空
        data["course_ID1"] = ""

        # 依次將值往後移
        data["course_ID1"] = data["course_ID2"]
        data["course_ID2"] = data["course_ID3"]
        data["course_ID3"] = data["course_ID4"]
        data["course_ID4"] = data["course_ID5"]
        data["course_ID5"] = data["course_ID6"]

        data["course_ID6"] = ""
        # 寫入修改後的 JSON 資料到檔案
        with open("./data/course.json", 'w') as file:
            json.dump(data, file, indent=4)