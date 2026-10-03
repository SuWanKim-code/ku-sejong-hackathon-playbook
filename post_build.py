"""빌드된 index.html 의 기획서 템플릿 링크를 HTML 안에 내장된 다운로드 링크로 바꾼다."""
import base64, pathlib
root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
src = "<p>[기획서 템플릿 내려받기](project-plan-template.docx)</p>"
data = base64.b64encode((root / "project-plan-template.docx").read_bytes()).decode()
mime = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
dst = ('<p><a href="data:%s;base64,%s" download="[Template] 고려대 세종캠 Studio 활용 프로젝트 기획서.docx" '
       'style="display:inline-block;padding:10px 18px;border:1px solid var(--ups-purple);'
       'border-radius:var(--radius-md);color:var(--ups-purple);font-weight:600;text-decoration:none">'
       '기획서 템플릿 내려받기 (.docx)</a></p>') % (mime, data)
assert html.count(src) == 1, html.count(src)
(root / "index.html").write_text(html.replace(src, dst), encoding="utf-8")
print("template link embedded")
