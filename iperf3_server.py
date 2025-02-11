import subprocess
import datetime
import threading
import time

def save_log(output, ip, port, server_count):
    """保存输出到日志文件，并将服务端数量添加到文件名中"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"iperf3_{ip}_to_{port}_{current_time}_servers_{server_count}.log"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"日志已保存到 {filename}")

def start_iperf_server(ip, port=5201, server_count=1):
    """启动 iperf3 服务端并定期保存输出"""
    command = [
        'iperf3',
        '-s',                # 启动服务端
        '-B', ip,            # 绑定到特定IP地址
        '-p', str(port),     # 指定端口
        '--json'             # 输出结果为JSON格式，便于解析
    ]
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    print(f"iperf3服务端正在 {ip}:{port} 上运行...")

    output = ""
    last_data_time = time.time()  # 初始化最后数据接收时间

    while True:
        line = process.stdout.readline()
        if line:
            output += line
            last_data_time = time.time()  # 更新最后数据接收时间
        elif time.time() - last_data_time > 5:  # 检查是否超过5秒没有收到新数据
            save_log(output, ip, port, server_count)  # 保存日志
            output = ""  # 重置输出缓存
            last_data_time = time.time()  # 重置最后数据接收时间
        if not line and process.poll() is not None:
            break  # 进程结束，退出循环

    if output:  # 进程结束后，确保保存任何剩余的输出
        save_log(output, ip, port, server_count)

def manage_servers():
    threads = []
    
    # 获取用户输入的服务器数量
    try:
        server_count = int(input("请输入测试的服务端数量（1-8）："))
        if server_count < 1 or server_count > 8:
            print("请输入一个有效的数量（1到8之间）！")
            return
    except ValueError:
        print("无效输入！请输入数字。")
        return
    
    # 动态生成 IP 地址范围
    server_ips = [f"192.168.5.{i}" for i in range(30, 30 + server_count)]  # 根据输入的数量生成服务器IP地址
    thread_count = server_count  # 线程数和服务器数相同
    
    for server_ip in server_ips:
        thread = threading.Thread(target=start_iperf_server, args=(server_ip, 5201, thread_count))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()  # 等待所有线程完成

if __name__ == "__main__":
    manage_servers()
