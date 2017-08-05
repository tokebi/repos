@echo off
set PATH=%PATH%;D:\eclipse4.6\python\3;D:\pleiades-e4.4-python-jre_20130625\pleiades\python\3

set foldername=%date:~0,4%%date:~5,2%%date:~8,2%

REM カレントディレクトリの保存
set CurDir=%~d0%~p0
IF EXIST "C:\Users\hhara\OneDrive\SWProxy-windows" (
	SET SWPROXY_DIR=C:\Users\hhara\OneDrive\SWProxy-windows\
)
IF EXIST "C:\Users\tokebi\OneDrive\SWProxy-windows" (
	SET SWPROXY_DIR=C:\Users\tokebi\OneDrive\SWProxy-windows\
)
cd %SWPROXY_DIR%

REM ファイル・フォルダ存在チェック
IF EXIST "819205.json" ( 
	if NOT EXIST "%foldername%" (
		mkdir %foldername%
	)
	move 819205* %foldername%
	copy %foldername%\819205-swarfarm.json .
)

IF EXIST "2263709.json" ( 
	if NOT EXIST "%foldername%" (
		mkdir %foldername%
	)
	move 2263709* %foldername%
	copy %foldername%\2263709-swarfarm.json .
)

IF EXIST "819205-swarfarm.json" ( 
	cd %CurDir%
	python.exe sw.py 819205
)
cd %SWPROXY_DIR%
IF EXIST "2263709-swarfarm.json" ( 
	cd %CurDir%
	python.exe sw.py 2263709
)

if not %ERRORLEVEL% == 0 (
   pause
   exit /b 1
)

IF EXIST "C:\Users\hhara\OneDrive\SWProxy-windows" (
	start C:\Users\hhara\OneDrive\test819205.xlsx
	start C:\Users\hhara\OneDrive\test2263709.xlsx
)
IF EXIST "C:\Users\tokebi\OneDrive\SWProxy-windows" (
	start C:\Users\tokebi\OneDrive\test819205.xlsx
	start C:\Users\tokebi\OneDrive\test2263709.xlsx
)

REM pause
