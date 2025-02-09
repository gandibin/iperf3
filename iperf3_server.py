import subprocess
import threading

def start_iperf_server(ip, port):
    """
    在指定IP和端口上启动iperf3服务器。
    :param ip: 服务器的IP地址
    :param port: 监听的端口
    """
    try:
        command = [
            'iperf3',
            '-s',  # 服务端模式
            '-B', ip,  # 绑定到特定的IP
            '-p', str(port),  # 指定监听端口
            '--json'  # 输出结果为JSON格式
        ]
        print(f"启动iperf3服务端在 {ip}:{port}")
        subprocess.run(command, text=True)
    except Exception as e:
        print(f"在 {ip}:{port} 启动iperf3服务端时发生错误: {e}")

def main():
    # 定义IP地址和端口
    base_port = 5201
    ips = [f"192.168.5.{i}" for i in range(30, 38)]  # 192.168.5.20 - 192.168.5.27
    threads = []

    # 为每个IP启动一个服务端实例
    for index, ip in enumerate(ips):
        port = base_port + index
        thread = threading.Thread(target=start_iperf_server, args=(ip, port))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    #pss