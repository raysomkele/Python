import time

password = 1979
times = 3

print("This is the info-hub")
password = int(input("What is the password"))
if password == 1979:
    print("Welcome. We may need to ask you some questions")
else:
    times = times - 1
    print("Wrong password try again")
if times == 0:
    time_to_wait = 5
    wait = time.sleep(time_to_wait * 2)



