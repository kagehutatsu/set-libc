import os

def get_version():
	print ("1. ubuntu 16: libc-2.23.so")
	print ("2. ubuntu 18: libc-2.27.so")
	print ("3. ubuntu 19: libc-2.29.so")
	print ("4. ubuntu 20: libc-2.30.so")
	print ("which to choose? (1/2/3/4)")
	ver=input("choice:")
	return ver
	
def get_pre_libc():
	process=os.popen("ldd main")
	output=process.read()
	process.close()
	pre_libc=output.partition('\n\t')[2].partition(' ')[0]+' '
	return pre_libc
	
	
def patch(): 
	os.system(set_ld)
	os.system(set_libc)
	os.system("ldd main")
	
def get_path():
	global set_ld,set_libc
	working_path="/extra-libc/libc-"+version_string+"-"+str(bit)+"bit/"
	set_ld="patchelf --set-interpreter "+working_path+"ld-"+version_string+".so main"
	if (local==1): working_path=os.getcwd()+'/'
	set_libc="patchelf --replace-needed "+pre_libc+working_path+"libc-"+version_string+".so main"
	
def judge_bits():
	process=os.popen("file main")
	output=process.read()
	process.close()
	if (output[10]=="6"): return 64
	else: return 32

pre_libc=get_pre_libc()
bit=judge_bits()

print ("which mode would you choose?")
print ("1.local-mode\n2.global-mode")
local=input("choice:")

version=get_version()
if (version==1): version_string="2.23"
if (version==2): version_string="2.27"
if (version==3): version_string="2.29"
if (version==4): version_string="2.30"

get_path()
patch()


