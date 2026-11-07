import pathlib

p = pathlib.Path("integrations/ARES/ares/core/browser_sessions.py")
txt = p.read_text(encoding="utf-8")
old_str = '{"http://127.0.0.1:5173", "http://localhost:5173"}'
new_str = '{"http://127.0.0.1:5173", "http://localhost:5173", "http://127.0.0.1:5174", "http://localhost:5174"}'

if old_str in txt:
    txt = txt.replace(old_str, new_str)
    p.write_text(txt, encoding="utf-8")
    print("Patched successfully")
else:
    print("old_str not found")

