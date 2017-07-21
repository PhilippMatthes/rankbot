from Rankbot import Rankbot
from Mailer import Mailer
from time import sleep
import traceback
import sys

if __name__=="__main__":
    rankbot = Rankbot()
    mailer = Mailer()
    mailer.send("Ranking Bot started. Please send >>Start<< to start")
    while True:
        message = mailer.get_current_message()
        if (message == "Start" or message == "Continue"):
            try:
                rankbot.get_headlines(2)
            except KeyboardInterrupt:
                mailer.send("Keyboard Interrupt. Bot will exit now.")
                print("Exiting...")
                break
            except Exception as err:
                for frame in traceback.extract_tb(sys.exc_info()[2]):
                    fname, lineno, fn, text = frame
                error = "Error in "+str(fname)+" on line "+str(lineno)+": "+str(err)
                mailer.send(err)
                print(err)
                sleep(1)
                pass
        else:
            if (message == "Stop" or message == "Exit"):
                mailer.send("Ranking Bot will exit now.")
                break
            sleep(1)
