import subprocess

def run_iperf(server_ip, client_ip, duration=30):
    """
    运行iperf3测试的函数，介于服务器和客户端之间。
    :param server_ip: 服务器的IP地址
    :param client_ip: 客户端的IP地址
    :param duration: iperf测试的持续时间（秒）
    :return: iperf3的输出结果
    """
    try:
        # 构建iperf3命令
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
            print("测试成功完成。")
            return result.stdout
        else:
            print("测试运行错误：")
            print(result.stderr)
            return None
    except Exception as e:
        print(f"执行iperf3命令时发生错误: {e}")
        return None

# 示例用法
server_ip = '192.168.5.30'
client_ip = '192.168.5.20'
duration = 30  # 测试时间为30秒

# 运行测试
output = run_iperf(server_ip, client_ip, duration)
if output:
    print("测试输出：")
    print(output)
