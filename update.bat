cd crispy-guacamole
git stash
git pull origin master
git stash pop
cd flat-engine
git stash
git pull origin master
git stash pop
cd ../..
rm -r project
mkdir project
cd project
cmake .. -G "Visual Studio 14 2015 Win64"
cd ..
devenv project/crispy-guacamole.sln /build Debug /project project/crispy-guacamole.vcxproj /projectconfig Debug
copy .\dll\* .\project\Debug
echo READY
pause