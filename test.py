import sys
import time

old_stdout = sys.stdout
log_file = open("message.log","w")
sys.stdout = log_file

ts = time.time()

print(f"Hello World {ts}")

sys.stdout = old_stdout
log_file.close()