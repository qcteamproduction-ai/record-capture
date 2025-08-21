import cv2
import os

# Cetak direktori kerja saat ini
print("Direktori kerja saat ini:", os.getcwd())

# Pastikan direktori output ada
output_path = "D:\\output.avi"
output_dir = os.path.dirname(output_path)
if not os.path.exists(output_dir):
    print(f"Direktori {output_dir} tidak ada!")
    exit()

# Buka webcam (0 = webcam default)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Periksa apakah webcam berhasil dibuka
if not cap.isOpened():
    print("Error: Tidak dapat membuka webcam. Pastikan webcam terhubung dan indeks benar.")
    exit()

# Tentukan resolusi (opsional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 20)

# Verifikasi resolusi
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Resolusi webcam: {width}x{height}")

# Tentukan format penyimpanan video ke AVI dengan codec XVID
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

# Periksa apakah VideoWriter berhasil dibuka
if not out.isOpened():
    print("Error: Tidak dapat membuat file video. Periksa codec XVID atau izin penulisan.")
    cap.release()
    exit()

frame_count = 0
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Gagal membaca frame dari webcam.")
            break

        # Simpan frame ke file video
        out.write(frame)
        frame_count += 1
        print(f"Frame {frame_count} ditulis ke video.")

        # Tampilkan hasil di jendela
        cv2.imshow('Webcam', frame)

        # Tekan 'q' untuk berhenti
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program dihentikan dengan Ctrl+C, menyimpan video...")

finally:
    # Bersihkan resource
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    if os.path.exists(output_path):
        print(f"Video telah disimpan sebagai '{output_path}'")
        print(f"Ukuran file: {os.path.getsize(output_path)} bytes")
    else:
        print(f"File '{output_path}' tidak ditemukan!")
