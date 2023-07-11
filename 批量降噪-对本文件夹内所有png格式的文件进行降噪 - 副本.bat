@echo off
chcp 65001 > nul

REM 获取当前目录下的所有 png 文件
for %%I in (*.png) do (
    REM 检查文件名中是否包含 "-over"，如果包含则跳过
    echo %%~nI | findstr /C:"-over" > nul
    if errorlevel 1 (
        REM 运行降噪功能
        python clean.py "%%~dpnxI"
    )
)

echo 降噪完成！
pause
