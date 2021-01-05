from docx import Document
from docx.enum.style import WD_STYLE_TYPE

document = Document()
styles = document.styles
table_styles = [
    s for s in styles if s.type == WD_STYLE_TYPE.TABLE
]
for style in table_styles:
    print(style.name)
