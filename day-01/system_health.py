import psutil
#Check-cpu,memory,disk of system using python library & take respective thresholds from USER 
# Then compare the value with result in Terminal
def check_cpu():
    cpu_threshold = int(input("Enter the CPU Threshold:"))
    current_cpu = psutil.cpu_percent(interval=1) 
    print(f"current CPU% is {current_cpu} ")
    if current_cpu > cpu_threshold:
        print("CPU-ALERT Email sent....")
    else:
        print("CPU in SAFE state")

def check_mem():
    mem_threshold = int(input("Enter MEMORY Threshold :"))
    current_mem = psutil.virtual_memory().percent #attribute - percentage
    print(f"current Memory% is {current_mem} ")
    if current_mem > mem_threshold:
        print("MEMORY ALERT Email sent ...")
    else:
        print("MEMORY in SAFE state")
    
def check_disk():
    disk_threshold = int(input("Enter Disk Threshold :"))
    current_disk = psutil.disk_usage('/').percent # attribute - percent
    print(f"Disk Usage in ROOT is :{current_disk}")
    if disk_threshold > current_disk:
       print("DISK ALERT Email sent...")
    else:
       print("DISK usage in SAFE STATE")

check_cpu()
check_mem()
check_disk()