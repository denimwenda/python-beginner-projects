import socket

# List of ports to scan
ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 532, 5060, 5900, 5938, 8080, 10000, 20000]
host = input('Enter the site without http/https or IP address')
print("Wait, there is a port scan")

for port in ports:
    
    s = socket.socket()
    # Setting the time out to one second
    s.settimeout(1)
    
    try:
        s.connect((host, port))
        
        # If the connectio cost an error
    except socket.error:
        # then we don't do anything
        pass
    else:
        print(f"{host}: {port} port is active")
        s.close
        
print("The scan is complete")
