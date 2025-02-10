import subprocess
import datetime
import os
import threading

def save_log(output, ip, port):
    """保存输出到日志文件"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{ip}_{port}_{current_time}.log"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"日志已保存到 {filename}")

def start_iperf_server(ip, port=5201):
    """使用 subprocess.run 启动 iperf3 服务端并保存输出"""
    command = [
        'iperf3',
        '-s',
        '-B', ip,
        '-p', str(port),
        '--json'
    ]
    
    print(f"启动 iperf3 服务端在 {ip}:{port}...")
    result = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(f"iperf3 服务端在 {ip}:{port} 已停止。")
    if result.stdout:
        save_log(result.stdout, ip, port)

def manage_servers():
    threads = []
    ips = ["192.168.5." + str(i) for i in range(30, 38)]
    for ip in ips:
        port = 5201
        thread = threading.Thread(target=start_iperf_server, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # 等待所有线程完成

if __name__ == "__main__":
    manage_servers()
