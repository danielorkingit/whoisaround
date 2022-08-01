import subprocess

DEVICE_IP = '192.168.2.214'

def checkifconnected():

    a = subprocess.run(["ping", "-n", "2", DEVICE_IP], stdout=subprocess.PIPE, text=True, shell=True) # ping the phone/device in the local network; get exit code

    if a.returncode == 0:
        print(a)

        return 202 # established connection to the IP adress

    else:

        print(a)

        return 1 # no connection to the IP adress
