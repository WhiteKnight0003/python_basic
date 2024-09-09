class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class EmailMixin:
    def send_email(self, message):
        print(f"Sending email: {message}")

class User:
    def _init_(self, name):
        self.name = name

class AdminUser(User, LoggerMixin, EmailMixin):
    def _init_(self, name):
        super()._init_(name)
    
    def perform_admin_task(self):
        string = "Admin task"
        self.log(string+ " started")
        self.send_email(string + " completed")

admin = AdminUser()
admin.perform_admin_task()

''' giải thích
- LoggerMixin và EmailMixin là các Mixin, cung cấp chức năng ghi log và gửi email
- AdminUser kế thừa từ User và sử dụng cả hai Mixin
- AdminUser có thể sử dụng các phương thức từ cả hai Mixin mà không cần định nghĩa lại
'''

''' Ưu điểm của Mixin
- Tính mô-đun: Cho phép thêm chức năng mà không cần thay đổi cấu trúc kế thừa chính.
- Tái sử dụng code: Chức năng có thể được chia sẻ giữa nhiều lớp không liên quan.
- Tránh kế thừa đa cấp sâu: Giúp giảm độ phức tạp của cây kế thừa
'''


''' Lưu ý khi sử dụng Mixin
- Thứ tự kế thừa quan trọng: Python sử dụng MRO (Method Resolution Order) để xác định phương thức nào được gọi.
- Tránh xung đột tên: Cẩn thận với việc đặt tên phương thức trong Mixin để tránh ghi đè không mong muốn.
- Thiết kế Mixin đơn giản và tập trung: Mỗi Mixin nên cung cấp một chức năng cụ thể
'''