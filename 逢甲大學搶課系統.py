import tkinter as tk
import function
import numpy as np
import json
from tkinter import messagebox

# 用 pyinstaller 打包的時候要複製 ddddocr 套件到 dist 的資料夾下面

# 更新帳號密碼
def update_account():
    # 取得 std_ID , password
    New_Std_ID = std_ID.get()
    New_Password = password.get()
    # 如果內文不為空白則更新
    if not (len(New_Std_ID) == 0 or len(New_Password) == 0):
        function.update_account_data(New_Std_ID, New_Password)
        messagebox.showinfo('通知', '帳號密碼更新成功',parent=window)
    else:
        # 清除內文
        std_ID.delete(0, tk.END)
        password.delete(0, tk.END)
        messagebox.showwarning('錯誤', '帳號或密碼不能為空',parent=window)

# 確認帳號密碼
def check_account():
    std_ID, password = function.get_account()
    if(std_ID and password):
        messagebox.showinfo('帳號密碼確認', '學號 : ' + std_ID + '\n帳號 : ' + password,parent=window)
    else:
        messagebox.showwarning('帳號密碼確認', '帳號密碼尚未設定',parent=window)
    
# 清除帳號密碼資訊並移除查看功能
def clear_check_btn():
    result = messagebox.askquestion("確認", "是否要執行此操作？\n清除後就無法看到個人資訊",parent=window)
    if result == 'yes':
        # 移除查看功能
        check_btn.destroy()
        clear_btn.destroy()
        print("查看個人資訊功能已移除")
    else:
        # 取消操作的處理
        print("取消操作")

# 清除內文
def clear_input_field():
    New_Std_ID = std_ID.get()
    New_Password = password.get()
    # 如果內文其中一個不為空則清除
    if not (len(New_Std_ID) == 0 and len(New_Password) == 0):
        std_ID.delete(0, tk.END)
        password.delete(0, tk.END)
        messagebox.showinfo('通知', '空格已清空',parent=window)
    else:
        messagebox.showwarning('錯誤', '帳號或密碼空格為空',parent=window)

# 切換密碼顯示方式
def show_password():
    global show_password
    show_password = not show_password
    if show_password:
        password.config(show = "")
    else:
        password.config(show = "*")

# 更新欲搶課程代碼
def update_course():
    # 取得課程代碼
    Course = [course1.get(), course2.get(), course3.get(), course4.get()]
    if(not (len(Course[0])) and not (len(Course[1])) and not (len(Course[2])) and not (len(Course[3]))):
        messagebox.showwarning('錯誤', '四個欄位不能皆為空格',parent=window)
    else:
        # 檢查陣列元素是否有空白，若有空白則將後面的元素往前移
        for j in range(2):
            for i in range(len(Course) - 1):
                if len(Course[i]) == 0:
                    Course[i] = Course[i+1]
                    Course[i+1] = ''
        
        # 更新 Entry 欄位的文字
        course1.delete(0, tk.END)
        course2.delete(0, tk.END)
        course3.delete(0, tk.END)
        course4.delete(0, tk.END)
        course1.insert(0, Course[0])
        course2.insert(0, Course[1])
        course3.insert(0, Course[2])
        course4.insert(0, Course[3])

        function.update_courser_info(Course[0], Course[1], Course[2], Course[3])
        messagebox.showinfo('通知', '課程送出成功',parent=window)

# 顯示目前設定課程代碼
def show_course_info():
    # 設定課程數量
    course_count = 4
    Course = function.get_current_course()
    for i in range(len(Course)):
        if(not Course[i]):
            course_count -= 1
    # 顯示課程數量
    if course_count == 0:
        messagebox.showwarning('錯誤', '目前未設定課程代碼',parent=window)
    else:
        if (course_count == 4):
            messagebox.showinfo('通知', '課程一 : {}\n課程二 : {}\n課程三 : {}\n課程四 : {}'.format(Course[0],Course[1],Course[2],Course[3]))
        elif (course_count == 3):
            messagebox.showinfo('通知', '課程一 : {}\n課程二 : {}\n課程三 : {}'.format(Course[0],Course[1],Course[2]))
        elif (course_count == 2):
            messagebox.showinfo('通知', '課程一 : {}\n課程二 : {}'.format(Course[0],Course[1]))
        elif(course_count == 1):
            messagebox.showinfo('通知', '課程一 : {}'.format(Course[0]))

# 清除課程代碼
def clear_course_info():
    course1.delete(0, tk.END)
    course2.delete(0, tk.END)
    course3.delete(0, tk.END)
    course4.delete(0, tk.END)

