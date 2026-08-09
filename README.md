# Bug Bounty & Security Agent Skills Collection (100 Skills Milestone)

[![CI/CD Validation](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/validate.yml/badge.svg)](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/validate.yml)
[![Skills Count](https://img.shields.io/badge/Skills-100%20Skills-brightgreen.svg)](https://github.com/vulkana23-tech/skills-bug-bounty)
[![MCP Ready](https://img.shields.io/badge/MCP-Enabled-purple.svg)](https://github.com/vulkana23-tech/skills-bug-bounty)
[![OpenCode Ready](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://opencode.ai)
[![Claude Code Ready](https://img.shields.io/badge/Claude%20Code-Compatible-orange.svg)](https://claude.ai)

A comprehensive, curated collection of **100 Agent Skills** for **OpenCode**, **Claude Code**, **Antigravity**, **Cursor**, and **RAG-enabled AI Assistants**. 

Now featuring **Model Context Protocol (MCP)** tool call mappings, **Payloads & Wordlists**, **Automated Vulnerability Reporting Templates**, and a **Workflow Orchestrator CLI (`agent.py`)**.

---

## ⚡ Quick One-Line Installation

Install all 100 skills or choose a lightweight profile for your environment:

### Linux / macOS (Bash/Zsh)
```bash
curl -sSL https://raw.githubusercontent.com/vulkana23-tech/skills-bug-bounty/main/install.sh | bash -s -- all
```

### Windows (PowerShell)
```powershell
iwr -useb https://raw.githubusercontent.com/vulkana23-tech/skills-bug-bounty/main/install.ps1 | iex
```

---

## 🤖 Pentesting Workflow Orchestrator (`agent.py`)

Run the python orchestrator to switch profiles and load tools interactively:

```bash
python3 agent.py
```

---

## 🛠️ MCP (Model Context Protocol) Integration (`mcp/`)

Connect your AI Agent to local CLI tools (`subfinder`, `nmap`, `httpx`, `nuclei`, `ffuf`) using the Model Context Protocol configuration in [`mcp/mcp-config.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/mcp/mcp-config.json).

---

## 💣 Payloads, Wordlists & Report Templates

- **Payloads**: [`payloads/xss-waf-bypasses.txt`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/payloads/xss-waf-bypasses.txt), [`payloads/sqli-polyglots.txt`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/payloads/sqli-polyglots.txt)
- **Wordlists**: [`wordlists/api-endpoints-top100.txt`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/wordlists/api-endpoints-top100.txt), [`wordlists/subdomains-top1000.txt`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/wordlists/subdomains-top1000.txt)
- **Report Templates**: [`templates/hackerone-report-template.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/templates/hackerone-report-template.md), [`templates/bugcrowd-report-template.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/templates/bugcrowd-report-template.md)

---

## 🚀 Two Flexible Integration Modes

### Option A: Dynamic Lightweight Profiles (Anti-Prompt Saturation)

| Profile | Manifest Path | Skills | CLI Tools |
| :--- | :--- | :---: | :--- |
| **🔍 Recon & OSINT** | [`profiles/profile-recon-osint.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-recon-osint.json) | 25 | `subfinder`, `amass`, `httpx`, `naabu`, `spiderfoot` |
| **🌐 Web & API Audit** | [`profiles/profile-web-api-audit.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-web-api-audit.json) | 30 | `ffuf`, `arjun`, `linkfinder`, `secretfinder`, `jwt_tool` |
| **☁️ Cloud & DevOps** | [`profiles/profile-cloud-devops.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-cloud-devops.json) | 15 | `nuclei`, `s3scanner`, `cloudfox`, `checkov`, `docker` |
| **🔥 Advanced Exploitation** | [`profiles/profile-advanced-exploitation.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-advanced-exploitation.json) | 19 | `smuggler.py`, `turbo-intruder`, `sqlmap`, `bchecks` |
| **📱 Mobile, IoT & Binary** | [`profiles/profile-mobile-iot-binary.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-mobile-iot-binary.json) | 11 | `frida`, `apktool`, `binwalk`, `checksec`, `gdb` |

---

### Option B: Persistent Knowledge & RAG Integration (`rag/`)

1. **🤖 Ready-to-Use System Prompt**: [`rag/system-prompt-master.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/system-prompt-master.md)
2. **📄 Single-File Compendium**: [`rag/full-bug-bounty-knowledge-base.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/full-bug-bounty-knowledge-base.md)
3. **📊 Vector DB Datasets**: [`rag/chunks/`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/chunks)

---

## 📁 Repository Structure

```
bug-bounty-skills/
├── README.md                           # Master documentation & selection guide
├── skills.json                         # Master Manifest (100 skills)
├── agent.py                            # Interactive workflow orchestrator CLI
├── install.sh                          # One-line Linux/macOS installer
├── install.ps1                         # One-line Windows PowerShell installer
├── mcp/                                # 🛠️ Model Context Protocol (MCP) configs
├── payloads/                           # 💣 XSS and SQLi polyglot payload lists
├── wordlists/                          # 📝 API routes and subdomain dictionaries
├── templates/                          # 📋 HackerOne and Bugcrowd report templates
├── profiles/                           # 🚀 Dynamic Lightweight Profiles with tool mappings
├── rag/                                # 🧠 Persistent Knowledge & RAG Datasets
└── skills/                             # 100 Modular skills (SKILL.md + references/)
```

---

## 📄 License & Legal Notice
Maintained for educational purposes and authorized security research within defined program scopes.
