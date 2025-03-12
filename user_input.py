class UserInput:
    def __init__(self):
        self.device = None
        self.server_ips = []
        self.client_ips = []
        self.bandwidth = None
        self.threads = None
        self.test_choice = None
        self.device_type = None
        self.ip_count = None
    
    def collect_inputs(self):
        """收集所有必要的输入"""
        self.device = input("请选择你的设备 (A - 设备A 192.168.5.31-，B - 设备B 192.168.5.21-): ").strip().upper()
        
        # 检查设备是否有效
        if self.device not in ['A', 'B']:
            print("无效设备，请重新选择。")
            return
        
        self.ip_count = int(input("请输入需要测试的IP地址数量: "))
        
        self.device_type = input("请输入设备类型 (S - 服务器，C - 客户机): ").strip().upper()
        
        # 检查设备类型是否有效
        if self.device_type not in ['S', 'C']:
            print("无效设备类型，请重新选择。")
            return
        
        self.server_ips, self.client_ips = self.get_device_ip(self.device, self.device_type, self.ip_count)
        
        if self.device_type == "C":
            self.test_choice = self.get_test_choice()

        # 根据选择的测试类型动态询问需要的参数
        if self.test_choice == '2':  # UDP
            self.bandwidth = input("请输入带宽（例如10M，100M，1G）：").strip()
        
        if self.test_choice == '3':  # 多通道测试 
            self.threads = int(input("请输入并发线程数："))
    
    def get_device_ip(self, device, device_type, ip_count):
        """根据设备选择返回一批IP地址"""
        a_ips = [f"192.168.5.{i}" for i in range(31, 31 + ip_count)]  # 192.168.5.31-40
        b_ips = [f"192.168.5.{i}" for i in range(21, 21 + ip_count)]  # 192.168.5.21-30
        #如果选择1单条线测试要
        if ip_count == 1:
            lan_number = int(input("请输入测试的lan端口号1-10："))
            a_ips = [f"192.168.5.{30+lan_number}"] 
            b_ips = [f"192.168.5.{20+lan_number}"] 
        # 定义设备和设备类型的映射关系
        device_map = {
            'A': {
                'S': (a_ips, b_ips),  # A 设备，服务器：A的IP作为服务器，B的IP作为客户端
                'C': (b_ips, a_ips)   # A 设备，客户端：B的IP作为服务器，A的IP作为客户端
            },
            'B': {
                'S': (b_ips, a_ips),  # B 设备，服务器：B的IP作为服务器，A的IP作为客户端
                'C': (a_ips, b_ips)   # B 设备，客户端：A的IP作为服务器，B的IP作为客户端
            }
        }

        # 根据设备和设备类型获取服务器和客户端的IP
        server_ips, client_ips = device_map.get(device, {}).get(device_type, ([], []))

        if not server_ips or not client_ips:
            print("无效设备或设备类型，返回空列表。")
            return [], []  # 返回空列表

        return server_ips, client_ips

    def get_test_choice(self):
        """获取测试类型选择"""
        print("\n请选择测试功能：")
        print("1. TCP测试")
        print("2. UDP测试")
        print("3. 多线程测试")
        print("4. 双向测试")
        choice = input("请输入你的选择：").strip().upper()
        return choice
