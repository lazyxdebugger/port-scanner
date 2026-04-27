import socket

target = input("Enter IP or domain: ")

# works for both IP and domain
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid IP or domain")
    exit()

start = int(input("Enter the start port: "))
end = int(input("Enter the end port: "))

print(f"Scanning {target_ip}...")

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    res = s.connect_ex((target_ip, port))
    if res == 0:
        print(f"Port {port} is open")

    s.close()
