# fcu_course

<img src="https://github.com/qwe8496516/fcu_course/assets/92380307/9af13356-e37c-445d-bba7-73afb0713659" width="350px">

> 此系統是一種用於自動搶課的程序，旨在幫助學生在選課系統開放時盡選到所需的課程。


## 功能

設置學號及密碼 **（請自行斟酌使用，建議設置好後使用「移除查看功能」避免有心人盜取學號密碼）**

```bash
學號： D08156152
密碼： 123456789
```

設置課程代碼 **（順序即為志願序，輸入格式為四位「數字」，請自行至課程檢索系統確認課程是否存在）**

```bash
課程1 : 0001
課程2 : 0002
課程3 : 0003
課程4 : 0004
課程5 : 0005
課程6 : 0006
```

設置點擊頻率 **（分別輸入分鐘/秒/毫秒，空格欄內不得為空或負數）**

```bash
mins : 0
sec : 3
millisec : 0
```

- [O] 自動登入
- [O] 課程代碼設定
- [O] 設置平均點擊速度

> 如有任何問題請先點選 Help 查看

## 安裝

> 點擊上方的「<> Code」選項 -> 並點選 Download ZIP 以便下載完整檔案

以下將會引導你如何安裝此專案到你的電腦上。

Chromedriver 版本建議為：與您的瀏覽器相同版本
至 Chrome 設定 -> 關於Chrome 即可看到版本資訊
假設您的版本為114.0.5735.110 ，則請至下方連結下載114版本

```
https://chromedriver.chromium.org/downloads
```
> chromedriver.exe下載完成後將其放置於 / fcu_course-main / dist / fcu / chromedriver.exe 路徑底下

<br>

到資料夾fcu_course-main底下的dist路徑底下點擊 fcu.exe 即可使用
```bash
> fcu_course-main > dist > fcu > fcu.exe 
```

## 資料夾說明

- data - 所需資料放置處 (學號密碼 / 課程代號 / 功能說明)
- image - 驗證碼放置處
- dist - 打包好的執行檔和套件
- funtion.py - 搶課功能
- 逢甲大學搶課系統.py - GUI介面


## 專案技術

- Python v3.9.6
- ddddocr
- tkinter   
- selenium

### 環境需求

- chromedriver


## 聯絡作者

可以透過以下方式與我聯絡以提供改善功能

- [Github](https://github.com/qwe8496516/)
- [Instagram](https://www.instagram.com/gannagui__2001/)
...
