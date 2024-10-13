import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import time
import os

# 设置邮件发送者和接收者
sender_email = ''
receiver_email = ''
subject = '寝室电量警告！！！'

# 邮件正文内容
body = '剩余电量不足20度，请尽快充值！'

# SMTP 服务器登录信息
smtp_server = 'smtp.163.com'#以163邮箱为例
smtp_port = 465
smtp_password = ''  #授权码

# CSV 文件路径
csv_file_path = 'balance_data.csv'

# 检查balance_data.csv的最后一行balance值
def get_last_balance(csv_file):
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            if len(rows) > 1:  # 确保有数据行
                last_row = rows[-1]
                balance = float(last_row[1])  # 获取最后一行的balance列数据
                return balance
    return None

# 发送邮件函数
def send_email():
    try:
        # 创建MIMEMultipart对象
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # 添加邮件正文
        msg.attach(MIMEText(body, 'plain'))

        # 使用SMTP_SSL发送邮件
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# 每小时检测一次balance值
def monitor_balance():
    while True:
        balance = get_last_balance(csv_file_path)
        if balance is not None:
            print(f"Current balance: {balance}")
            if balance <= 20:
                print("Balance is low, sending alert email...")
                send_email()
        else:
            print("No balance data found.")
        
        # 每100小时检测一次
        time.sleep(360000)

if __name__ == "__main__":
    monitor_balance()