# 清除 Json 格式中的目標課程清單
def clear_course_list():
    result = messagebox.askquestion("清除課程", "是否要執行此操作？",parent=window)
    if result == 'yes':
        with open("./data/course.json", 'r+') as file:
            data = json.load(file)
            # 更新 JSON 檔案中的帳號和密碼
            data["course_ID1"] = ""
            data["course_ID2"] = ""
            data["course_ID3"] = ""
            data["course_ID4"] = ""

            # 將更新後的資料寫回 JSON 檔案
            file.seek(0)  # 移動回檔案開頭
            json.dump(data, file, indent=4)
            file.truncate()  # 截斷檔案，移除舊資料
        messagebox.showinfo('通知', '課程已清除',parent=window)
        print("課程已清除")
    else:
        # 取消操作的處理
        print("取消操作")

# 抓取Click的頻率
def ClickHandler():
    # 取得點擊頻率 分鐘 / 秒 / 微秒
    mins_value = int(mins.get())
    sec_value = int(sec.get())
    millsec_value = int(millsec.get())
    frequency = mins_value*60 + sec_value + 0.01*millsec_value
    # 錯誤頻率偵測
    if(frequency <= 0):
        messagebox.showwarning('錯誤', '請先設定點擊頻率',parent=window)
    else:
        function.Browser(frequency)

# 檢查課程輸入規則
def course_validate_input(text):
    # 檢查輸入長度是否超過指定值 && 只包含數字
    if (len(text) <= 4 and (text.isdigit() or text == '')):
        return True
    else:
        if(not text.isdigit()):
            messagebox.showwarning('錯誤', '課程代碼必須為數字',parent=window)
        return False
    
# 檢查點擊頻率輸入規則
def click_validate_input(text):
    # 檢查輸入數字為正數
    if (text.isdigit()):
        return True
    else:
        if(text == ''):
            messagebox.showwarning('錯誤', '時間不得為空',parent=window)
        else:
            messagebox.showwarning('錯誤', '時間必須為數字',parent=window)
        return False
    
# 顯示幫助資訊
def show_help():
    window2 = tk.Tk()
    window2.title('幫助')
    window2.resizable(False, False)
    window2.geometry('450x580+600+0')
    
    help_info = ""
    line = "------------------------------------------------------------------------"
    
    # 讀取 function.json 的功能說明
    with open('./data/function.json', 'rb') as file:
        help_data = json.load(file)
        
        for func in help_data:
            help_info += "\n" + func + "\n{}\n".format(line)
            account_data = help_data[func]
            
            for key, value in account_data.items():
                help_info += key + "-> " + value + "\n\n"
            
            help_info += "\n"

    std_ID_label = tk.Label(window2, text=help_info, anchor=tk.W, justify=tk.LEFT, wraplength=400)
    std_ID_label.pack()

    window2.mainloop()
    
    

