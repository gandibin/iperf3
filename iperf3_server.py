import subprocess
import datetime
import os
import threading

def save_log(output, ip, port):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{ip}_{port}_{current_time}.log"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"日志已保存到 {filename}")

def start_iperf_server(ip, port=5201):
    command = [
        'iperf3',
        '-s',
        '-B', ip,
        '-p', str(port),
        '--json'
    ]
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    print(f"在 {ip}:{port} 上启动iperf3服务端...")
    
    def monitor():
        print(f"iperf3服务端已启动在 {ip}:{port}。请输入'3'停止。")
        output = ""
        while True:
            action = input()
            if action == '3':
                process.terminate()  # 使用terminate方法来停止进程
                stdout, stderr = process.communicate()
                output += stdout
                if stderr:
                    output += "\n错误信息：\n" + stderr
                save_log(output, ip, port)
                print("iperf3服务端已停止。")
                break

    thread = threading.Thread(target=monitor)
    thread.start()

if __name__ == "__main__":
    ips = ["192.168.5." + str(i) for i in range(20, 238)]
    for ip in ips:
        start_iperf_server(ip)
