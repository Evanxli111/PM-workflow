# -*- coding: utf-8 -*-
"""
创建符合 Word文档格式规范标准V1.0.md 的 Word 模板文件
运行: python create_template.py
"""

from docx import Document
from docx.shared import Pt, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_cell_border(cell, **kwargs):
    """设置单元格边框"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ['top', 'left', 'bottom', 'right']:
        if edge in kwargs:
            tag = 'w:{}'.format(edge)
            element = OxmlElement(tag)
            element.set(qn('w:val'), kwargs[edge].get('val', 'single'))
            element.set(qn('w:sz'), kwargs[edge].get('sz', '4'))
            element.set(qn('w:color'), kwargs[edge].get('color', '000000'))
            tcBorders.append(element)
    tcPr.append(tcBorders)

def set_table_borders(table):
    """为表格设置边框"""
    for row in table.rows:
        for cell in row.cells:
            set_cell_border(
                cell,
                top={"val": "single", "sz": "6", "color": "000000"},
                bottom={"val": "single", "sz": "6", "color": "000000"},
                left={"val": "single", "sz": "6", "color": "000000"},
                right={"val": "single", "sz": "6", "color": "000000"}
            )

def create_template():
    """创建 Word 模板文件"""
    doc = Document()

    # 页面设置：A4，纵向，边距
    section = doc.sections[0]
    section.page_height = Cm(29.7)
    section.page_width = Cm(21)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2)
    section.right_margin = Cm(2)
    section.header_distance = Cm(1.5)

    # ============ 定义样式 ============

    # 1. 标题 1 样式（一级标题）
    style = doc.styles['Heading 1']
    style.font.name = '宋体'
    style._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    style.font.size = Pt(16)
    style.font.bold = True
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    style.paragraph_format.space_before = Pt(12)
    style.paragraph_format.space_after = Pt(6)

    # 2. 标题 2 样式（二级标题）
    style = doc.styles['Heading 2']
    style.font.name = '宋体'
    style._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    style.font.size = Pt(14)
    style.font.bold = True
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    style.paragraph_format.space_before = Pt(8)
    style.paragraph_format.space_after = Pt(4)

    # 3. 标题 3 样式（三级标题）
    style = doc.styles['Heading 3']
    style.font.name = '宋体'
    style._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    style.font.size = Pt(12)
    style.font.bold = True
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    style.paragraph_format.space_before = Pt(6)
    style.paragraph_format.space_after = Pt(3)

    # 4. 正文样式
    style = doc.styles['Normal']
    style.font.name = '宋体'
    style._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    style.paragraph_format.first_line_indent = Cm(0.74)  # 首行缩进2字符
    style.paragraph_format.left_indent = Cm(0)

    # ============ 创建示例内容 ============

    # 文档标题
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run('文档标题')
    run.font.name = '宋体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run.font.size = Pt(22)
    run.font.bold = True
    title.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE

    # 一级标题
    doc.add_heading('一、文档前言', level=1)

    # 二级标题
    doc.add_heading('1.1 文档目的', level=2)

    # 正文
    p = doc.add_paragraph('本文档用于说明系统功能需求和使用方法。')
    p.paragraph_format.first_line_indent = Cm(0.74)

    # 有序列表示例
    p = doc.add_paragraph()
    p.add_run('1. 这是有序列表第一项')
    p2 = doc.add_paragraph()
    p2.add_run('2. 这是有序列表第二项')

    # 无序列表示例
    p = doc.add_paragraph()
    run = p.add_run('● ')
    run.font.name = '宋体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    p.add_run('这是无序列表第一项')

    p = doc.add_paragraph()
    run = p.add_run('● ')
    run.font.name = '宋体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    p.add_run('这是无序列表第二项')

    # 表格示例
    doc.add_heading('1.2 表格示例', level=2)
    table = doc.add_table(rows=3, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)

    # 表头
    header_cells = table.rows[0].cells
    for i, text in enumerate(['列1', '列2', '列3']):
        header_cells[i].text = text
        for paragraph in header_cells[i].paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.bold = True
                run.font.size = Pt(12)

    # 数据行
    for row_idx in range(1, 3):
        row_cells = table.rows[row_idx].cells
        for i, text in enumerate([f'数据{row_idx}-{i+1}' for i in range(3)]):
            row_cells[i].text = text

    # 说明文字
    doc.add_paragraph()

    # 嵌套列表示例
    doc.add_heading('1.3 嵌套列表示例', level=2)
    p = doc.add_paragraph()
    p.add_run('1. 一级列表')
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.74)
    p.add_run('① 二级列表项A')
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.74)
    p.add_run('② 二级列表项B')

    # 保存
    output_path = 'Word文档模板.docx'
    doc.save(output_path)
    print(f'模板文件已创建: {output_path}')
    print('\n模板包含以下样式:')
    print('- 标题 1: 宋体, 三号, 加粗')
    print('- 标题 2: 宋体, 四号, 加粗')
    print('- 标题 3: 宋体, 小四, 加粗')
    print('- 正文: 宋体, 小四, 1.5倍行距, 首行缩进')
    print('- 表格: 带边框, 表头居中加粗')

if __name__ == '__main__':
    create_template()
