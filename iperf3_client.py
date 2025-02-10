import subprocess
import threading
import datetime

def save_log(output, client_ip, server_ip):
    """保存输出到日志文件"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"iperf3_test_{client_ip}_to_{server_ip}_{current_time}.log"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"日志已保存到 {filename}")

def run_iperf(server_ip, client_ip, duration=30):
    """
    运行iperf3测试，介于服务器和客户端之间。
    :param server_ip: 服务器的IP地址
    :param client_ip: 客户端的IP地址
    :param duration: iperf测试的持续时间（秒）
    :return: iperf3的输出结果
    """
    try:
        command = [
            'iperf3',
            '-c', server_ip,  # 指定服务器IP
            '-B', client_ip,  # 绑定到特定的客户端IP
            '-t', str(duration),  # 测试持续时间
            '--json'  # 输出结果为JSON格式，便于解析
        ]

        # 执行命令
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 检查测试是否成功
        if result.returncode == 0:
            print(f"测试从 {client_ip} 到 {server_ip} 成功完成。")
            save_log(result.stdout, client_ip, server_ip)
            return result.stdout
        else:
            print(f"测试从 {client_ip} 到 {server_ip} 出错：")
            print(result.stderr)
            save_log(result.stderr, client_ip, server_ip)
            return None
    except Exception as e:
        print(f"执行iperf3命令时发生错误: {e}")
        return None

def thread_function(server_ip, client_ip):
    run_iperf(server_ip, client_ip)

def manage_clients():
    threads = []
    server_ips = [f"192.168.5.{i}" for i in range(30, 38)]
    client_ips = [f"192.168.5.{i}" for i in range(20, 28)]
    
    for server_ip, client_ip in zip(server_ips, client_ips):
        thread = threading.Thread(target=thread_function, args=(server_ip, client_ip))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()  # 等待所有线程完成

if __name__ == "__main__":
    manage_clients()
