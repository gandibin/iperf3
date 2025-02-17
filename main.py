from user_input import UserInput
from iperf3_test import Iperf3Test

def main():
    print("欢迎使用iperf3测试工具！")
    
    mode = input("请选择设备模式 (S - 服务器端，C - 客户端): ").strip().upper()
    if mode == 'S':
        # 服务器端模式
        print("正在启动iperf3服务器...")
        Iperf3Test.run_server()
    elif mode == 'C':
        # 客户端模式
        user_input = UserInput()
        device = user_input.get_device_choice()
        ip = user_input.get_device_ip(device)

        if ip:
            while True:
                test_choice = user_input.get_test_choice()
                iperf3_test = Iperf3Test(ip)
                
                if test_choice == '1':
                    iperf3_test.test_tcp()
                elif test_choice == '2':
                    iperf3_test.test_udp()
                elif test_choice == '3':
                    iperf3_test.test_multithread()
                elif test_choice == '4':
                    iperf3_test.test_bidirectional()
                elif test_choice == 'A':
                    iperf3_test.test_full()
                else:
                    print("无效选项，请重新选择。")

                cont = input("是否继续测试？(Y - 继续，N - 退出)：").strip().upper()
                if cont != 'Y':
                    print("感谢使用，程序退出。")
                    break
        else:
            print("无效的设备选择，请重新启动程序。")
    else:
        print("无效的设备模式，请重新选择。")

if __name__ == "__main__":
    main()
