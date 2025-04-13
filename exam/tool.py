#pip install psutil
import os
import psutil

def memory_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss  # ค่า RSS (Resident Set Size) หน่วยเป็น byte
    print(f"Memory usage: {mem / (1024 * 1024):.2f} MB")