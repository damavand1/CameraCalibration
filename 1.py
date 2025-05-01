import cv2
import os

# پوشه‌ای برای ذخیره تصاویر
# save_dir = "calib_images"
# os.makedirs(save_dir, exist_ok=True)

try:
    save_dir = "calib_images"
    os.makedirs(save_dir, exist_ok=True)
    print(f"✅ پوشه ساخته شد یا از قبل وجود داشت: {os.path.abspath(save_dir)}")
except Exception as e:
    print(f"❌ خطا در ساخت پوشه: {e}")


# عدد 0 یعنی اولین دوربین USB سیستم
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ دوربین پیدا نشد یا باز نشد!")
    exit()

print("✅ دوربین آماده است. کلید SPACE را برای ذخیره عکس بزن. ESC برای خروج.")

img_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ فریم دریافت نشد!")
        break

    cv2.imshow('Camera View', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # کلید ESC
        break
    elif key == 32:  # کلید SPACE
        filename = os.path.join(save_dir, f"image_{img_count:03}.jpg")
        cv2.imwrite(filename, frame)
        print(f"💾 ذخیره شد: {filename}")
        img_count += 1

cap.release()
cv2.destroyAllWindows()
