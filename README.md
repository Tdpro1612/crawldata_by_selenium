## Crawldata_by_selenium(in window 10)

#### Ý tưởng
- tìm kiếm trang web cần lấy thông tin,yêu cầu http không đổi
- khởi tạo các bước và lấy thông tin
- lưu thông tin và xử lý
#### Thực hành với ví dụ crawl kết quả 20 năm sổ xố miền bắc? xem tỷ lệ soi cầu 2 số cuối có chính xác không?
- tra tìm trang web kết quả sổ xố có rất nhiều nhưng ta lựa chọn trang https://www.thantai.net/so-ket-qua vì url không đổi chỉ đổi thông tin trong trang
- thư viện sử dụng selenium để crawl
- lưu file dạng csv và sử dụng google colab để show kết quả xem dự đoán chính xác không?

### Bắt đầu nào

* đầu tiên cài đặt visual studio code for window
* cài đặt anaconda
* vào trình soạn thảo visual studio code 
* tạo file crawldatasx.py với nội dung như sau


```
    from selenium import webdriver  # để lựa chọn trình duyệt ,ở đây xài chrome
    from time import sleep, time  # để cho web dừng lại 1 xíu khi bạn load
    from selenium.webdriver.common.keys import Keys  # để sử dụng 1 số key như enter,hay đưa số trực tiếp vào ô trống
    import pandas as pd  # để lưu dữ liệu về dạng csv
    from datetime import datetime,timedelta  #  để tạo hàm ngày tháng
    
    browser = webdriver.Chrome('C:/Users/TD/new_data/chromedriver') # khai báo biến truy cập vào chrome ở đây cần lưu ý chrome phải xem phiên bản nào thì lên google search phiên bản drive cho phù hợp ở đây là phiên bản chrome 92
    
    URL = "https://www.thantai.net/so-ket-qua" # có thể sử dụng trang khác để lấy thông tin


    browser.get(URL)

    current_day = datetime(2021,8,14)
    data = []
    i = 0
    while i < 20*365:
        
        end = browser.find_element_by_id("end")  # id của ngày cần điền bắt đầu lui lại 
        end.clear()
        end.send_keys("{}-{}-{}".format(current_day.day,current_day.month,current_day.year))
```
![day](https://user-images.githubusercontent.com/61773507/129463765-3d1ac59b-a92a-408a-a1c7-f7c6e6aed714.jpg)
```
        button = browser.find_element_by_xpath("/html/body/div[2]/main/div/form/div[2]/div/button[9]") # lấy full x path của nút 300 lượt rồi click để hiển thị kết quả của 300 kì liên tiếp
        button.click()
```

![300l](https://user-images.githubusercontent.com/61773507/129463972-fc8ce20c-e622-472c-b5bd-7829ed8e39ec.jpg)


```

        KQ = browser.find_elements_by_class_name("font-weight-bold.text-danger.col-12.d-block.p-1.m-0")   # lấy tất cả kết quả giải đặt biệt bằng class lưu ý elements không phải element vì lấy hết chứ không phải lấy 1 kết quả
```
![kqdb](https://user-images.githubusercontent.com/61773507/129463936-cbd6a45e-c056-470a-a1fd-514c18d8f883.jpg)

```
        for j in KQ:
            print(j.text)
            data.append(j.text)
            i += 1
        current_day -= timedelta(days= 300)

    df = pd.DataFrame(data,columns = ['KQ'])
    df.to_csv("SXMB.csv", index = False)

    browser.close()
```

* đã có file SXMB.csv chúng ta mở google colab để xem xét dự đoán nhé

![test](https://user-images.githubusercontent.com/61773507/129464449-eac324f2-57ff-4099-a395-42e224366f58.jpg)

qua bảng ta kết luận số lượng chẵn lẻ là tương đương nhé nên không bắt chẵn lẻ được

![test](https://user-images.githubusercontent.com/61773507/129464490-c9a1ab69-6b89-454b-859f-d5341b46d9be.jpg)

việc phân bố xác suất ở đây có sự chênh lệch nhất định

![test](https://user-images.githubusercontent.com/61773507/129464550-525cad73-baf7-464d-badf-d8872c37cf76.jpg)

nhưng khi đưa về các khoảng = 10 ta có thể thấy xác suất xấp xỉ nhau 
Vì lẽ đó,qua 2 bảng này ta có thể kết luận việc soi cầu là không tồn tại
