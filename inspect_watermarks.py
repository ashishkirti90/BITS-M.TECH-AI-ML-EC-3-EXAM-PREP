from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"C:\Users\Admin\Downloads\Sem 1")
targets = [
    ROOT / "MFML" / "MFML watermark.pdf",
    ROOT / "ISM" / "ISM watermark.pdf",
    ROOT / "DNN" / "DNNWaterMarked.pdf",
    ROOT / "ML" / "ML WaterMark.pdf",
]
outdir = ROOT / "exam_analysis" / "watermarks"
outdir.mkdir(parents=True, exist_ok=True)
for p in targets:
    r = PdfReader(str(p))
    parts = [f"SOURCE: {p.relative_to(ROOT)}", f"PAGES: {len(r.pages)}"]
    sample_pages = sorted(set(list(range(min(20, len(r.pages)))) + list(range(max(0,len(r.pages)-5),len(r.pages)))))
    for i in sample_pages:
        try: txt = r.pages[i].extract_text() or ""
        except Exception as e: txt = f"[ERROR {e}]"
        parts.append(f"\n===== PAGE {i+1} =====\n{txt}")
    (outdir / f"{p.parent.name}_watermark_sample.txt").write_text("\n".join(parts), encoding="utf-8")
    print(p.name, len(r.pages))
