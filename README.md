# port-scanner
A simple Python-based port scanner that scans a target IP address or domain to identify open ports using socket programming.

---

**`Features`**
- Scans custom port ranges
- Supports IP and domain names
- Detects common services running on open ports

---
**`what it does?`**
- It scans a targeted IP/domain name to identify the open ports on that IP/domain.
---

**`how to run?`**
```bash
python scan.py
```
---

**`example output`**
- tried it on my own IP.
 
─(zoro㉿kali)-[~/Desktop/portscan]

└─$ python scan.py

Enter IP or domain: 127.0.0.1

Enter the start port: 8000

Enter the end port: 8005

Scanning 127.0.0.1...

Port 8000 is open

---

**`version`**
```md
Current Version: v4
```
---

**`output after new updates`**

(zoro㉿kali)-[~/Desktop/portscan]

└─$ python scan.py

Enter IP or domain: localhost

Enter the start port: 1  

Enter the end port: 100

Scanning 127.0.0.1...

Port 80 (http) is open

---

**`Disclaimer`**

This tool is for educational purposes only.
Only scan systems you own or have permission to test.
