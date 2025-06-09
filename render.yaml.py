services:
  - type: web
    name: livestream-bot
    env: python
    buildCommand: "apt-get update && apt-get install -y ffmpeg && pip install -r requirements.txt"
    startCommand: "python main.py"
    plan: free
    region: singapore
