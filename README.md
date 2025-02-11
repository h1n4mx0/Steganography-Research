# Steganography Research
>Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. The word steganography comes from Greek steganographia, which combines the words steganós, meaning “covered or concealed”, and -graphia meaning “writing”.




## 1. Các phương pháp ẩn tin
- **Least Significant Bit (LSB) Steganography**

    **How LSB works**  

    Để hiểu cách LSB hoạt động thì đầu tiên ta cần hiểu cách pixel hoạt động. Như đã biết thì pixel được định nghĩa là một điểm ảnh cấu tạo nên bởi 3 kênh màu RGB

    |     | R | G | B |
    | --- |:-:|:-:|:-:|
    |Black|0|0|0|
    |Red  |255|0|0|
    |Green|0|255|0|
    |Blue |0|0|255|
    |White|255|255|255|
    
    Từ 3 kênh màu này có thể tạo ra bất kì màu nào chúng ta muốn. 
    
    **Binary**
    
    Mỗi kênh màu của một pixel cần 1 byte = 8 bits để lưu trữ. Ví dụ cho một pixel màu xanh:
    
    |     | R | G | B |
    | --- |:-:|:-:|:-:|
    |Decimal|0|0|255|
    |Binary |00000000|00000000|11111111|
    
    Vậy điều gì sẽ xảy ra nếu ra thay đổi bit cuối cùng của byte từ 255 -> 254
    
    |     | R | G | B |
    | --- |:-:|:-:|:-:|
    |Decimal|0|0|254|
    |Binary |00000000|00000000|11111110|
    
    Bây giờ hãy kiểm tra màu sắc của 2 pixel này:
    
    ![](/img/image1.png)
    
    Màu sắc của 2 pixel này khá giống nhau, ngay cả khi đặt cạnh nhau mắt thường cũng không nhận ra được.
    
    ![](/img/image2.png)

    Vì thế chúng ta có thể lưu 3 bits trên mỗi pixel và không làm màu sắc của ảnh mới thay đổi so với ảnh cũ.

    **ASCII Table**

    Để che giấu tin nhắn, đầu tiên ta cần lấy giá trị decimal tương ứng của kí tự từ bảng ASCII. Xem ví dụ dưới đây:

    > Giá trị dec của "a" trong bảng ASCII là 97, chuyển sang binary là 01100001. Để giấu kí tự "a" vào trong ảnh, ta cần lưu trữ đủ 8 bits của nó. Theo phương pháp LSB mỗi pixel có thể lưu trữ được 3 bits, chính vì thế ta cần ít nhất 3 pixels để lưu trữ 1 kí tự. Đầu tiên, ta lưu các bits 0 1 1 vào pixel đầu tiên, 0 0 0 và pixel tiếp theo, và 0 1 vào pixel thứ 3. Và ngược lại, khi lấy 8 bits cuối cùng của 3 pixels đầu tiên và chuyển lại theo bảng ASCII ta sẽ được kí tự "a".
    
    **Mở rộng**
    
    Trên thực tế, không nhất thiết phải lưu trữ ở các pixel liên tục, bản chất là bit thứ 8 của mỗi kênh màu trong 1 pixel là không quan trọng. Vì thế ta có thể sử dụng một khóa để generate ra các bộ pixel để lưu trữ, điều này giúp cho bản tin được bảo mật hơn.
    
    **Resources**
    
    [LSB Steganography — Hiding a message in the pixels of an image](https://medium.com/@renantkn/lsb-steganography-hiding-a-message-in-the-pixels-of-an-image-4722a8567046).
    
    [Source code](https://github.com/h1n4mx0/Steganography-Research/tree/main/LSB).

- **DCT (Discrete Cosine Transform) Steganography**
- **DWT (Discrete Wavelet Transform) Steganography**
- **Spread Spectrum Steganography**
- **Transform Domain Steganography**
- **Masking and Filtering Steganography**
- **Deep Learning-based Steganography**

## 2. Các loại dữ liệu được ẩn tin
- **Image Steganography** (ẩn tin trong ảnh)
- **Audio Steganography** (ẩn tin trong âm thanh)
- **Video Steganography** (ẩn tin trong video)
- **Text Steganography** (ẩn tin trong văn bản)
- **Network Steganography** (ẩn tin trong lưu lượng mạng)

## 3. Phát hiện và tấn công ẩn tin
- **Steganalysis** (Phân tích và phát hiện ẩn tin)
- **Chiến lược tấn công**
  - Statistical Attacks
  - Visual Attacks
  - Structural Attacks
- **Machine Learning for Steganalysis**

## 4. Ứng dụng và bảo mật
- **Sử dụng ẩn tin trong bảo vệ quyền sở hữu trí tuệ**
- **Ẩn tin trong truyền thông an toàn**
- **Mối đe dọa từ ẩn tin trong mã độc và tấn công mạng**
- **Ẩn tin và Blockchain**

