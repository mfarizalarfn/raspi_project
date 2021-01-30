relayOn = False

def turnRelayOn():
    relayOn = True
    #turn on the relay
def turnRelayOff():
    relayOn = False
    #turn off the relay

def printRelayState():
    if relayOn:
        print "The relay is currently ON"
    else:
        print "The relay is currently OFF"
