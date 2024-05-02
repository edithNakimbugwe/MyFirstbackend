import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))  # Connect to Google's DNS server
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

if __name__ == "__main__":
    print("Local IP address:", get_local_ip())
