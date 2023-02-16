cd /d %~dp0
set deviceid=%1%
set aabfilePath=%2%
set Path=%Path%;../platform-tools
echo %aabfilePath%

call :GetAABName %aabfilePath%
echo %aabName%

set aabfile=%aabfilePath%
set apksfile=./apksfiles/%aabName%.apks
set javatool=java\jre1.8.0_251\bin\java

if not exist apksfiles (
   md apksfiles
) else (
	echo %aabName%
)

if exist %apksfile% (
echo install app
%javatool% -jar bundletool-all-1.2.0.jar install-apks --device-id %deviceid% --apks %apksfile%
) else (
echo build apks
::%javatool% -jar bundletool-all-1.2.0.jar build-apks --local-testing --bundle %aabfile% --output %apksfile% --ks 20201009.keystore --ks-pass pass:123456 --ks-key-alias 20201009 --key-pass pass:123456
%javatool% -jar bundletool-all-1.2.0.jar build-apks --local-testing --bundle %aabfile% --output %apksfile% --ks ltyjfbtw.keystore --ks-pass pass:qslwsy1874 --ks-key-alias ltyjfbtw --key-pass pass:qslwsy1874
echo install app
%javatool% -jar bundletool-all-1.2.0.jar install-apks --device-id %deviceid% --apks %apksfile%
)

echo intasll finish!!!!!

::exit

:GetAABName
set aabName=%~n1