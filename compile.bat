@echo off
title Compilation
echo Compilation...
pyinstaller blackscreen.spec --noconfirm
echo Installer...
iscc compilation.iss
echo Termine !
pause