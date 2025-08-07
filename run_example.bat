@echo off
echo 正在启动PDF转换示例...
echo 将使用固定路径: D://Research//LOUDONG//ssrn-4433510.pdf
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未检测到Python，请安装Python 3.8或更高版本
    pause
    exit /b 1
)

REM 检查是否已安装依赖
echo 检查依赖...
pip show langchain >nul 2>&1
if %errorlevel% neq 0 (
    echo 首次运行，正在安装依赖...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo 依赖安装失败，请手动运行: pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo 依赖安装完成
)

echo.
echo 开始运行示例代码...
python example_usage.py

echo.
echo 操作完成
pause