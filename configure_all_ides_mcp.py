import json
import pathlib
import shutil

PYTHON_EXE = r"C:\Users\logir\.gemini\antigravity-ide\scratch\bug-bounty-skills\rag\pentesting-everything\.venv\Scripts\python.exe"
ARES_MCP_BLOCK = {
    "command": PYTHON_EXE,
    "args": ["-m", "ares.mcp"]
}

def update_cursor():
    p = pathlib.Path.home() / ".cursor" / "mcp.json"
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        data["mcpServers"]["ares"] = ARES_MCP_BLOCK
        p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Updated Cursor mcp.json")
    else:
        print("Cursor mcp.json not found")

def update_codex():
    p = pathlib.Path.home() / ".codex" / "mcp.json"
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        data["mcpServers"]["ares"] = ARES_MCP_BLOCK
        p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Updated Codex mcp.json")

    # Also deploy skill to .codex/skills
    skill_src = pathlib.Path("skills/ares-redteam/SKILL.md")
    codex_skill = pathlib.Path.home() / ".codex" / "skills" / "ares-redteam"
    codex_skill.mkdir(parents=True, exist_ok=True)
    shutil.copy(skill_src, codex_skill / "SKILL.md")
    print("Copied ares-redteam skill to .codex/skills")

def update_opencode():
    p = pathlib.Path.home() / ".config" / "opencode" / "opencode.json"
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        if "mcp" not in data:
            data["mcp"] = {}
        data["mcp"]["ares"] = ARES_MCP_BLOCK
        p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Updated OpenCode opencode.json")

def main():
    update_cursor()
    update_codex()
    update_opencode()
    print("ARES MCP registrado exitosamente en Cursor, Codex y OpenCode!")

if __name__ == "__main__":
    main()