# 主程式
if __name__ == '__main__':

    # window 的設定
    window = tk.Tk()
    window.title('逢甲大學搶課系統')
    window.resizable(False, False)
    window.geometry('+0+0')

    # 設定按鈕相同寬度
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    # 元件之間的間隔
    paddingx = 30
    paddingy = 5

    # 建立學號密碼設定
    account_label = tk.LabelFrame(window, text='學號密碼設定', padx=15, pady=15)
    account_label.grid(column=0, row=0, columnspan=3, ipadx=5, ipady=5, padx=paddingx, pady=(18, 5))

    # 學號欄位
    std_ID_label = tk.Label(account_label, text='學號 : ')
    std_ID = tk.Entry(account_label, show="")
    std_ID_label.grid(column=1, row=1, sticky="nsew")
    std_ID.grid(column=2, row=1, sticky="nsew")

    # 密碼設定
    password_label = tk.Label(account_label, text='密碼 : ')
    password = tk.Entry(account_label, show="*")
    password_label.grid(column=3, row=1, sticky="nsew")
    password.grid(column=4, row=1, sticky="nsew")

    # 清除空格內容
    submit = tk.Button(window, text="清除空格內容", width=10, height=2, command=clear_input_field)
    submit.grid(column=0, row=1, sticky="nsew", padx=(paddingx, 20), pady=5)

    # 清除相關資訊
    clear_info_btn = tk.Button(window, text="顯示密碼", width=10, height=2, command=show_password)
    clear_info_btn.grid(column=1, row=1, sticky="nsew", padx=(0, paddingx), pady=5)

    # 更新送出按鈕
    submit = tk.Button(window, text="更新帳號密碼", width=10, height=2, command=update_account)
    submit.grid(column=0, row=2, sticky="nsew", padx=(paddingx, 20), pady=5)

    # Help
    help_btn = tk.Button(window, text="Help ? >>", width=10, height=2, command=show_help)
    help_btn.grid(column=1, row=2, sticky="nsew", padx=(0, paddingx), pady=5)

    # 查看帳號密碼按鈕
    check_btn = tk.Button(window, text="查看目前帳號密碼", width=10, height=2, command=check_account)
    check_btn.grid(column=0, row=3, sticky="nsew", padx=(paddingx, 20), pady=5)

    # 移除查看功能
    clear_btn = tk.Button(window, text="移除查看功能", width=10, height=2, command=clear_check_btn)
    clear_btn.grid(column=1, row=3, sticky="nsew", padx=(0, paddingx), pady=5)



    # 建立驗證規則
    validation = window.register(course_validate_input)

    # 輸入所選課程
    course_label = tk.LabelFrame(window, text='輸入欲搶課程代碼', padx=15, pady=15)
    course_label.grid(column=0, row=4, columnspan=3, ipadx=5, ipady=5, padx=paddingx, pady=(18, 5))

    # 課程一
    course1_label = tk.Label(course_label, text='課程1 : ')
    course1 = tk.Entry(course_label, validate="key", validatecommand=(validation, '%P'), show="")
    course1_label.grid(column=1, row=1, sticky="nsew", pady=5)
    course1.grid(column=2, row=1, sticky="nsew", pady=5)

    # 課程二
    course2_label = tk.Label(course_label, text='課程2 : ')
    course2 = tk.Entry(course_label, validate="key", validatecommand=(validation, '%P'), show="")
    course2_label.grid(column=3, row=1, sticky="nsew", pady=5)
    course2.grid(column=4, row=1, sticky="nsew", pady=5)

    # 課程三
    course3_label = tk.Label(course_label, text='課程3 : ')
    course3 = tk.Entry(course_label, validate="key", validatecommand=(validation, '%P'), show="")
    course3_label.grid(column=1, row=2, sticky="nsew", pady=5)
    course3.grid(column=2, row=2, sticky="nsew", pady=5)

    # 課程四
    course4_label = tk.Label(course_label, text='課程4 : ')
    course4 = tk.Entry(course_label, validate="key", validatecommand=(validation, '%P'), show="")
    course4_label.grid(column=3, row=2, sticky="nsew", pady=5)
    course4.grid(column=4, row=2, sticky="nsew", pady=5)

    # 清除空格代碼
    clear_course_info = tk.Button(window, text="清除空格代碼", width=10, height=2, command=clear_course_info)
    clear_course_info.grid(column=0, row=5, sticky="nsew", padx=(paddingx, 20), pady=5)

    # 清除已設定課程代碼
    clear_course_list = tk.Button(window, text="清除已設定課程代碼", width=10, height=2, command=clear_course_list)
    clear_course_list.grid(column=1, row=5, sticky="nsew", padx=(0, paddingx), pady=5)

    # 送出課程代碼
    submit_course = tk.Button(window, text="送出課程代碼", width=10, height=2, command=update_course)
    submit_course.grid(column=0, row=6, sticky="nsew", padx=(paddingx, 20), pady=5)

    # 顯示已設定課程代碼
    show_course_info = tk.Button(window, text="顯示已設定課程代碼", width=10, height=2, command=show_course_info)
    show_course_info.grid(column=1, row=6, sticky="nsew", padx=(0, paddingx), pady=5)


    # 建立驗證規則
    validation2 = window.register(click_validate_input)

    # 調整點擊速度
    ClickInterval = tk.LabelFrame(window, text='Click Interval', padx=15, pady=15)
    ClickInterval.grid(column=0, row=7, columnspan=3, ipadx=5, ipady=5, padx=paddingx, pady=(18, 5))

    # 分鐘
    mins = tk.Entry(ClickInterval,width=10, validate="key", validatecommand=(validation2, '%P'), show="")
    mins_label = tk.Label(ClickInterval, text='mins')
    mins.insert(0, "0")
    mins.grid(column=1, row=1, sticky="nsew")
    mins_label.grid(column=2, row=1, sticky="nsew",padx=10)
    
    # 秒
    sec = tk.Entry(ClickInterval,width=10, validate="key", validatecommand=(validation2, '%P'), show="")
    sec_label = tk.Label(ClickInterval, text='sec')
    sec.insert(0, "3")
    sec.grid(column=3, row=1, sticky="nsew")
    sec_label.grid(column=4, row=1, sticky="nsew",padx=10)

    # 微秒
    millsec = tk.Entry(ClickInterval,width=10, validate="key", validatecommand=(validation2, '%P'), show="")
    millsec_label = tk.Label(ClickInterval, text='millisec')
    millsec.insert(0, "0")
    millsec.grid(column=5, row=1, sticky="nsew")
    millsec_label.grid(column=6, row=1, sticky="nsew",padx=10)

    # 開始搶課
    open_browser = tk.Button(window, text="開始搶課", height=2, command=ClickHandler)
    open_browser.grid(column=0, row=8, sticky="nsew", columnspan=3, padx=paddingx, pady=(5, 18))

    # 持續執行 mainloop
    window.mainloop()
