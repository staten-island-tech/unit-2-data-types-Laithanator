#set stopwatch
#stopwatchTime = stopwatch
#switchTime = stopwatchTime % 5
#if switchTime === 0 true
#if traffic eastward true
#set traffic westward
#else
#set traffic eastward






westboundTraffic = input("State whether westbound traffic is going (if it is then input true, if it isn't input false) ")
eastboundTraffic = input("State whether eastbound traffic is going (if it is then input true, if it isn't input false) ")
if eastboundTraffic and westboundTraffic === ("true"):
    print("FALSE STATEMENT")
else:
    print("TRUE STATEMENT")