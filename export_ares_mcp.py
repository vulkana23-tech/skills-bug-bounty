import json
import pathlib
import subprocess
import sys
import re

def main():
    mcp_dir = pathlib.Path("C:/Users/logir/.gemini/antigravity/mcp/ares")
    mcp_dir.mkdir(parents=True, exist_ok=True)

    instructions = """# ARES MCP Best Practices

ARES is an enterprise red team orchestration platform.
Before executing live modules:
1. Always verify target scope with `ares_verify_target_scope`.
2. Run `ares_dry_run_module` first to inspect OPSEC noise and obtain a 60-second cryptographic `confirmation_token`.
3. Call `ares_execute_module` using that `confirmation_token`.
4. Use `ares_query_attack_graph` to inspect paths to Domain Admins or sensitive nodes.
5. Use `ares_list_findings` and `ares_get_remediation_guidance` for post-exploitation reporting and defense remediation.
"""
    (mcp_dir / "instructions.md").write_text(instructions, encoding="utf-8")

    from ares.mcp.tools import McpToolRegistry
    from ares.mcp.security import ConfirmationTokenManager

    tm = ConfirmationTokenManager()
    reg = McpToolRegistry(token_manager=tm)
    tools = reg.list_tools()

    for t in tools:
        schema = {
            "name": t.name,
            "description": t.description,
            "parameters": t.inputSchema.model_dump() if hasattr(t.inputSchema, "model_dump") else t.inputSchema.__dict__
        }
        (mcp_dir / f"{t.name}.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")
        print(f"Generated {t.name}.json")

    print(f"Exito: {len(tools)} herramientas ARES MCP exportadas a {mcp_dir}")

if __name__ == "__main__":
    main()
