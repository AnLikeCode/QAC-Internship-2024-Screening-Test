FROM python:3.12.3-slim

WORKDIR /app

# Sao chép file requirements.txt từ Host vào thư mục /app trong container
COPY requirements.txt requirements.txt

# Tiến hành cài đặt các thứ cần thiết được liệt kê trong requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép tất cả mọi thứ trong thư mục hiện tại của Host vào thư mục /app trong container.
COPY . .

# Thiết lập biến môi trường FLASK_APP trong container.
ENV FLASK_APP=random_app.py

# Sử dụng port 8080 trên Container
EXPOSE 8080

# Khi khởi động Container, flask chạy trên port 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]


        # Hướng dẫn tạo Image và Chạy Container

            # Build Image: docker build -t <tên_image> .

            # Chạy Container: docker run -p 8080:8080 -e FLASK_ENV=development <tên_image>

        # Giải thích: 

            # "-p 8080:8080": ánh xạ port 8080 của container với port 8080 trên máy chủ.
            # "-e FLASK_ENV=development": thiết lập biến môi trường cho container.





