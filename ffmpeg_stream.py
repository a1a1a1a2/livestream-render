import subprocess

def start_stream():
    stream_url = "rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY"  # 🔁 Thay bằng URL riêng
    input_file = "sample.mp4"  # 🔁 Có thể đổi thành ảnh động, camera, hoặc video URL

    command = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",
        "-i", input_file,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-maxrate", "3000k",
        "-bufsize", "6000k",
        "-pix_fmt", "yuv420p",
        "-g", "50",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        stream_url
    ]

    subprocess.Popen(command)
