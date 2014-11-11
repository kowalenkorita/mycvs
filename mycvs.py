import os
import sys
import shutil
PATH = os.getcwd().replace('\\', '/')

log = open('C:/Users/Рита/Documents/log.txt', 'w')
command = sys.argv[1]
log.write('started\n')

if command == 'init':
    os.mkdir('mycvs')
    a = open('mycvs/.version', 'w')
    a.write('0')
    a.close()
    open('mycvs/main.py', 'w').close()

if command == "commit":
	last_version = int(open('mycvs/.version', 'r').read())
	last_version = int(last_version) + 1
	os.mkdir('mycvs/v' + str(last_version))
	shutil.copyfile(PATH + '/main.py', PATH + '/mycvs/v' + str(last_version) + '/main.py')
	open('mycvs/.version', 'w').write(str(last_version))

if command == "checkout":
	version = int(sys.argv[2][1:])
	last_version = int(open('mycvs/.version', 'r').read())
	if version > last_version:
		print('There is not this version. Last version is', last_version)
	else:
		shutil.copyfile(PATH + '/mycvs/v' + str(version) + '/main.py', PATH + '/main.py')


log.write('finished')
log.close()