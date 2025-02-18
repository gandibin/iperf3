class UserInput:
    def __init__(self):
        self.device = None
        self.ips = []
        self.bandwidth = None
        self.threads = None
        self.test_choice = None
        self.device_type = None
    
    def collect_inputs(self):
        """收集所有必要的输入"""
        self.device = input("请选择你的设备 (A - 设备A，B - 设备B): ").strip().upper()
        self.device_type = input("请输入设备类型 (S - 服务器，C - 客户机): ").strip().upper()
        self.ips = self.get_device_ip(self.device)
        
        
        # 选择测试功能
        self.test_choice = self.get_test_choice()

        # 根据选择的测试类型动态询问需要的参数
        if self.test_choice == '2' or self.test_choice == 'A':  # UDP 或 测试全部功能
            self.bandwidth = input("请输入带宽（例如10M，100M，1G）：").strip()
        
        if self.test_choice == '3' or self.test_choice == 'A':  # 多通道测试 或 测试全部功能
            self.threads = int(input("请输入并发线程数："))
    
    def get_device_ip(self, device):
        """根据设备选择返回一批IP地址"""
        if device == 'A':
            return [f"192.168.5.{i}" for i in range(31, 41)]  # 192.168.5.31-40
        elif device == 'B':
            return [f"192.168.5.{i}" for i in range(21, 31)]  # 192.168.5.21-30
        else:
            print("无效设备，返回空列表。")
            return []
    
    def get_test_choice(self):
        """获取测试类型选择"""
        print("\n请选择测试功能：")
        print("1. TCP测试")
        print("2. UDP测试")
        print("3. 多线程测试")
        print("4. 双向测试")
        print("A. 测试全部功能")
        choice = input("请输入你的选择：").strip().upper()
        return choice

