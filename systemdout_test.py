import sys 
import time

for i in range(100):
    sys.stdout.write("\rProgress: %d%%"% (i+1))
    sys.stdout.flush()
    time.sleep(0.1)  # Simulate some work
print("\nTask completed!")