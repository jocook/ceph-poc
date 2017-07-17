import sys
import json
import ucscceph
import ucsmceph
import time

ucsm = ucsmceph.UcsmCeph()
ucsc = ucscceph.UcscCeph()

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print "Usage: %s <JSON settings file>" % sys.argv[0]
            print "       <settings file>: all settings"
            sys.exit(0)
        with open(sys.argv[1]) as f:
            settings = json.load(f)

        print "\n#######################################################"
        print "################UCSM Deployment #######################"
        print "#######################################################"
        ucsm.deploy(settings)
        #print "Waiting 30 seconds..."
        #time.sleep(30)
        print "\n#######################################################"
        print "################UCSC Deployment #######################"
        print "#######################################################"
        ucsc.deploy(settings)


    except Exception, err:
        print "Exception:", str(err)
        import traceback, sys

        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60




