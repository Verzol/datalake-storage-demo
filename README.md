# datalake-storage-demo

Demo sử dụng MinIO làm Data Lake Storage và DuckDB để query dữ liệu.

## 1. Chuẩn bị môi trường

### 1.1. Cài đặt Minikube và Helm

```powershell
# Cài đặt Minikube
winget install Kubernetes.minikube

# Cài đặt Helm
winget install Helm.Helm

# Kiểm tra phiên bản
minikube version
helm version
```

### 1.2. Khởi động Minikube

```powershell
minikube start
```

### 1.3. Cài đặt MinIO bằng Helm

```powershell
# Thêm MinIO Helm repository
helm repo add minio https://charts.min.io/
helm repo update

# Cài đặt MinIO
helm install my-datalake minio/minio --set mode=standalone --set replicas=1 --set rootUser=admin --set rootPassword=password123 --set persistence.enabled=false --set resources.requests.memory=512Mi
```

### 1.4. Kiểm tra trạng thái

```powershell
# Kiểm tra pods đang chạy
kubectl get pods

# Kết quả mong đợi:
# NAME                                 READY   STATUS    RESTARTS   AGE
# my-datalake-minio-xxxxxxxxxx-xxxxx   1/1     Running   0          xxs
```

## 2. Test

- Dùng 2 tab Terminal mới và chạy song song:
```bash
kubectl port-forward svc/my-datalake-minio 9000:9000
```

```bash
kubectl port-forward svc/my-datalake-minio-console 9001:9001
```

- Truy cập `http://localhost:9001` và đăng nhập.

Tên đăng nhập: `admin`

Mật khẩu: `password123`

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/7b56827b-7e6c-4e01-9702-31ef9c5fdcdb" />

- Tạo `Bucket` mới với tên `"hoc-tap"`

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a2bbb166-8168-40dc-872a-383246149dde" />

- Upload file `"diem_so.csv"` đã chuẩn bị sẵn dạng như dưới:

```bash
mon_hoc,diem,tin_chi
Triet_hoc,8.5,3
Co_so_du_lieu,9.0,4
Mang_may_tinh,7.5,3
```

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/8d692153-5a44-44e0-bfd7-5e7eaf10adaf" />

- Chạy file `"final_score_calculator"` để kiểm tra xem đã thành công kết nối chưa:

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ae4e2c4b-2193-40b5-9a19-1d7a258c476c" />

==> Đã thành công
