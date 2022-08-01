from mailer import mailer
from checker import checkifconnected

active = False

if __name__ == "__main__":

    while True:

        checkerresult = checkifconnected()

        if checkerresult == 202 and active == False:
            print("connected")
            mailer()
            active = True

        else:
            print("...")
                    
