import redis
import time

def consumer ():
    r = redis.StrictRedis ()

    while True:
        qname, msg = r.blpop ('hello_queue')
        print 'received', msg

def producer (name):
    r = redis.StrictRedis ()
    i = 0

    while True:
        m = 'hi from {0}! msg # {1}'.format (name, i)
        i += 1
        
        r.rpush ('hello_queue', m)
        time.sleep (5)

def subscriber (channel):
    pubsub = redis.StrictRedis ().pubsub ()
    pubsub.subscribe (channel)

    for msg in pubsub.listen ():
        if msg['type'] == 'message':
            print 'received', msg['data'], 'on', msg['channel']

def publisher (name, channel):
    r = redis.StrictRedis ()
    i = 0

    while True:
        m = 'hi from {0}! msg # {1}'.format (name, i)
        i += 1
        
        r.publish (channel, m)
        time.sleep (5)


   


