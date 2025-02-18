@echo off
echo Moving all log files to the log folder...

REM Check if the log folder exists, if not, create it
if not exist "log" (
    mkdir log
)

REM Move all .log files to the log folder
move *.json log\ >nul

echo Move completed.
pause