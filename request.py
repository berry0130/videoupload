import requests,os,subprocess
import time
# while True:
# 	time.sleep(300)
# 	os.system('curl 0.0.0.0:8080')
while True:
	r=os.popen('uptime --p').read()
	now=int(r[3]+r[4])
	print(now)
	if now>3:
		os.system('python /home/vr760//lidar_interaction/apps/app_manager.py')
		print('turn')
		break
