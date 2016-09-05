import subprocess

import os
import shutil
import sys

flagErrorPull = False
print('\n')
sys.stdout.write("%s" % ("|" * 60))
sys.stdout.flush()
sys.stdout.write("\b" * (60+1)) # return to start of line, after '['

def printProgress (n=60, msg="normal"):
    for x in range(n):
        sys.stdout.write("▒" if (msg == "normal") else "|")
        sys.stdout.flush()


progress = 6
printProgress(6)
os.chdir('crispy-guacamole')
err1 = False
err2 = False
res = subprocess.Popen('git stash',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()
progress += 6
printProgress(6)

res = subprocess.Popen('git pull origin master',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()
if ('error' in err.decode('utf-8')):
    flagErrorPull = True
    err1 = err.decode('utf-8')


progress += 6
printProgress(6)

res = subprocess.Popen('git stash pop',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()

progress += 6
printProgress(6)
res = subprocess.Popen('git submodule update',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()

progress += 6
printProgress(6)
os.chdir('flat-engine')

res = subprocess.Popen('git stash',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()
progress += 6
printProgress(6)

res = subprocess.Popen('git pull origin master',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()
err2 = err.decode('utf-8')
progress += 6
printProgress(6)

if ('error' in err.decode('utf-8')):

    flagErrorPull = True

if (flagErrorPull):
    printProgress(60 - progress, "error")
    print('\n')
    res = subprocess.Popen('git status',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ( 'up-to-date' in out.decode('utf-8') ):
        print('flat-engine is up to date, checking root')
        os.chdir('..')
        res = subprocess.Popen('git status',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = res.communicate()
        print(err.decode('utf-8'))
    if (err1):
        print(err1)
    if (err2):
        print(err2)
    print('\n' + out.decode('utf-8'))
    sys.exit()



res = subprocess.Popen('git stash pop',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()

res = subprocess.Popen('git submodule update',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = res.communicate()


os.chdir('../..')
shutil.rmtree('./project')
os.makedirs('./project')
os.chdir('./project')

res = subprocess.Popen('cmake .. -G "Visual Studio 14 2015 Win64"',stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = res.communicate()

os.chdir('..')
try:
    res = subprocess.Popen('devenv project/crispy-guacamole.sln /build Debug /project project/crispy-guacamole.vcxproj /projectconfig Debug',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = res.communicate()

except:
    print('error visual')
    res = subprocess.Popen('devenv project/crispy-guacamole.sln',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = res.communicate()
    sys.exit()

src_files = os.listdir('.\dll')
for file_name in src_files:
    full_file_name = os.path.join('.\dll', file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copyfile(full_file_name, '.\project\Debug\\' + file_name)
