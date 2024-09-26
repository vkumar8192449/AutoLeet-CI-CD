import random
import subprocess
import time

# Generate a random number from 1 to 4
num_runs = random.randint(1, 2)
print(f"Running script.py {num_runs} times.")

# Run script.py the specified number of times
for i in range(num_runs):
    subprocess.run(["python", "leetcode_hitter.py"])
    if i < num_runs - 1:  # Avoid waiting after the last run
        print(f"Waiting for 15 seconds before the next run...")
        time.sleep(15)