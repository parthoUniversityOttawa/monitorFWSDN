import csv,json
import parser
from flask import Flask, json
import sys
import os
import thread
import subprocess 
import signal
from threading import Thread
import time

pid_startServerProcess = 0 
pid_startController = 0 

def startServer():
	import os
	import subprocess
	devnull = open('/dev/null', 'w')
	startServerProcess = subprocess.Popen(["python", "server.py"], stdout=devnull ,shell= False)
	global pid_startServerProcess
	pid_startServerProcess = startServerProcess.pid
	
#os.system("python server.py") 
	

def startController():
	import os
	import subprocess
	devnull = open('/dev/null', 'w')
	startController = subprocess.Popen(["python", "pox/pox.py", "monitorFwSDN.startup"], stdout=devnull, shell=False)
	global pid_startController
	pid_startController = startController.pid
	

def receiveSignal(sig, frame):
	print("startServerProcess PID:",pid_startServerProcess)
	print("startController PID:",pid_startController)
	os.kill(pid_startServerProcess, signal.SIGINT)
	os.kill(pid_startController, signal.SIGINT)
	exit(0)

if __name__ == "__main__":

    if "pox" == str(sys.argv[1]):
	signal.signal(signal.SIGINT, receiveSignal)
	t = Thread ( target = startServer )
	t.start()
	t1 = Thread ( target = startController )
	t1.start()
	#thread.start_new_thread( startServer, ( ) )
	#thread.start_new_thread( startController, ( ) )
	time.sleep(1)
	while(1):
		pass
	#print("startServerProcess PID:",pid_startServerProcess)
	
	#print("startController PID:",pid_startController)
	
