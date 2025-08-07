import os
import sys
import shutil
from services.pdf_converter import PDFConverter
from services.model_manager import LangChainModelManager

def test_pdf_converter():
    """测试PDF转换功能"""
    print("\n===== 测试PDF转换功能 =====\n")
    
    # 检查是否有测试PDF文件
    test_pdf = None
    
    # 检查uploads目录
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # 检查是否有PDF文件在uploads目录
    pdf_files = [f for f in os.listdir('uploads') if f.lower().endswith('.pdf')]
    
    if pdf_files:
        test_pdf = os.path.join('uploads', pdf_files[0])
        print(f"找到测试PDF文件: {test_pdf}")
    else:
        # 检查上级目录是否有PDF文件
        parent_dir = os.path.dirname(os.path.abspath('.'))
        for root, dirs, files in os.walk(parent_dir):
            for file in files:
                if file.lower().endswith('.pdf'):
                    source_pdf = os.path.join(root, file)
                    test_pdf = os.path.join('uploads', file)
                    print(f"从 {source_pdf} 复制PDF文件到 {test_pdf}")
                    shutil.copy2(source_pdf, test_pdf)
                    break
            if test_pdf:
                break
    
    if not test_pdf:
        print("错误: 未找到任何PDF文件进行测试")
        print("请将PDF文件放入 'uploads' 目录后重试")
        return False
    
    try:
        # 初始化模型管理器和PDF转换器
        model_manager = LangChainModelManager()
        pdf_converter = PDFConverter(model_manager)
        
        # 转换PDF为Markdown
        print(f"\n开始转换PDF: {test_pdf}")
        markdown_content = pdf_converter.convert_to_markdown(test_pdf)
        
        # 保存Markdown文件
        output_dir = './outputs'
        os.makedirs(output_dir, exist_ok=True)
        
        base_name = os.path.basename(test_pdf).split('.')[0]
        markdown_filename = f"{base_name}_test_converted.md"
        markdown_path = os.path.join(output_dir, markdown_filename)
        
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\n转换成功! 结果保存在: {markdown_path}")
        print("\nMarkdown内容预览:")
        print("=" * 50)
        preview = markdown_content[:500] + "..." if len(markdown_content) > 500 else markdown_content
        print(preview)
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"\n转换过程中出错: {str(e)}")
        return False

if __name__ == "__main__":
    test_pdf_converter()