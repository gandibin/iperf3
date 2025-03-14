from user_input import UserInput
from iperf3_test import Iperf3Test
import sys

def main():
    print("欢迎使用iperf3测试工具！")
    try:
        # 收集所有用户输入
        user_input = UserInput()
        user_input.collect_inputs()  # 收集所有输入
        iperf3_instance = Iperf3Test(user_input.server_ips, user_input.client_ips, user_input.bandwidth, user_input.threads, user_input.test_choice)  #实例化控制单元
        
        # 判断设备类型，启动相应模式
        if user_input.device_type == 'S':
            # 服务器端模式，启动多个服务器
            iperf3_instance.start_multiple_servers()
        elif user_input.device_type == 'C':            
            if user_input.test_choice == '1':
                iperf3_instance.test_tcp()
            elif user_input.test_choice == '2':
                iperf3_instance.test_udp()
            elif user_input.test_choice == '3':
                iperf3_instance.test_multithread()
            elif user_input.test_choice == '4':
                iperf3_instance.test_bidirectional()
            else:
                print("无效选项，请重新选择。")
        else:
            print("无效的设备类型，请重新选择。")

    except KeyboardInterrupt:
        print("\n程序被用户终止，正在退出...")
        sys.exit(0)

if __name__ == "__main__":
    main()
    print("程序运行结束")
