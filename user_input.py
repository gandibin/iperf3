class UserInput:
    def __init__(self):
        self.device = None
        self.ip = None
    
    def get_device_choice(self):
        self.device = input("请选择你的设备 (A - 设备A，B - 设备B): ").strip().upper()
        return self.device
    
    def get_device_ip(self, device):
        if device == 'A':
            return input("请选择设备A的IP地址（范围192.168.5.31-40）：").strip()
        elif device == 'B':
            return input("请选择设备B的IP地址（范围192.168.5.21-30）：").strip()
        else:
            print("无效设备，返回默认IP地址。")
            return None
    
    def get_test_choice(self):
        print("\n请选择测试功能：")
        print("1. TCP测试")
        print("2. UDP测试")
        print("3. 多线程测试")
        print("4. 双向测试")
        print("A. 测试全部功能")
        choice = input("请输入你的选择：").strip().upper()
        return choice
