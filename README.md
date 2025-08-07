# PDF转换工具

这是一个用于将PDF文件转换为Markdown格式的工具，使用AI模型进行图像识别和文本提取。

## 项目结构

```
PDFConverter/
├── config/                # 配置文件目录
│   └── models_config.json # 模型配置
├── gptpdf/               # PDF解析核心模块
│   ├── __init__.py       # 模块初始化
│   └── parse.py          # PDF解析实现
├── services/             # 服务模块
│   ├── model_manager.py  # 模型管理器
│   └── pdf_converter.py  # PDF转换服务
├── outputs/              # 输出目录
├── uploads/              # 上传目录
├── convert_pdf.py        # 示例脚本
├── requirements.txt      # 依赖列表
└── README.md             # 说明文档
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 命令行使用

```bash
python convert_pdf.py <pdf文件路径>
```

例如：

```bash
python convert_pdf.py ./uploads/example.pdf
```

### 在代码中使用

```python
from services.model_manager import LangChainModelManager
from services.pdf_converter import PDFConverter

# 初始化
model_manager = LangChainModelManager()
pdf_converter = PDFConverter(model_manager)

# 转换单个PDF
markdown_content = pdf_converter.convert_to_markdown('path/to/your.pdf')

# 保存结果
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)
```

## 配置模型

在 `config/models_config.json` 文件中配置AI模型参数：

- 支持多种模型提供商
- 可配置不同任务使用不同模型
- 可设置模型参数如温度、最大token等

## 注意事项

- 确保PDF文件可读且格式良好
- 转换大型PDF文件可能需要较长时间
- 转换结果的质量取决于所使用的AI模型
- 首次运行时会在outputs目录生成中间图像文件