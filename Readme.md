### Em thật sự xin lỗi Anh/Chị nhà tuyển dụng!!!
+ Dự án này là đồ án thời sinh viên của em và hồi đó em chểnh mảng học tập nên dự án còn rất sơ sài.
+ Em hy vọng được Anh/Chị nhà tuyển dụng trao cơ hội để em có thể bắt đầu lại trên con đường sự nghiệp.
+ Em cảm ơn Anh/Chị đã đọc ạ!!!

__________________________ config __________________________

## type sport:
+ 1: đối kháng: gồm 2 đội, 2 người, 2 team,...; data gồm lịch, bxh
+ 2: hỗn hợp: nhiều bên tham gia thi đấu; data gồm lịch, kết quả của các bên

## type crawl:
+ 0: không crawl, lấy luôn thông tin từ config
+ 1: request
+ 2: selenium

## type response:
+ 1: html
+ 2: json

## sourceType:
+ 0 : root
+ 1: parent

## type find result:
+ 1: list elements
+ 2: list string
+ 3: list int
+ 4: string
+ 5: int
+ 6: datetime
+ 7: timestamp
<!-- + 3: list string -->


## type find:
+ 1: find by xpath
+ 2: find by xpath + regex


## type output:
+ 1: list elements
+ 2: list string
+ 3: list int
+ 4: string
+ 5: int
+ 6: datetime: 
+ 7: true/false
+ 8: string html
+ 9: string url; kèm theo tham số domain nếu cộng thêm domain trước url


## type action:
+ 1: click
+ 2: get attributes
+ 3: scroll down
+ 4: send keys
+ 5: crawl detail
+ 6: enter

## type result:
+ 1: string
+ 2: list string
+ 3: list element

## auto add key:
+ 0: False
+ 1: True

## type replace:
+ 1: replace charactors
+ 2: replace time
__________________________ database __________________________
# type dữ liệu:
+ 1: lịch thi đấu
+ 2: kết quả
+ 3: chi tiết trận đấu: ...
+ 4: bảng xếp hạng
+ 5: môn thể thao
+ 6: giải đấu
+ 7: đối tượng thi đấu
+ 8: content thêm


# 1. lịch thi đấu:
## type_lich:
+ 1: lịch thi đấu kiểu vòng tròn đơn: ít đội, mỗi đội gặp nhau 1 lần
+ 2: lịch thi đấu kiểu vòng tròn kép: ít đội, mỗi đội gặp nhau 2 lần
+ 3: lịch thi đấu kiểu vòng tròn chia bảng: nhiều đội, chia bảng và mỗi bảng thi đấu vòng tròn bảng
+ 4: lịch thi đấu kiểu loại trực tiếp một lần thua: thua loại
+ 5: lịch thi đấu kiểu loại trực tiếp 2 lần thua: thua 2 lần loại
+ 6: lịch thi đấu kiểu hỗn hợp: giai đoạn đầu thi đấu vòng tròn, sau thi đấu loại trực tiếp
+ 7: thi đấu theo nội dung.


# 2. kết quả:
## type_ket_qua:


# 3. chi tiết trận đấu
## type:


# 4. bảng xếp hạng:
## type_bxh:
+ 1: bảng xếp hạng cho thi đấu kiểu vòng tròn: có các vòng đấu và điểm số, thông số thắng thua
+ 2: bảng xếp hạng cho thi đấu loại trực tiếp tính điểm 
+ 3: bảng xếp hạng chung cuộc: kết quả huy chương

# 5. môn thể thao:
## type_mon:
### theo địa điểm chơi:
+ 11: dưới nước
+ 12: trong nhà
+ 13: ngoài trời(trên mặt đất)
+ 14: trên trời
### theo dụng cụ chơi:
+ 21: môn thể thao đối kháng: chiến đấu trực tiếp bằng tay chân.
+ 22: môn thể thao dùng bóng: chơi với bóng
+ 23: môn thể thao dùng vợt: 
### theo cách phối hợp:
+ 31: thể thao cá nhân
+ 32: thể thao đồng đội
### theo cách chơi:
+ 41: thể thao trí tuệ
+ 42: thể thao thể lực


# 6. giải đấu


# 7. đối tượng thi đấu
## type_doi_tuong:
+ 1: vận động viên 
+ 2: câu lạc bộ/team/đội/nhóm

# __________________ INFO_________________________
thuật toán crawl tương tự như khi crawl lịch bóng đá

