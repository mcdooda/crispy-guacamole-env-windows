rmdir /s /q .\project
mkdir project\Debug
mkdir project\Release
mkdir project\RelWithDebInfo
cd project
cmake .. -G "Visual Studio 14 2015 Win64"
cd ..
copy .\dll\* .\project\Debug
copy .\dll\* .\project\Release
copy .\dll\* .\project\RelWithDebInfo
copy .\crispy-guacamole.vcxproj.user .\project
pause