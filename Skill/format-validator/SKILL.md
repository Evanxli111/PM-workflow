---
name: format-validator
description: "自动检查文档格式是否符合标准规范"
description_zh: "格式验证器 - 自动检查Word文档格式规范"
description_en: "Format Validator - Automatically check Word document format compliance"
version: 1.0.0
license: MIT
---

# Format Validator

## 概述
本技能用于自动检查Word文档的格式是否符合公司标准规范，包括字体、字号、间距、对齐方式、列表格式、表格规范等，确保文档质量一致性。

## 适用场景
- PRD文档格式检查
- 操作手册格式验证
- 合同文档格式审核
- 规范文档合规检查

## 核心功能

### 1. 字体格式检查
- 字体名称验证
- 字号大小检查
- 加粗/斜体规范
- 中英文字体混用检测

### 2. 间距规范检查
- 行距一致性
- 段落间距
- 首行缩进
- 段前段后距离

### 3. 对齐方式检查
- 标题对齐规范
- 正文对齐方式
- 表格对齐规则
- 图片对齐位置

### 4. 列表格式检查
- 有序列表编号
- 无序列表符号
- 嵌套列表层级
- 列表缩进规范

### 5. 表格格式检查
- 边框样式规范
- 列宽比例检查
- 表头格式验证
- 单元格对齐

### 6. 页面设置检查
- 页边距规范
- 纸张大小
- 页眉页脚
- 页码格式

## 使用方法

### 基本调用
```
/format-validator <document_file>
```

### 详细配置
```
/format-validator
  --document operation-manual.docx
  --standard corporate
  --report format-report.json
  --fix-mode auto
```

### 参数说明
- `--document`: 文档路径（必需）
- `--standard`: 规范标准（corporate/standard/custom）
- `--report`: 检查报告输出路径
- `--fix-mode`: 修复模式（auto/manual/none）
- `--verbose`: 详细输出模式

## 检查规则

### 字体规范
```json
{
  "font_rules": {
    "title": {
      "font_name": "宋体",
      "font_size": 22,
      "bold": true,
      "alignment": "center"
    },
    "heading_1": {
      "font_name": "宋体",
      "font_size": 16,
      "bold": true,
      "alignment": "left"
    },
    "heading_2": {
      "font_name": "宋体",
      "font_size": 14,
      "bold": true,
      "alignment": "left"
    },
    "heading_3": {
      "font_name": "宋体",
      "font_size": 12,
      "bold": true,
      "alignment": "left"
    },
    "body": {
      "font_name": "宋体",
      "font_size": 12,
      "bold": false,
      "first_line_indent": 24
    }
  }
}
```

### 间距规范
```json
{
  "spacing_rules": {
    "line_spacing": 1.5,
    "paragraph_spacing_before": 0,
    "paragraph_spacing_after": 0,
    "first_line_indent": 24,
    "heading_spacing": {
      "title_to_content": 2.0,
      "h1_to_h2": 1.0,
      "h2_to_h3": 0.5,
      "content_to_content": 0.5
    }
  }
}
```

### 列表规范
```json
{
  "list_rules": {
    "ordered_list": {
      "format": "1. 2. 3.",
      "separator": "、",
      "indent": 0,
      "hanging_indent": 0
    },
    "unordered_list": {
      "symbol": "●",
      "indent": 0,
      "hanging_indent": 0
    },
    "nested_list": {
      "level_1": "① ② ③",
      "level_2": "■",
      "indent_increment": 24
    }
  }
}
```

### 表格规范
```json
{
  "table_rules": {
    "border_style": "single",
    "header_format": {
      "bold": true,
      "font_size": 12,
      "alignment": "center"
    },
    "cell_format": {
      "font_size": 12,
      "alignment": "left",
      "vertical_alignment": "center"
    },
    "cell_padding": {
      "top": 60,
      "bottom": 60,
      "left": 100,
      "right": 100
    }
  }
}
```

