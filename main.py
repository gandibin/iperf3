from user_input import UserInput
from iperf3_test import Iperf3Test

def main():
    print("欢迎使用iperf3测试工具！")
    
    # 收集所有用户输入
    user_input = UserInput()
    user_input.collect_inputs()  # 收集所有输入
    
    if user_input.device_type == 'S':
        # 服务器端模式
        Iperf3Test.run_server()
    elif user_input.device_type == 'C':
        # 客户端模式
        iperf3_test = Iperf3Test(user_input.ips, user_input.bandwidth, user_input.threads, user_input.test_choice)
        
        if user_input.test_choice == '1':
            iperf3_test.test_tcp()
        elif user_input.test_choice == '2':
            iperf3_test.test_udp()
        elif user_input.test_choice == '3':
            iperf3_test.test_multithread()
        elif user_input.test_choice == '4':
            iperf3_test.test_bidirectional()
        elif user_input.test_choice == 'A':
            iperf3_test.test_full()
        else:
            print("无效选项，请重新选择。")
    else:
        print("无效的设备模式，请重新选择。")

if __name__ == "__main__":
    main()
