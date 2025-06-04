<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<h1 align="center"><b>NHẬP MÔN THỊ GIÁC MÁY TÍNH</b></h1>

## THÀNH VIÊN NHÓM

| STT | Họ và tên                | MSSV     | Github                                                 | Email                                                   |
| --- | ------------------------ | -------- | ------------------------------------------------------ | ------------------------------------------------------- |
| 1   | Hoàng Quang Khải         | 21520952 | [khaifade (Khai Hoang)](https://github.com/khaifade)   | [21520952@gm.uit.edu.vn](mailto:21520952@gm.uit.edu.vn) |
| 2   | Hoàng Anh Đức Đăng Quang | 21522509 | [QuangHoang059](https://github.com/QuangHoang059)      | [21522509@gm.uit.edu.vn](mailto:21522509@gm.uit.edu.vn) |
| 3   | Phan Văn Thiện           | 21522628 | [Thienvp (Phan Văn Thiện)](https://github.com/imvp3) | [21522628@gm.uit.edu.vn](mailto:21522628@gm.uit.edu.vn) |

## GIỚI THIỆU MÔN HỌC

* **Tên môn học:** Nhập môn thị giác máy tính
* **Mã môn học:** CS231
* **Mã lớp:** CS231.O21
* **Năm học:** HK2 (2023 - 2024)
* **Giảng viên:** TS. Mai Tiến Dũng

## **ĐỒ ÁN CUỐI KỲ**

### Giới thiệu đề tài

* **Tên đề tài:** Nhận dạng cử chỉ tay
* **Mô tả:** Nhận dạng ba loại cử chỉ tay: "left", "right", "up" từ ảnh đầu vào chứa bàn tay người dùng.
* **Ứng dụng:** Hệ thống tương tác người - máy, điều khiển không chạm, trò chơi,...
* **File báo cáo:** [slide.pdf](docs\slide.pdf)

### Phát biểu bài toán

* **Input:** Ảnh bàn tay người đã được xén sẵn và gán nhãn (left, right, up).
* **Output:** Nhãn dự đoán tương ứng với cử chỉ tay.

### Bộ dữ liệu

* **Nguồn:** Tự thu thập từ 3 thành viên trong nhóm.
* **Số lượng:** 2550 ảnh

  * Train: 2250 ảnh
  * Test: 300 ảnh
* **Tiền xử lý:**

  * Cắt vùng bàn tay (sử dụng thư viện `cvzone`)
  * Resize ảnh về kích thước (224, 224)

### Phương pháp và mô hình sử dụng

* **Trích xuất đặc trưng:** VGG16 pre-trained trên ImageNet, lấy output sau lớp MaxPooling cuối cùng, sau đó Flatten.
* **Mô hình phân loại:**

  * **SVM:** kernel='rbf', C=100, gamma='auto'
  * **Random Forest:** n\_estimators ∈ \[100, 300], max\_features='auto'
  * **Logistic Regression:** C ∈ \[0.1, 1, 10, 100], solver ∈ \['lbfgs', 'saga']
* **Tối ưu hyperparameter:** Dùng RandomizedSearchCV

### Đánh giá mô hình

* **Metric:** Accuracy, Precision, Recall, F1-score
* **Kết quả tốt nhất:**

  | Mô hình | Accuracy | Precision | Recall | F1-score |
  | ------- | -------- | --------- | ------ | -------- |
  | SVM     | 0.98     | 0.98      | 0.98   | 0.98     |
  | RF      | 1.00     | 1.00      | 1.00   | 1.00     |
  | LR      | 0.97     | 0.97      | 0.97   | 0.97     |

## HƯỚNG DẪN CHẠY MÃ

### Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### Chạy notebook

```bash
jupyter notebook cs231-vgg-svm.ipynb
```

## TÀI LIỆU THAM KHẢO

1. Simonyan, K., & Zisserman, A. (2014). Very Deep Convolutional Networks for Large-Scale Image Recognition. *ICLR*.
2. Breiman, L. (2001). Random Forests. *Machine Learning Journal*.
3. Surowiecki, J. (2004). *The Wisdom of Crowds*.
4. Vapnik, V. (1995). *The Nature of Statistical Learning Theory*.
5. Maalouf, M. (2011). Logistic regression in data analysis: An overview. *International Journal of Data Analysis Techniques and Strategies*.
6. [cvzone GitHub](https://github.com/cvzone/cvzone)
7. [Kaggle VGG16 Dataset](https://www.kaggle.com/datasets/crawford/vgg16)
