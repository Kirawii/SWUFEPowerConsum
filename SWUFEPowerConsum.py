import requests
import time
import random
import logging
import csv
import os

# 设置日志配置
logging.basicConfig(
    filename='balance_data.log',  # 日志文件名
    level=logging.INFO,  # 记录级别
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
)

# 请求的 URL
url = 

# 请求头
headers = {
    
}

# Cookies
cookies = {
   
}


# 请求体数据
data = {
}

balance_data = []
balance_changes = []
timestamps = []

# 创建 CSV 文件并写入表头
csv_file_path = 'balance_data.csv'
if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Balance', 'Change'])  # 加入 'Change' 表头

# 无限循环
while True:
    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=data)

        if response.status_code == 200:
            try:
                response_data = response.json()
                balance = float(response_data.get('balance'))  # 获取 balance 数据
                if balance is not None:
                    if balance_data:
                        change = balance_data[-1] - balance
                        if change > 0:
                            balance_changes.append(change)
                        else:
                            change = 0  # 如果balance增加，将减少值设为0
                    else:
                        change = 0
                    balance_data.append(balance)

                    # 获取当前时间，格式化为 YYYY-MM-DD HH:MM:SS
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    timestamps.append(timestamp)

                    log_message = f'当前时间: {timestamp}, Balance: {balance}, 减少值: {change}'
                    print(log_message)  # 打印到控制台
                    logging.info(log_message)  # 写入日志文件

                    # 写入 CSV 文件，保存时间戳、余额和减少值
                    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([timestamp, balance, change])  # 写入减少值
                else:
                    logging.warning('未找到 balance 数据')
            except ValueError:
                error_message = '响应不是有效的 JSON'
                print(error_message)  # 调试
                logging.error(error_message)
                logging.error(response.text)  # 调试
        else:
            error_message = f'请求失败，状态码：{response.status_code}'
            print(error_message)
            logging.error(error_message)
            logging.error(response.text)

        # 随机化访问时间（在30到60分钟之间随机）
        wait_time = random.randint(1800, 3600) 
        time.sleep(wait_time)

    except Exception as e:
        # 捕获任何异常并记录
        error_message = f'发生异常: {str(e)}'
        print(error_message)
        logging.error(error_message)

        # 等待几秒后重启
        time.sleep(5)  # 等待5秒后再重启


