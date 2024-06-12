from body import body
print("[main] finished import body.body")
from sys import exit
print("[main] finished import sys.exit")

def main():
    while True:
        body_code = body()
        if body_code == 1:
            return 1
    return 0

if __name__ == "__main__":
    return_code = main()
    if return_code == 1:
        print("[main] exiting process")
        exit()
    elif return_code == 0:
        print("[main] i don't know what happened")
