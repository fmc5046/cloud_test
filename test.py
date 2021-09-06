import sys
old_stdout = sys.stdout

log_file = open("message.log","w")

sys.stdout = log_file

print("Hello World")

sys.stdout = old_stdout

log_file.close()