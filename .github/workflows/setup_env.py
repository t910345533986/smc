import os
import subprocess
import sys

def install_dependencies():
    print("正在安裝必要的 Python 套件...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 套件安裝成功！")
    except Exception as e:
        print(f"❌ 安裝失敗: {e}")

def create_env_file():
    env_content = 'DISCORD_WEBHOOK_URL="在這裡貼上你的網址"\n'
    if not os.path.exists(".env"):
        with open(".env", "w", encoding="utf-8") as f:
            f.write(env_content)
        print("✅ 已建立 .env 範本檔，請記得去修改裡面的 Webhook 網址。")
    else:
        print("ℹ️ .env 檔案已存在，跳過建立。")

if __name__ == "__main__":
    install_dependencies()
    create_env_file()