### 页面规范
```json
{
  "page_rules": {
    "paper_size": "A4",
    "orientation": "portrait",
    "margins": {
      "top": 25,
      "bottom": 25,
      "left": 20,
      "right": 20
    },
    "page_number": {
      "position": "bottom_center",
      "font_size": 12,
      "font_name": "宋体",
      "start_from": "一、文档前言"
    },
    "header": {
      "content": "文档标题",
      "position": "top_center",
      "font_size": 12
    }
  }
}
```

## 检查报告格式

### JSON格式报告
```json
{
  "document": "operation-manual.docx",
  "check_time": "2025-04-09 15:30:00",
  "overall_status": "PASS",
  "summary": {
    "total_issues": 5,
    "critical": 0,
    "major": 2,
    "minor": 3
  },
  "details": [
    {
      "category": "字体",
      "issue": "正文使用了Times New Roman字体",
      "location": "第3段",
      "severity": "major",
      "suggestion": "应使用宋体",
      "auto_fixable": true
    },
    {
      "category": "间距",
      "issue": "行距为1.0，应为1.5",
      "location": "第5-8段",
      "severity": "minor",
      "suggestion": "将行距调整为1.5倍",
      "auto_fixable": true
    }
  ],
  "statistics": {
    "total_paragraphs": 156,
    "total_tables": 8,
    "total_images": 12,
    "total_lists": 24
  }
}
```

### HTML格式报告
生成带有颜色标注的可视化报告，方便定位和修改问题。

## 自动修复功能

### 可自动修复的问题
- 字体名称统一
- 行距调整
- 首行缩进设置
- 列表符号规范化
- 表格边框修复

### 需要手动处理的问题
- 内容逻辑错误
- 表格结构问题
- 图片位置调整
- 跨页断行处理

### 修复命令
```bash
# 自动修复所有可修复问题
/format-validator --document test.docx --fix-mode auto

# 预览修复建议（不执行）
/format-validator --document test.docx --fix-mode manual

# 仅生成报告
/format-validator --document test.docx --fix-mode none
```

## 工作流程

### 1. 文档加载
- 解析Word文档结构
- 提取所有段落和样式
- 扫描表格和列表
- 识别图片和对象

### 2. 执行检查
- 逐项应用检查规则
- 记录发现的问题
- 评估问题严重程度
- 生成问题清单

### 3. 生成报告
- 汇总检查结果
- 分类整理问题
- 提供修复建议
- 生成统计信息

### 4. 自动修复（如需要）
- 识别可修复项
- 批量应用修复
- 验证修复效果
- 生成修复日志

## 检查清单

### 必检项
- [ ] 字体名称一致性
- [ ] 字号大小规范性
- [ ] 行距设置正确性
- [ ] 首行缩进规范性
- [ ] 标题层级清晰性
- [ ] 列表格式规范性
- [ ] 表格格式正确性
- [ ] 页边距设置
- [ ] 页码连续性

### 建议检项
- [ ] 英文大小写规范
- [ ] 标点符号使用
- [ ] 数字格式统一
- [ ] 专业术语一致性
- [ ] 截图表注规范

## 与其他技能集成

### 输入来源
- **operation-manual-generator**: 操作手册生成
- **prd-generator**: PRD文档生成

### 质量门禁
可作为文档发布的质量门禁，确保所有生成的文档符合规范。

## 质量指标

### 合格率标准
- 关键项合格率：100%
- 重要项合格率：≥95%
- 一般项合格率：≥90%
- 整体合规率：≥95%

### 检查覆盖率
- 字体检查：100%
- 间距检查：100%
- 列表检查：100%
- 表格检查：100%
- 页面检查：100%

## 技术实现

### 工具选择
- python-docx：Word文档解析
- lxml：XML结构处理
- 正则表达式：文本模式匹配
- Pandas：数据统计

### 性能优化
- 并行处理多文档
- 增量检查（仅变更部分）
- 结果缓存机制
- 批量检查支持