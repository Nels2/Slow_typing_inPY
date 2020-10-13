import sys
import time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.7/10)

if __name__ == '__main__':
    slowprint("This text is being shown to you as if it were a type-writer")
    #prints everything a letter at a time.
    while True:
        slowprint("Would you like to being the exploration of Nelson's Mind?")
        x = input()
        if x != 'y':
            slowprint("Okay!. eti")
            continue
        elif x == 'y':
            slowprint("We wwill continue, I suppose.")
            break
        else:
            continue
    
