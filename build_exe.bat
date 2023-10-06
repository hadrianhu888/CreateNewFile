@echo off
REM Batch Script to Create Installer Using PyInstaller on Windows

REM Step 1: Install PyInstaller (uncomment next line if you need to install it)
pip install pyinstaller

REM Step 2: Navigate to the directory containing your Python script.
cd /d %~dp0

REM Step 3: Compile the script into an executable
pyinstaller --onefile --windowed ./src/CreateNewFile.py --icon=./img/newfile.ico 

REM Step 4: Notify the user that the process is complete
echo.
echo Executable has been created and can be found in the "dist" directory.
pause
