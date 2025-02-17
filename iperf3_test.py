import subprocess

class Iperf3Test:
    def __init__(self, ip=None):
        self.ip = ip

    @staticmethod
    def run_server():
        """启动iperf3服务器"""
        print("正在启动iperf3服务器...")
        subprocess.run(["iperf3", "-s"])

    def run_client(self, protocol, bandwidth=None, time=10, threads=1, bidirectional=False):
        """启动iperf3客户端"""
        print(f"正在启动iperf3客户端，连接到 {self.ip}...")
        command = ["iperf3", "-c", self.ip, "-t", str(time), "-P", str(threads)]

        if protocol == "UDP":
            command.append("-u")
            if bandwidth:
                command.extend(["-b", bandwidth])
            command.append("-i 1")  # 每秒报告一次丢包率和延迟

        if bidirectional:
            command.append("-d")  # 启动双向测试

        subprocess.run(command)

    def test_tcp(self):
        """进行TCP测试"""
        print("选择TCP测试...")
        self.run_client("TCP")

    def test_udp(self):
        """进行UDP测试"""
        print("选择UDP测试...")
        bandwidth = input("请输入带宽（例如10M，100M，1G）：")
        self.run_client("UDP", bandwidth)

    def test_multithread(self):
        """进行多线程测试"""
        print("选择多线程测试...")
        threads = int(input("请输入并发线程数："))
        self.run_client("TCP", threads=threads)

    def test_bidirectional(self):
        """进行双向测试"""
        print("选择双向测试...")
        self.run_client("TCP", bidirectional=True)

    def test_full(self):
        """进行全面测试（TCP、UDP、多线程）"""
        print("选择全面的网络性能测试...")
        self.test_tcp()
        self.test_udp()
        self.test_multithread()
