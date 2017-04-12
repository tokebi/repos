@echo off
set PATH=%PATH%;D:\eclipse4.6\python\3;D:\pleiades-e4.4-python-jre_20130625\pleiades\python\3

set foldername=%date:~0,4%%date:~5,2%%date:~8,2%

REM カレントディレクトリの保存
set CurDir=%~d0%~p0
IF EXIST "C:\Users\hhara\OneDrive\SWProxy-windows" (
	cd C:\Users\hhara\OneDrive\SWProxy-windows
)
IF EXIST "C:\Users\tokebi\OneDrive\SWProxy-windows" (
	cd C:\Users\tokebi\OneDrive\SWProxy-windows
)

REM ファイル・フォルダ存在チェック
IF EXIST "819205.json" ( 
	if NOT EXIST "%foldername%" (
		mkdir %foldername%
	)
	move 819205* %foldername%
	copy %foldername%\819205-swarfarm.json .
)

cd %CurDir%
python.exe sw.py

REM emeditor monster.tsv runes.tsv skill.tsv
REM emeditor monster.tsv runes.tsv

IF EXIST "C:\Users\hhara\OneDrive\SWProxy-windows" (
	C:\Users\hhara\OneDrive\test.xlsx
)
IF EXIST "C:\Users\tokebi\OneDrive\SWProxy-windows" (
	C:\Users\tokebi\OneDrive\test.xlsx
)

pause
