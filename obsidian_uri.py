import sys, os, urllib.parse

def open_obsidian(target, vault="Cyber-Vault"):
    if not target or target == "--dashboard":
        target = "00-WarRoom-Dashboard.md"
        
    encoded_vault = urllib.parse.quote(vault)
    
    if target.startswith("--search "):
        query = target.replace("--search ", "").strip()
        encoded_query = urllib.parse.quote(query)
        uri = f"obsidian://search?vault={encoded_vault}&query={encoded_query}"
    else:
        # Limpiar extension o barras
        file_path = target.replace("\\\\", "/").strip("/")
        if not file_path.endswith(".md") and not file_path.endswith(".canvas") and not file_path.endswith(".base"):
            file_path += ".md"
        encoded_file = urllib.parse.quote(file_path)
        uri = f"obsidian://open?vault={encoded_vault}&file={encoded_file}"
        
    print(f"[*] Disparando URI de Obsidian: {uri}")
    try:
        os.startfile(uri)
        print("[+] ¡Comando enviado a Obsidian Desktop!")
    except Exception as e:
        print(f"[!] Error al invocar os.startfile: {e}")

if __name__ == "__main__":
    t = sys.argv[1] if len(sys.argv) > 1 else "--dashboard"
    v = sys.argv[2] if len(sys.argv) > 2 else "Cyber-Vault"
    open_obsidian(t, v)
