import os
import sys
import logging
from services.pdf_converter import PDFConverter
from services.model_manager import LangChainModelManager

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def convert_pdf_to_markdown(pdf_path):
    """将PDF文件转换为Markdown格式
    
    Args:
        pdf_path: PDF文件路径
        
    Returns:
        转换后的Markdown内容
    """
    try:
        # 初始化模型管理器和PDF转换器
        model_manager = LangChainModelManager()
        pdf_converter = PDFConverter(model_manager)
        
        # 转换PDF为Markdown
        logger.info(f"正在转换PDF: {pdf_path}")
        markdown_content = pdf_converter.convert_to_markdown(pdf_path)
        
        # 保存Markdown文件
        output_dir = './outputs'
        os.makedirs(output_dir, exist_ok=True)
        
        base_name = os.path.basename(pdf_path).split('.')[0]
        markdown_filename = f"{base_name}_converted.md"
        markdown_path = os.path.join(output_dir, markdown_filename)
        
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"转换成功，保存为: {markdown_path}")
        return markdown_content, markdown_path
        
    except Exception as e:
        logger.error(f"转换PDF时出错: {str(e)}")
        return None, None

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("使用方法: python convert_pdf.py <pdf文件路径>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误: 文件 '{pdf_path}' 不存在")
        sys.exit(1)
    
    # 检查文件是否为PDF
    if not pdf_path.lower().endswith('.pdf'):
        print("错误: 只支持PDF文件")
        sys.exit(1)
    
    # 转换PDF
    markdown_content, markdown_path = convert_pdf_to_markdown(pdf_path)
    
    if markdown_content:
        print(f"\nPDF转换成功! 结果保存在: {markdown_path}\n")
        print("Markdown内容预览:")
        print("=" * 50)
        print(markdown_content[:500] + "..." if len(markdown_content) > 500 else markdown_content)
        print("=" * 50)
    else:
        print("PDF转换失败")