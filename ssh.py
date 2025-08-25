import socket
# SSH默认端口
HOST = '0.0.0.0'
PORT = 22  
banner = b"SSH-2.0-OpenSSH_8.0\r\n"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Fake SSH service running on port {PORT}...")
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connection from:', addr)
            conn.sendall(banner)
