import tkinter as tk
import function
from tkinter import messagebox


# 更新帳號密碼
def update_account():
    # 取得 std_ID , password
    New_Std_ID = std_ID.get()
    New_Password = password.get()
    # 如果內文不為空白則更新
    if not (len(New_Std_ID) == 0 or len(New_Password) == 0):
        function.update_account_data(New_Std_ID, New_Password)
        messagebox.showinfo('通知', '帳號密碼更新成功')
    else:
        # 清除內文
        std_ID.delete(0, tk.END)
        password.delete(0, tk.END)
        messagebox.showinfo('錯誤', '帳號或密碼不能為空')

# 確認帳號密碼
def check_account():
    std_ID, password = function.get_account()
    if(std_ID and password):
        messagebox.showinfo('帳號密碼確認', '學號 : ' + std_ID + '\n帳號 : ' + password)
    else:
        messagebox.showinfo('帳號密碼確認', '帳號密碼尚未設定')
    

# 清除帳號密碼資訊並移除查看功能
def clear_check_btn():
    result = messagebox.askquestion("確認", "是否要執行此操作？\n清除後就無法看到個人資訊")
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
        messagebox.showinfo('通知', '空格已清空')
    else:
        messagebox.showinfo('錯誤', '帳號或密碼空格為空')

# 切換密碼顯示方式
def show_password():
    global show_password
    show_password = not show_password
    if show_password:
        password.config(show = "")
    else:
        password.config(show = "*")


# 主程式
if __name__ == '__main__':

    # window 的設定
    window = tk.Tk()
    window.title('逢甲大學搶課系統')
    window.resizable(False, False)

    # 設定按鈕相同寬度
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    # 元件之間的間隔
    paddingx = 30
    paddingy = 5

    # 建立學號密碼設定
    account_label = tk.LabelFrame(window, text='帳號密碼設定', padx=15, pady=15)
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
    help_btn = tk.Button(window, text="Help ? >>", width=10, height=2, command=show_password)
    help_btn.grid(column=1, row=2, sticky="nsew", padx=(0, paddingx), pady=5)

    # 查看帳號密碼按鈕
    check_btn = tk.Button(window, text="查看目前帳號密碼", width=10, height=2, command=check_account)
    check_btn.grid(column=0, row=3, sticky="nsew", padx=(paddingx, 20), pady=5)

    # 移除查看功能
    clear_btn = tk.Button(window, text="移除查看功能", width=10, height=2, command=clear_check_btn)
    clear_btn.grid(column=1, row=3, sticky="nsew", padx=(0, paddingx), pady=5)

    # 開啟網頁並登入
    open_browser = tk.Button(window, text="開始搶課", height=2, command=function.Browser)
    open_browser.grid(column=0, row=4, sticky="nsew", columnspan=3, padx=paddingx, pady=(5, 18))

    
    # 持續執行 mainloop
    window.mainloop()
