from pathlib import Path
import logging
from pypdf import PdfReader
logging.getLogger("pypdf").setLevel(logging.ERROR)
root=Path(r"C:\Users\Admin\Downloads\Sem 1")
for subj,name in [("MFML","MFML watermark.pdf"),("ML","ML WaterMark.pdf")]:
    p=root/subj/name; r=PdfReader(str(p)); parts=[]
    for i,page in enumerate(r.pages,1):
        parts.append(f"\n===== PAGE {i} =====\n"+(page.extract_text() or ""))
    out=root/'exam_analysis'/'extracted'/f'{subj}_{name}.txt'
    out.write_text(f'SOURCE: {p.relative_to(root)}\n'+''.join(parts),encoding='utf-8')
    print(subj,len(r.pages),len(''.join(parts)))
