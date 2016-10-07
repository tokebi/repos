@echo off
set PATH=%PATH%;D:\eclipse4.6\python\3;D:\pleiades-e4.4-python-jre_20130625\pleiades\python\3

set foldername=%date:~0,4%%date:~5,2%%date:~8,2%

REM ファイル・フォルダ存在チェック
IF EXIST "819205.json" ( 
	if NOT EXIST "%foldername%" (
		mkdir %foldername%
	)
	move 819205* %foldername%
	copy %foldername%\819205-swarfarm.json .
)


python.exe sw.py

emeditor monster.tsv runes.tsv

pause
