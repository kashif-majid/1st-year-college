import time
from time import time as my_timer
import random

input("PRESS ENTER TO START")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("PRESS ENTER TO STOP")

end_time = my_timer()

print("STARTED AT " + time.strftime("%X", time.localtime(start_time)))
print("ENDED AT " + time.strftime("%X", time.localtime(end_time)))

print("YOUR REACTION TIME WAS {} SECONDS".format(end_time - start_time))
