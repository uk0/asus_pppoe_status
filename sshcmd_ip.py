import paramiko

def get_router_wan_ip(host, port, username, password):
    # 创建SSHClient 实例
    ssh = paramiko.SSHClient()
    # 自动添加主机密钥（避免在未配置known_hosts时出现提示）
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接路由器
        ssh.connect(host, port=port, username=username, password=password)

        # 执行获取WAN IP的命令
        stdin, stdout, stderr = ssh.exec_command("nvram get wan0_ipaddr")

        # 从 stdout 读取结果（bytes -> str）并去掉多余的换行
        wan_ip = stdout.read().decode().strip()
        return wan_ip
    except Exception as e:
        print(f"SSH连接或执行命令出错: {e}")
        return None
    finally:
        ssh.close()
