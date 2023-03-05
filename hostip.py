import socket

def get_host_ip_address(host):
    try:
        ip_address = socket.gethostbyname(host)
        return ip_address
    except socket.gaierror:
        print("Error: Invalid hostname or IP address")
        return None

host_site = "www.example.com"
ip_address = get_host_ip_address(host_site)
if ip_address:
    print("The IP address of", host_site, "is", ip_address)
