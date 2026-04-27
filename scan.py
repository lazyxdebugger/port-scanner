import socket

target = input("Enter IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid IP or domain")
    exit()

start = int(input("Enter the start port: "))
end = int(input("Enter the end port: "))

if start>end:
    print("invalid range.")
    exit()

print(f"Scanning {target_ip}...")

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    res = s.connect_ex((target_ip, port))

    if res == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "unknown"

        print(f"Port {port} ({service}) is open")

    s.close()
