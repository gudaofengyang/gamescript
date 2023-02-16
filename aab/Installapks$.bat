cd /d %~dp0
set deviceid=%1%
set aabfilePath=%2%
set Path=%Path%;../platform-tools
echo %aabfilePath%
adb -s %deviceid% install %aabfilePath%
exit
