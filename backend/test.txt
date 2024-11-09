# Sử dụng Python image
FROM python:3.12-slim

# Cài đặt các thư viện cần thiết cho PostgreSQL và các thư viện bổ trợ
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Tạo thư mục app trong container
WORKDIR /app

# Copy các file vào container
COPY . /app

# Cài đặt các thư viện yêu cầu từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose cổng mà Flask sẽ chạy (giả sử là 5000)
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "app.py"]
