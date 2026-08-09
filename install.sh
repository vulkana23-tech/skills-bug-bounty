#!/usr/bin/env bash
# ==============================================================================
# Bug Bounty & Security Skills Collection Installer (OpenCode & Claude Code)
# ==============================================================================

set -e

PROFILE=${1:-"all"}
TARGET_DIR=""

echo "=================================================================="
echo "  🚀 Bug Bounty Agent Skills Installer (100 Skills Collection)"
echo "=================================================================="

# Detect framework directory
if [ -d "$HOME/.claude" ]; then
    TARGET_DIR="$HOME/.claude/skills"
    echo "[*] Detected Claude Code environment at: $TARGET_DIR"
elif [ -d ".agents" ]; then
    TARGET_DIR=".agents/skills"
    echo "[*] Detected OpenCode environment at: $TARGET_DIR"
else
    TARGET_DIR="$HOME/.agents/skills"
    echo "[*] Defaulting to OpenCode skills directory at: $TARGET_DIR"
fi

mkdir -p "$TARGET_DIR"

echo "[*] Selected Installation Profile: '$PROFILE'"

case "$PROFILE" in
    "recon"|"recon-osint")
        echo "[*] Installing Recon & OSINT Profile (25 Skills)..."
        cp -r skills/bug-bounty-recon* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-osint* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-subdomain* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-asn* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-cert* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-spiderfoot* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-amass* "$TARGET_DIR/" 2>/dev/null || true
        ;;
    "web"|"web-api")
        echo "[*] Installing Web & API Audit Profile (30 Skills)..."
        cp -r skills/bug-bounty-xss* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-sqli* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-ssrf* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-idor* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-graphql* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-jwt* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-js* "$TARGET_DIR/" 2>/dev/null || true
        ;;
    "cloud"|"cloud-devops")
        echo "[*] Installing Cloud & DevOps Profile (15 Skills)..."
        cp -r skills/bug-bounty-cloud* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-container* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-nuclei* "$TARGET_DIR/" 2>/dev/null || true
        ;;
    "advanced"|"exploitation")
        echo "[*] Installing Advanced Exploitation Profile (19 Skills)..."
        cp -r skills/bug-bounty-request-smuggling* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-http-desync* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-turbo* "$TARGET_DIR/" 2>/dev/null || true
        cp -r skills/bug-bounty-bchecks* "$TARGET_DIR/" 2>/dev/null || true
        ;;
    "all"|*)
        echo "[*] Installing Full Master Collection (100 Skills)..."
        cp -r skills/* "$TARGET_DIR/"
        ;;
esac

echo ""
echo "✅ Installation completed successfully!"
echo "📍 Installed Skills Location: $TARGET_DIR"
echo "💡 Restart your AI Agent (OpenCode / Claude Code / Antigravity) to load the skills."
