'''Create a sample log file access.log containing records of web server access logs (timestamp, IP 12)  Sr. No. address, URL). 
▪ Write a Python program to extract and display all unique IP addresses. 
▪ Count the number of occurrences of each IP address'''

file=open("access.log", "w")
file.write("2026.04-23 ____ 15.05.25 ____ 192.168.1.10 ____ /home/sarthak52/CTPL/access.log \n")
file.write("2026.04-23 ____ 15.05.26 ____ 192.168.1.20 ____ /home/sarthak52/CTPL/access.log \n")
file.write("2026.04-23 ____ 15.05.27 ____ 192.168.1.30 ____ /home/sarthak52/CTPL/access.log \n")
file.write("2026.04-23 ____ 15.05.28 ____ 192.168.1.40 ____ /home/sarthak52/CTPL/access.log \n")
file.write("2026.04-23 ____ 15.05.29 ____ 192.168.1.50 ____ /home/sarthak52/CTPL/access.log \n")
file.write("2026.04-23 ____ 15.05.30 ____ 192.168.1.60 ____ /home/sarthak52/CTPL/access.log \n")
file.close()


print("Log file access.log created successfully with sample data.")

file=open("access.log", "r")

ip_list = []
for line in file:
    data = line.split()

    ip_list.append(data[4])  

file.close()

print("Unique IP addresses found:")
unique_ips = set(ip_list)

for ip in unique_ips:
    print(ip)

print("\n IP Address Occurrences:")
for ip in unique_ips:
    count = ip_list.count(ip)
    print(f"{ip}: {count}")