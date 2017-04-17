@echo off
set PATH=%PATH%;D:\eclipse4.6\python\3;D:\pleiades-e4.4-python-jre_20130625\pleiades\python\3

REM カレントディレクトリの保存
set CurDir=%~d0%~p0

cd %CurDir%
python.exe convert.py

python.exe convertMonster.py

sw.bat
