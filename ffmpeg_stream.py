import subprocess
import os

def start_stream():
    input_file = "sample.mp4"
    
    if not os.path.exists(input_file):
        print("⚠️ File sample.mp4 chưa tồn tại. Vui lòng thêm file vào thư mục gốc.")
        return

    stream_url = "rtmp://a.rtmp.youtube.com/live2/h00q-wcg0-h5ku-j4w5-8b89"  # 🔁 Thay bằng stream key thật!

    command = [
        "ffmpeg",
        "-re", "-i", input_file,
        "-c:v", "libx264", "-preset", "veryfast",
        "-c:a", "aac", "-b:a", "128k",
        "-f", "flv", stream_url
    ]

    try:
        subprocess.Popen(command)
        print("✅ Livestream đang được phát...")
    except Exception as e:
        print("❌ Lỗi khi chạy FFmpeg:", e)
