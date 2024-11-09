# Sử dụng Python image
FROM python:3.12-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Cài đặt các thư viện cần thiết cho psycopg2
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy file requirements.txt vào container và cài đặt các thư viện
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Thiết lập biến môi trường cho Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Mở cổng 5000 cho ứng dụng Flask
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["flask", "run"]
