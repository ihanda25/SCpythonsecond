import time

X = raw_input("Enter what kind of time mesurement you are using: ")

if X == "seconds":
    sec = float(raw_input("Enter num of seconds: "))
    status = "calculating..."
    print(status)
    hour = sec // 3600
    sec_remaining = sec%3600
    minutes = sec_remaining // 60
    final_sec_remaining = sec_remaining%60
    time.sleep(3.5)
    status = "Done!"
    print status
    time.sleep(1)
    print(hour, "hours", minutes, "minutes", final_sec_remaining, "seconds")

else:
    if X == "minutes":
        minutes = float(raw_input("Enter num of minutes: "))
        status = "calculating..."
        print status
        sec = minutes *60
        hour = sec//3600
        sec_remaining = sec %3600
        final_minutes = sec_remaining // 60
        final_sec_remaining = sec_remaining%60
        time.sleep(3.5)
        status = "Done!"
        print(status)
        time.sleep(1)
        print(hour, "hours", final_minutes, "minutes", final_sec_remaining, "seconds")
    else:
        if X == "hours":
            hour = float(raw_input("Enter num of hours: "))
            status = "calculating..."
            print status
            sec = hour * 3600
            final_hour = sec // 3600
            sec_remaining = sec%3600
            minutes = sec_remaining // 60
            final_sec_remaining = sec_remaining%60
            time.sleep(3.5)
            status = "Done!"
            print status
            time.sleep(1)
            print(final_hour, "hours", minutes, "minutes", final_sec_remaining, "seconds")