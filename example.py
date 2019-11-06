#!/usr/bin/env python3
import sys
import pyjulius3
from queue import Queue, Empty

# Initialize and try to connect
client = pyjulius3.Client('localhost', 10500)
try:
    client.connect()
except pyjulius3.ConnectionError:
    print('Start julius as module first!')
    sys.exit(1)

# Start listening to the server
client.start()
try:
    while 1:
        try:
            result = client.results.get(False)
            if isinstance(result, pyjulius3.Sentence):
                print( 'Sentence "%s" recognized with score %.2f' % (result, result.score))

        except Empty:
            continue
        print( repr(result) )
except KeyboardInterrupt:
    print ('Exiting...')
    client.stop()  # send the stop signal
    client.join()  # wait for the thread to die
    client.disconnect()  # disconnect from julius
