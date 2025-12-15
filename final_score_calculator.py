import duckdb

# Kết nối database ảo trong RAM
con = duckdb.connect()

# Cài đặt plugin để đọc S3 (MinIO dùng giao thức S3)
con.sql("INSTALL httpfs; LOAD httpfs;")

# Cấu hình chìa khóa để mở kho MinIO
con.sql(
    """
    SET s3_region='us-east-1';
    SET s3_endpoint='localhost:9000';
    SET s3_access_key_id='admin';
    SET s3_secret_access_key='password123';
    SET s3_use_ssl=false;
    SET s3_url_style='path';
"""
)

# Query 1: Xem tất cả dữ liệu
print("\n--- Details ---")
con.sql("SELECT * FROM 's3://hoc-tap/diem_so.csv'").show()

# Query 2: Tính điểm trung bình (Ví dụ Data Engineering)
print("\n--- Average Scores ---")
con.sql("SELECT AVG(diem) as average FROM 's3://hoc-tap/diem_so.csv'").show()
