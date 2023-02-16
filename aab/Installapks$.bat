cd /d %~dp0
set deviceid=%1%
set aabfilePath=%2%
echo %aabfilePath%
adb -s %deviceid% install %aabfilePath%
pause