import subprocess
import json
import threading
import time
import datetime

class Iperf3Test:
    def __init__(self, server_ips, client_ips, bandwidth, threads, test_choice):
        self.server_ips = server_ips
        self.client_ips = client_ips
        self.bandwidth = bandwidth
        self.threads = threads
        self.test_choice = test_choice

    def save_log(self, output, client_ip, server_ip, test_type):
        """保存输出到JSON日志文件，并将服务端数量添加到文件名中"""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ports = str(len(self.client_ips))
        filename = f"{test_type}_thread_{ports}_{client_ip}_to_{server_ip}_{current_time}.json"
        with open(filename, 'w') as file:
            json.dump(output, file, indent=4)
        print(f"日志已保存到 {filename}")

    def run_client(self, client_ip, server_ip):
        """客户端进行iperf3测试，根据测试类型传入不同的命令"""
        print(f"正在启动iperf3客户端，{client_ip} 连接到 {server_ip}...")
        # 根据测试类型选择不同的命令
        if self.test_choice == '1':  # TCP 测试
            command = ["iperf3", "-c", server_ip, "-t", "60", "--json", "-B", client_ip]
            testype = "TCP"
        elif self.test_choice == '2':  # UDP 测试
            command = ["iperf3", "-c", server_ip, "-u", "-b", self.bandwidth, "-t", "60", "--json", "-B", client_ip]
            testype = "UDP"
        elif self.test_choice == '3':  # 多线程测试
            command = ["iperf3", "-c", server_ip, "-t", "60", "--json", "-P", str(self.threads), "-B", client_ip]
            testype = "multithread"
        elif self.test_choice == '4':  # 双向测试
            command = ["iperf3", "-c", server_ip, "-d", "-t", "60", "--json", "-B", client_ip]
            testype = "bidirectional"
        else:
            print("无效的测试类型。")
            return
        # 执行命令并获取输出
        result = subprocess.run(command, capture_output=True, text=True)
        try:
            json_output = json.loads(result.stdout)
            # 保存日志
            self.save_log(json_output, client_ip, server_ip, testype)
        except json.JSONDecodeError:
            print(result.stdout)
            with open(f"{testype}_{server_ip}_to_{client_ip}_ports{str(len(self.client_ips))}.txt", 'w') as file:
                file.write(result.stdout)
            print(f"无法解析服务器日志 {server_ip}，已保存为文本文件...")



    def test_tcp(self):
        """进行TCP测试"""
        print("选择TCP测试...")
        threads = []
        for client_ip, server_ip in zip(self.client_ips, self.server_ips):
            thread = threading.Thread(target=self.run_client, args=(client_ip, server_ip))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # 等待所有线程完成

    def test_udp(self):
        """进行UDP测试"""
        print("选择UDP测试...")
        threads = []
        for client_ip, server_ip in zip(self.client_ips, self.server_ips):
            thread = threading.Thread(target=self.run_client, args=(client_ip, server_ip))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # 等待所有线程完成

    def test_multithread(self):
        """进行多线程测试"""
        print("选择多线程测试...")
        threads = []
        for client_ip, server_ip in zip(self.client_ips, self.server_ips):
            thread = threading.Thread(target=self.run_client, args=(client_ip, server_ip))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # 等待所有线程完成

    def test_bidirectional(self):
        """进行双向测试"""
        print("选择双向测试...")
        threads = []
        for client_ip, server_ip in zip(self.client_ips, self.server_ips):
            thread = threading.Thread(target=self.run_client, args=(client_ip, server_ip))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # 等待所有线程完成

    @staticmethod
    def start_multiple_servers(server_ips):
        """启动多个iperf3服务器，每个IP绑定一个服务器"""
        threads = []
        for server_ip in server_ips:
            thread = threading.Thread(target=Iperf3Test.run_server, args=(server_ip,))
            threads.append(thread)
            thread.start()

        # 等待所有线程完成
        for thread in threads:
            thread.join()

        print("所有服务器已停止。")

    @staticmethod
    def run_server(server_ip):
        """启动iperf3服务器并绑定到指定的IP地址"""
        print(f"正在启动iperf3服务器，绑定到 IP: {server_ip}...")
        command = ["iperf3", "-s", "-B", server_ip, "--json"]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        output = ""
        while True:
            line = process.stdout.readline()
            if line:
                output += line
            elif not line and process.poll() is not None:
                break  # 进程结束，退出循环

        if output:
            try:
                json_output = json.loads(output)
                Iperf3Test.save_log(json_output, server_ip, server_ip, "server")
            except json.JSONDecodeError:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                with open(f"server_log_{server_ip}_{current_time}.txt", 'w') as file:
                    file.write(output)
                print(f"无法解析服务器日志 {server_ip}，已保存为文本文件...")
