rmdir /s /q .\project
mkdir project\Debug
mkdir project\Release
mkdir project\RelWithDebInfo
cd project
cmake ..
cd ..
copy .\dll\* .\project\Debug
copy .\dll\* .\project\Release
copy .\dll\* .\project\RelWithDebInfo
copy .\crispy-guacamole.vcxproj.user .\project
pause