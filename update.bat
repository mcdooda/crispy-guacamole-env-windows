cd crispy-guacamole
git pull origin master
cd flat-engine
git pull origin master
cd ../..
rm -r project
mkdir project
cd project
cmake .. -G "Visual Studio 14 2015 Win64"
cd ..
devenv project/crispy-guacamole.sln /build Debug /project project/crispy-guacamole.vcxproj /projectconfig Debug
cp ./dll/* ./project/Debug
echo READY
pause