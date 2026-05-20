""" 
Đề xuất 2 giải pháp 💡
 - Giải pháp 1 — while True
    - Lặp vô hạn
        Nếu nhập đúng → break
    - Ưu điểm
        Code ngắn
        Linh hoạt
    - Nhược điểm
        Người mới học hơi khó hiểu
        
Giải pháp 2 — while với điều kiện
    Chạy khi dữ liệu còn sai
    - Ưu điểm
        Dễ đọc
        Gần ngôn ngữ tự nhiên
    - Nhược điểm
        Phải khởi tạo biến trước
        
em chọn giải pháp 2 dễ hiểu và giống logic code cắc ngôn ngữ cũ đã đc học

"""

count = 0

while count <= 0:
    count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này:  "))
    
    if count <= 0 :
        
        print ("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.")
    
print (f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản "
       f"cho {count} nhân sự mới!")