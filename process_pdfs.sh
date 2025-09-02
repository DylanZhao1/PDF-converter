#!/bin/bash

# 批量处理PDF文件的脚本
# 用法: ./process_pdfs.sh

# 设置PDF文件夹路径
PDF_FOLDER="D:\Research\LOUDONG\PDF"

# 检查文件夹是否存在
if [ ! -d "$PDF_FOLDER" ]; then
  echo "错误: 文件夹 '$PDF_FOLDER' 不存在"
  exit 1
fi

# 检查文件夹中是否有PDF文件
PDF_COUNT=$(find "$PDF_FOLDER" -name "*.pdf" | wc -l)
if [ "$PDF_COUNT" -eq 0 ]; then
  echo "错误: 在 '$PDF_FOLDER' 中没有找到PDF文件"
  exit 1
fi

echo "找到 $PDF_COUNT 个PDF文件，开始处理..."
echo ""

# 遍历文件夹中的所有PDF文件并处理
find "$PDF_FOLDER" -name "*.pdf" | while read pdf_file; do
  echo "处理文件: $(basename "$pdf_file")"
  python convert_pdf.py "$pdf_file"
  echo "------------------------"
done

echo ""
echo "所有PDF文件处理完成！"