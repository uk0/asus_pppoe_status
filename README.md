# asus_pppoe_status
RT-BE88U 路由器获取公网IP（前提需要自己将宽带账号转换为公网用户）


### examples

```python

host = "10.88.51.8"
port = 10022
username = "admin"
password = "admin123"

WAN_IP = get_router_wan_ip(host, port, username, password)
if WAN_IP:
    print(f"路由器 WAN IP: {WAN_IP}")
else:
    print("无法获取路由器 WAN IP")

```
