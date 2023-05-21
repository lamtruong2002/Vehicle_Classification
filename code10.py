import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np

# Load mô hình từ file .h5
model = tf.keras.models.load_model('model.h5')

# Load tên lớp nhãn
class_names = ['XE CỨU THƯƠNG','XE ĐẠP','XE BUÝT','XE Ô TÔ','XE MÁY','XE TẢI']  
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Mở ảnh
        image = Image.open(file_path)
        # Chuyển kích thước ảnh về 40x30
        resized_image = image.resize((40, 30))
        # Chuyển đổi ảnh thành mảng numpy
        image_array = np.array(resized_image) / 255.0  # Chuẩn hóa giá trị pixel trong khoảng từ 0 đến 1
        image_array = np.expand_dims(image_array, axis=0)  # Mở rộng chiều cho batch (1 ảnh)
        # Dự đoán lớp nhãn
        predictions = model.predict(image_array)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_class_index]
        
        # Hiển thị ảnh và kết quả dự đoán
        #image_large = image.resize((400, 300))  # Thu nhỏ ảnh gốc để hiển thị lớn hơn
        image_zoomed = resized_image.resize((400, 300), resample=Image.NEAREST)  # Phóng to ảnh gốc để hiển thị rõ từng pixel
        image_tk = ImageTk.PhotoImage(image_zoomed)
        image40x30.config(image=image_tk)
        image40x30.image = image_tk

        resized_image1 = image.resize((400, 300))
        image_tk1 = ImageTk.PhotoImage(resized_image1)
        imagegoc.config(image=image_tk1)
        imagegoc.image = image_tk1

        result_label.config(text=f'PHÂN LOẠI: {predicted_class}', font=('Arial', 20, 'bold'))  # Điều chỉnh kích thước và kiểu chữ
        

# Tạo cửa sổ
window = tk.Tk()
# Đặt tên cho cửa sổ
window.title("PHÂN LOẠI PHƯƠNG TIỆN GIAO THÔNG")
# Điều chỉnh kích thước cửa sổ
window.geometry("800x600")  
window.configure(bg="lightblue")
# Tạo nút "Open" để chọn ảnh
open_button = tk.Button(window, text="Thêm hình ảnh",font=('Arial', 12, 'bold'),bg='green', command=open_image, width=15, height=2)  
open_button.place(x=330, y=150)

# Tạo nhãn để hiển thị ảnh
image40x30 = tk.Label(window)
image40x30.place(x=0, y=230)
imagegoc = tk.Label(window)
imagegoc.place(x=400, y=230)

# Tạo nhãn để hiển thị kết quả dự đoán
result_label = tk.Label(window)
result_label.place(x=250, y=550)

# Tạo label 1
label1 = tk.Label(window, text="TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT TPHCM")
label1.config(font=("Arial", 12,"bold"))
label1.place(x=210, y=30)

# Tạo label 2
label2 = tk.Label(window, text="MÔN HỌC: TRÍ TUỆ NHÂN TẠO")
label2.config(font=("Arial", 12))
label2.place(x=300, y=60)

# Tạo label 3
label1 = tk.Label(window, text="HỌ VÀ TÊN: NGUYỄN LAM TRƯỜNG  MSSV:20146189")
label1.config(font=("Arial", 11))
label1.place(x=220, y=90)

# Tạo label 4
label1 = tk.Label(window, text="CHỦ ĐỀ: PHÂN LOẠI PHƯƠNG TIỆN GIAO THÔNG")
label1.config(font=("Arial", 11))
label1.place(x=230, y=120)



# hiển thị logo Trường
image1 = Image.open("logotruong.jpg")
image1 = image1.resize((200, 200))  # Thiết lập kích thước hình ảnh
photo1 = ImageTk.PhotoImage(image1)
image_label1 = tk.Label(window, image=photo1)
image_label1.place(x=0, y=0)

#Hiển thị logo khoa
image2 = Image.open("logokhoa.jpg")
image2 = image2.resize((200, 200))  # Thiết lập kích thước hình ảnh
photo2 = ImageTk.PhotoImage(image2)
image_label2 = tk.Label(window, image=photo2)
image_label2.place(x=600, y=0)


# Chạy vòng lặp chính của ứng dụng giao diện
window.mainloop()
