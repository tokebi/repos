@echo off
set PATH=%PATH%;D:\eclipse4.6\python\3;D:\pleiades-e4.4-python-jre_20130625\pleiades\python\3

set foldername=%date:~0,4%%date:~5,2%%date:~8,2%

REM �J�����g�f�B���N�g���̕ۑ�
set CurDir=%~d0%~p0
IF EXIST "C:\Users\hhara\OneDrive\SWProxy-windows" (
	SET SWPROXY_DIR=C:\Users\hhara\OneDrive\SWProxy-windows\
)
IF EXIST "C:\Users\tokebi\OneDrive\SWProxy-windows" (
	SET SWPROXY_DIR=C:\Users\tokebi\OneDrive\SWProxy-windows\
)
cd %SWPROXY_DIR%

REM �t�@�C���E�t�H���_���݃`�F�b�N
IF EXIST "819205.json" ( 
	echo �t�@�C���ړ��J�n(���C��)
	if NOT EXIST "%foldername%" (
		mkdir %foldername%
	)
	move 819205* %foldername%
	copy %foldername%\819205-swarfarm.json .
	echo �t�@�C���ړ��I��(���C��)
)

IF EXIST "2263709.json" ( 
	echo �t�@�C���ړ��J�n(�T�u)
	if NOT EXIST "%foldername%" (
		mkdir %foldername%
	)
	move 2263709* %foldername%
	copy %foldername%\2263709-swarfarm.json .
	echo �t�@�C���ړ��I��(�T�u)
)

IF EXIST "819205-swarfarm.json" ( 
	echo ��͊J�n(���C��)
	cd %CurDir%
	python.exe sw.py 819205
	echo ��͏I��(���C��)
)
cd %SWPROXY_DIR%
IF EXIST "2263709-swarfarm.json" ( 
	echo ��͊J�n(�T�u)
	cd %CurDir%
	python.exe sw.py 2263709
	echo ��͏I��(�T�u)
)

if not %ERRORLEVEL% == 0 (
   pause
   exit /b 1
)

IF EXIST "C:\Users\hhara\OneDrive\SWProxy-windows" (
	echo EXCEL�J��
	start C:\Users\hhara\OneDrive\test819205.xlsx
	start C:\Users\hhara\OneDrive\test2263709.xlsx
)
IF EXIST "C:\Users\tokebi\OneDrive\SWProxy-windows" (
	echo EXCEL�J��
	start C:\Users\tokebi\OneDrive\test819205.xlsx
	start C:\Users\tokebi\OneDrive\test2263709.xlsx
)

REM pause
