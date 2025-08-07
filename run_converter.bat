@echo off
echo PDF转换工具启动中...
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
echo 选择操作:
echo 1. 转换单个PDF文件
echo 2. 运行测试
echo 3. 退出
echo.

set /p choice=请输入选项 (1-3): 

if "%choice%"=="1" (
    echo.
    set /p pdf_path=请输入PDF文件路径: 
    python convert_pdf.py "%pdf_path%"
) else if "%choice%"=="2" (
    echo.
    echo 运行测试...
    python test_converter.py
) else if "%choice%"=="3" (
    echo 退出程序
    exit /b 0
) else (
    echo 无效选项，请重新运行
)

echo.
echo 操作完成
pause