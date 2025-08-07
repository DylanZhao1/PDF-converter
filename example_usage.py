import os
from services.pdf_converter import PDFConverter
from services.model_manager import LangChainModelManager

def convert_specific_pdf():
    """
    直接调用PDF转换功能，使用指定的PDF文件路径
    """
    # 指定PDF文件路径
    pdf_path = "D:\\Research\\LOUDONG\\ssrn-4433510.pdf"
    
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误: 文件 '{pdf_path}' 不存在")
        return
    
    try:
        # 初始化模型管理器和PDF转换器
        model_manager = LangChainModelManager()
        pdf_converter = PDFConverter(model_manager)
        
        # 转换PDF为Markdown
        print(f"开始转换PDF: {pdf_path}")
        markdown_content = pdf_converter.convert_to_markdown(pdf_path)
        
        # 保存Markdown文件
        output_dir = './outputs'
        os.makedirs(output_dir, exist_ok=True)
        
        markdown_filename = "ssrn-4433510_converted.md"
        markdown_path = os.path.join(output_dir, markdown_filename)
        
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\n转换成功! 结果保存在: {markdown_path}")
        print("\nMarkdown内容预览:")
        print("=" * 50)
        preview = markdown_content[:500] + "..." if len(markdown_content) > 500 else markdown_content
        print(preview)
        print("=" * 50)
        
    except Exception as e:
        print(f"转换过程中出错: {str(e)}")

if __name__ == "__main__":
    convert_specific_pdf()