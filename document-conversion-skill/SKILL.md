---
name: document-conversion-skill
description: Master document conversion between formats (PDF, DOCX, HTML, Markdown, EPUB). Use for: markdown to PDF with Thai fonts, HTML to PDF with WeasyPrint, DOCX conversion with Pandoc, encoding handling (UTF-8 BOM), font embedding, CSS styling for documents, batch conversion workflows, and production-quality document generation.
---

# 📄 Document Conversion Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [Conversion Fundamentals](#conversion-fundamentals)
2. [Markdown to PDF](#markdown-to-pdf)
3. [HTML to PDF](#html-to-pdf)
4. [DOCX Conversion](#docx-conversion)
5. [Thai Language Support](#thai-language-support)
6. [Encoding Handling](#encoding-handling)
7. [Font Embedding](#font-embedding)
8. [CSS for Print](#css-for-print)
9. [Batch Conversion](#batch-conversion)
10. [Troubleshooting](#troubleshooting)

---

## 🎯 Conversion Fundamentals

### Common Document Formats

**Source Formats:**
- Markdown (.md) - Lightweight markup
- HTML (.html) - Web documents
- DOCX (.docx) - Microsoft Word
- Plain Text (.txt)
- LaTeX (.tex)

**Target Formats:**
- PDF (.pdf) - Universal, print-ready
- DOCX (.docx) - Microsoft Word
- EPUB (.epub) - E-books
- HTML (.html) - Web

---

### Essential Tools

**WeasyPrint** (HTML → PDF)
```bash
# Install
pip install weasyprint

# Convert
python -m weasyprint input.html output.pdf
```

**Pandoc** (Universal converter)
```bash
# Install
sudo apt install pandoc  # Linux
brew install pandoc      # macOS

# Convert
pandoc input.md -o output.pdf
pandoc input.docx -o output.html
```

**Python Libraries:**
- `markdown` - MD to HTML
- `python-docx` - DOCX manipulation
- `PyPDF2` - PDF manipulation
- `reportlab` - PDF generation

---

## 📝 Markdown to PDF

### ⚠️ Critical: The Proven 3-Step Method

**❌ DON'T:**
```bash
# Direct conversion FAILS with Thai fonts!
pandoc input.md -o output.pdf  # ❌ Thai text invisible
```

**✅ DO: Use 3-Step Method**

```bash
# Step 1: Ensure UTF-8 BOM encoding
python scripts/ensure_utf8_bom.py input.md

# Step 2: Convert Markdown → HTML (with Thai fonts)
~/projects/.venv-docs/bin/python convert_md_to_html.py

# Step 3: Convert HTML → PDF
~/projects/.venv-docs/bin/python -m weasyprint output.html output.pdf
```

---

### Step 2: Markdown to HTML Converter

**convert_md_to_html.py:**
```python
#!/usr/bin/env python3
import markdown
from pathlib import Path

def md_to_html_with_thai_fonts(input_path, output_path):
    """
    Convert Markdown to HTML with Thai font support.
    """
    # Read markdown (UTF-8 with BOM)
    with open(input_path, 'r', encoding='utf-8-sig') as f:
        md_content = f.read()

    # Convert to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc', 'nl2br']
    )

    # Create full HTML with Thai fonts
    full_html = f'''<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Google Fonts for Thai -->
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap" rel="stylesheet">

    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}

        body {{
            font-family: 'Sarabun', 'Noto Sans Thai', sans-serif;
            line-height: 1.8;
            font-size: 14pt;
            color: #333;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Sarabun', sans-serif;
            font-weight: 700;
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }}

        h1 {{ font-size: 24pt; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }}
        h2 {{ font-size: 20pt; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.3em; }}
        h3 {{ font-size: 16pt; }}

        code {{
            font-family: 'Courier New', monospace;
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-size: 0.9em;
        }}

        pre {{
            background-color: #2d2d2d;
            color: #f8f8f2;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            line-height: 1.5;
        }}

        pre code {{
            background: none;
            padding: 0;
            color: inherit;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 8pt;
            text-align: left;
        }}

        th {{
            background-color: #3498db;
            color: white;
            font-weight: 700;
        }}

        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        blockquote {{
            border-left: 4px solid #3498db;
            margin: 1em 0;
            padding-left: 1em;
            font-style: italic;
            color: #555;
        }}

        ul, ol {{
            margin: 1em 0;
            padding-left: 2em;
        }}

        li {{
            margin: 0.5em 0;
        }}

        a {{
            color: #3498db;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        hr {{
            border: none;
            border-top: 2px solid #eee;
            margin: 2em 0;
        }}

        img {{
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>'''

    # Save HTML
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"✅ HTML created: {output_path}")

if __name__ == '__main__':
    import sys

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.md'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output.html'

    md_to_html_with_thai_fonts(input_file, output_file)
```

---

### Step 1: Ensure UTF-8 BOM Encoding

**scripts/ensure_utf8_bom.py:**
```python
#!/usr/bin/env python3
"""
Ensure file has UTF-8 BOM encoding (required for Thai fonts).
"""
import sys
from pathlib import Path

def ensure_utf8_bom(file_path):
    """Add UTF-8 BOM if not present."""
    file_path = Path(file_path)

    # Read current content
    with open(file_path, 'rb') as f:
        content = f.read()

    # Check if BOM exists
    BOM = b'\xef\xbb\xbf'
    if content.startswith(BOM):
        print(f"✅ {file_path.name} already has UTF-8 BOM")
        return

    # Add BOM
    with open(file_path, 'wb') as f:
        f.write(BOM + content)

    print(f"✅ Added UTF-8 BOM to {file_path.name}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ensure_utf8_bom.py <file>")
        sys.exit(1)

    ensure_utf8_bom(sys.argv[1])
```

---

### Complete Workflow (One-liner)

```bash
# Full conversion pipeline
python scripts/ensure_utf8_bom.py input.md && \
~/projects/.venv-docs/bin/python convert_md_to_html.py input.md output.html && \
~/projects/.venv-docs/bin/python -m weasyprint output.html output.pdf

# Verify result
ls -lh output.pdf
file output.pdf
```

---

## 🌐 HTML to PDF

### WeasyPrint (Recommended)

```python
from weasyprint import HTML, CSS

# Simple conversion
HTML('input.html').write_pdf('output.pdf')

# With custom CSS
thai_css = CSS(string='''
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');

    body {
        font-family: 'Sarabun', 'Noto Sans Thai', sans-serif !important;
        line-height: 1.8;
        font-size: 14pt;
    }

    h1, h2, h3 {
        font-family: 'Sarabun', sans-serif !important;
    }
''')

HTML('input.html').write_pdf('output.pdf', stylesheets=[thai_css])

# From URL
HTML('https://example.com').write_pdf('output.pdf')

# From string
html_string = '<h1>Hello</h1><p>Thai: สวัสดี</p>'
HTML(string=html_string).write_pdf('output.pdf', stylesheets=[thai_css])
```

---

### Advanced WeasyPrint Options

```python
from weasyprint import HTML, CSS

# Custom page size and margins
css = CSS(string='''
    @page {
        size: A4 landscape;
        margin: 1cm;

        @top-center {
            content: "Page " counter(page) " of " counter(pages);
        }
    }

    body {
        font-family: 'Sarabun', sans-serif;
    }
''')

HTML('input.html').write_pdf(
    'output.pdf',
    stylesheets=[css],
    presentational_hints=True  # Respect HTML attributes like width=""
)
```

---

## 📄 DOCX Conversion

### Pandoc (Markdown ↔ DOCX)

```bash
# Markdown → DOCX
pandoc input.md -o output.docx

# DOCX → Markdown
pandoc input.docx -o output.md

# With custom reference doc (styling)
pandoc input.md -o output.docx --reference-doc=template.docx

# DOCX → PDF (requires LibreOffice)
pandoc input.docx -o output.pdf
```

---

### Python-docx (Programmatic DOCX)

```python
from docx import Document
from docx.shared import Pt, Inches

# Create new document
doc = Document()

# Add heading
doc.add_heading('Document Title', 0)

# Add paragraph
p = doc.add_paragraph('This is a paragraph.')

# Customize paragraph
p_format = p.paragraph_format
p_format.line_spacing = 1.5
p_format.space_after = Pt(12)

# Add styled text
p = doc.add_paragraph()
run = p.add_run('Bold text')
run.bold = True
run.font.size = Pt(14)

# Add table
table = doc.add_table(rows=3, cols=3)
table.style = 'Table Grid'

# Populate table
for i in range(3):
    for j in range(3):
        table.cell(i, j).text = f'Cell {i},{j}'

# Add image
doc.add_picture('image.png', width=Inches(4))

# Save
doc.save('output.docx')
```

---

### Read DOCX Content

```python
from docx import Document

doc = Document('input.docx')

# Extract all paragraphs
for para in doc.paragraphs:
    print(para.text)

# Extract tables
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text, end='\t')
        print()

# Extract images
from docx.opc.constants import RELATIONSHIP_TYPE as RT

for rel in doc.part.rels.values():
    if RT.IMAGE in rel.reltype:
        image = rel.target_part.blob
        # Save image
        with open(f'image_{rel.rId}.png', 'wb') as f:
            f.write(image)
```

---

## 🇹🇭 Thai Language Support

### Key Points

**1. Font Requirements:**
- Use Thai-compatible fonts: Sarabun, Noto Sans Thai, TH Sarabun New
- Embed fonts in PDF (automatic with Google Fonts)

**2. Encoding:**
- Always use UTF-8 (with BOM for compatibility)
- Never use ASCII or Latin-1 encoding

**3. Line Breaking:**
- Thai has no spaces between words
- Use `word-break: break-word` in CSS
- WeasyPrint handles Thai line breaking automatically

---

### CSS for Thai Typography

```css
/* Thai font stack */
body {
    font-family: 'Sarabun', 'Noto Sans Thai', 'TH Sarabun New', sans-serif;
    line-height: 1.8;  /* Thai needs more line height */
    font-size: 14pt;   /* Slightly larger for readability */
}

/* Word breaking */
p {
    word-break: break-word;
    overflow-wrap: break-word;
}

/* Prevent orphans */
h1, h2, h3 {
    page-break-after: avoid;
}

p {
    orphans: 2;
    widows: 2;
}
```

---

### Google Fonts for Thai

```html
<!-- Sarabun (Recommended) -->
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;700&display=swap" rel="stylesheet">

<!-- Noto Sans Thai -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;700&display=swap" rel="stylesheet">

<!-- Prompt -->
<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;700&display=swap" rel="stylesheet">
```

---

## 🔤 Encoding Handling

### UTF-8 BOM

**What is BOM?**
- Byte Order Mark: `EF BB BF` (3 bytes)
- Signals UTF-8 encoding to legacy systems
- Required for some Thai font rendering

**Add BOM:**
```python
def add_bom(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    BOM = b'\xef\xbb\xbf'
    if not content.startswith(BOM):
        with open(file_path, 'wb') as f:
            f.write(BOM + content)
```

**Remove BOM:**
```python
def remove_bom(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    BOM = b'\xef\xbb\xbf'
    if content.startswith(BOM):
        with open(file_path, 'wb') as f:
            f.write(content[3:])
```

---

### Encoding Detection

```python
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw = f.read()

    result = chardet.detect(raw)
    encoding = result['encoding']
    confidence = result['confidence']

    print(f"Encoding: {encoding} (confidence: {confidence:.2%})")
    return encoding

# Usage
encoding = detect_encoding('input.txt')

# Read with detected encoding
with open('input.txt', 'r', encoding=encoding) as f:
    content = f.read()
```

---

### Convert Encoding

```python
def convert_encoding(input_path, output_path, from_enc, to_enc='utf-8'):
    """
    Convert file encoding.
    """
    with open(input_path, 'r', encoding=from_enc) as f:
        content = f.read()

    with open(output_path, 'w', encoding=to_enc) as f:
        f.write(content)

    print(f"✅ Converted {from_enc} → {to_enc}")

# Example
convert_encoding('input.txt', 'output.txt', from_enc='latin-1', to_enc='utf-8')
```

---

## 🎨 Font Embedding

### Google Fonts (Web Fonts)

**HTML Method:**
```html
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap" rel="stylesheet">

<style>
    body {
        font-family: 'Sarabun', sans-serif;
    }
</style>
```

**CSS @import:**
```css
@import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');

body {
    font-family: 'Sarabun', sans-serif;
}
```

---

### Local Font Files

**@font-face:**
```css
@font-face {
    font-family: 'Sarabun';
    src: url('fonts/Sarabun-Regular.ttf') format('truetype');
    font-weight: 400;
    font-style: normal;
}

@font-face {
    font-family: 'Sarabun';
    src: url('fonts/Sarabun-Bold.ttf') format('truetype');
    font-weight: 700;
    font-style: normal;
}

body {
    font-family: 'Sarabun', sans-serif;
}
```

---

### WeasyPrint Font Configuration

```python
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

font_config = FontConfiguration()

css = CSS(string='''
    @font-face {
        font-family: Sarabun;
        src: url(fonts/Sarabun-Regular.ttf);
    }
    body {
        font-family: Sarabun;
    }
''', font_config=font_config)

HTML('input.html').write_pdf(
    'output.pdf',
    stylesheets=[css],
    font_config=font_config
)
```

---

## 🖨️ CSS for Print

### Page Rules

```css
@page {
    size: A4;  /* A4, Letter, Legal, or custom (210mm 297mm) */
    margin: 2cm;

    /* Running headers/footers */
    @top-center {
        content: "Document Title";
        font-size: 10pt;
        color: #666;
    }

    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
    }
}

/* First page different */
@page :first {
    margin-top: 5cm;
}

/* Left/right pages (for book printing) */
@page :left {
    margin-left: 3cm;
    margin-right: 2cm;
}

@page :right {
    margin-left: 2cm;
    margin-right: 3cm;
}
```

---

### Page Breaks

```css
/* Avoid breaks */
h1, h2, h3 {
    page-break-after: avoid;
}

table {
    page-break-inside: avoid;
}

/* Force breaks */
.chapter {
    page-break-before: always;
}

.section {
    page-break-after: always;
}

/* Orphans & widows */
p {
    orphans: 2;  /* Min lines at bottom of page */
    widows: 2;   /* Min lines at top of page */
}
```

---

### Print-Specific Styles

```css
/* Hide elements in print */
@media print {
    .no-print {
        display: none;
    }

    /* Remove backgrounds (save ink) */
    * {
        background: transparent !important;
    }

    /* Black text for better printing */
    body {
        color: black;
    }

    /* Expand links */
    a[href]:after {
        content: " (" attr(href) ")";
    }
}
```

---

## 📦 Batch Conversion

### Batch Markdown → PDF

```bash
#!/bin/bash
# convert_all_md.sh

for md_file in *.md; do
    echo "Converting $md_file..."

    # Get filename without extension
    base="${md_file%.md}"

    # Convert
    python scripts/ensure_utf8_bom.py "$md_file"
    ~/projects/.venv-docs/bin/python convert_md_to_html.py "$md_file" "${base}.html"
    ~/projects/.venv-docs/bin/python -m weasyprint "${base}.html" "${base}.pdf"

    echo "✅ Created ${base}.pdf"
done

echo "✅ All files converted!"
```

---

### Python Batch Converter

```python
from pathlib import Path
from weasyprint import HTML, CSS

def batch_convert(input_dir, output_dir, css_file=None):
    """
    Convert all HTML files in directory to PDF.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    # Load CSS if provided
    css = CSS(filename=css_file) if css_file else None

    # Convert all HTML files
    for html_file in input_dir.glob('*.html'):
        pdf_file = output_dir / f"{html_file.stem}.pdf"

        print(f"Converting {html_file.name} → {pdf_file.name}")

        HTML(filename=html_file).write_pdf(
            pdf_file,
            stylesheets=[css] if css else None
        )

    print("✅ Batch conversion complete!")

# Usage
batch_convert('input/', 'output/', css_file='styles.css')
```

---

## 🔧 Troubleshooting

### Thai Text Not Visible in PDF

**Problem:** Thai text shows as boxes or disappears.

**Solutions:**
1. ✅ Use 3-step method (MD → HTML → PDF)
2. ✅ Ensure UTF-8 BOM encoding
3. ✅ Use Google Fonts in HTML `<head>`
4. ✅ Specify font-family in CSS
5. ✅ Use WeasyPrint (not wkhtmltopdf or other tools)

---

### Font Not Embedded

**Problem:** PDF displays differently on other computers.

**Solution:**
```python
# Verify fonts are embedded
from PyPDF2 import PdfReader

reader = PdfReader('output.pdf')
metadata = reader.metadata

# Check embedded fonts
if '/Font' in reader.pages[0]['/Resources']:
    fonts = reader.pages[0]['/Resources']['/Font']
    print("Embedded fonts:", fonts)
```

---

### Page Breaks Wrong

**Problem:** Content split across pages incorrectly.

**Solution:**
```css
/* Prevent breaking inside elements */
table, figure, pre {
    page-break-inside: avoid;
}

/* Keep heading with content */
h1, h2, h3 {
    page-break-after: avoid;
}

/* Orphan/widow control */
p {
    orphans: 3;
    widows: 3;
}
```

---

### Large File Size

**Problem:** PDF file too large.

**Solutions:**
```python
# 1. Compress images before conversion
from PIL import Image

img = Image.open('large.jpg')
img.save('compressed.jpg', quality=70, optimize=True)

# 2. Use CSS to limit image size
css = '''
img {
    max-width: 100%;
    height: auto;
}
'''

# 3. Remove unnecessary fonts
# Only include font weights you use (400, 700) not all (100-900)
```

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,000+
**Status:** Production Ready ✅
