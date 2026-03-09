import datetime
import os

def main():
    now = datetime.datetime.utcnow()
    # 環境変数 EXAMPLE_NAME を読んでみる（なければ "World"）
    name = os.environ.get("EXAMPLE_NAME", "World")
    print(f"[{now}] Hello, {name}! Render Cron Job is running.")

if __name__ == "__main__":
    main()
