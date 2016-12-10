# python3
# this program takes ip address as input and tells valid or invalid.
# try these ip addresses
# correct ip's : 127.0.0.1, 192.168.0.1, 255.255.255.0
# Wrong ip's : .123.1.1.1, 123.256.1.1, 123.123.123.1111, 10.1m.2.2, 12.34.1.2.3.4, ''- means enter
# 0.0.0.0 should be invalid
ip = input("Enter ip address: ")
count = 0
for i in ip.split('.'):
    try:
        if int(i) not in range(0, 256):
            print("{} is not in range 0-256".format(int(i)))
            exit()
        elif int(i) == 0:
            count += 1
            if count == 4:
                print("{} is not valid".format(ip))
                break
    except ValueError:
        print("Oops! '{}' is not valid.  Try again...".format(i))
        exit()
else:
    print("{} is valid ip address".format(ip))
