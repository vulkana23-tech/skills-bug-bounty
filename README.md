# Bug Bounty & Security Agent Skills Collection (100 Skills Milestone)

[![CI/CD Validation](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/validate.yml/badge.svg)](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/validate.yml)
[![Security & Secret Scan](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/security-scan.yml/badge.svg)](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/security-scan.yml)
[![Auto-Update CISA KEV](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/auto-update-feeds.yml/badge.svg)](https://github.com/vulkana23-tech/skills-bug-bounty/actions/workflows/auto-update-feeds.yml)
[![Skills Count](https://img.shields.io/badge/Skills-109%20Skills-brightgreen.svg)](https://github.com/vulkana23-tech/skills-bug-bounty)
[![Version](https://img.shields.io/badge/Version-19.0.0-blue.svg)](https://github.com/vulkana23-tech/skills-bug-bounty)
[![Ethical Framing](https://img.shields.io/badge/Refusal%20Bypass-Ethical%20Framing-green.svg)](https://github.com/vulkana23-tech/skills-bug-bounty)
[![MCP Ready](https://img.shields.io/badge/MCP-Enabled-purple.svg)](https://github.com/vulkana23-tech/skills-bug-bounty)
[![OpenCode Ready](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://opencode.ai)
[![Claude Code Ready](https://img.shields.io/badge/Claude%20Code-Compatible-orange.svg)](https://claude.ai)

A comprehensive, curated collection of **109 Agent Skills** for **OpenCode**, **Claude Code**, **Cline / Roo Code**, **Antigravity**, **Cursor**, and **RAG-enabled AI Assistants**. 

Featuring **7-Question Validation Gate (`bug-bounty-7-question-gate`)**, **Claude-BugHunter 5-Phase Workflow (`profile-claude-bughunter-workflow.json`)**, **Burp Suite MCP Integration**, **Reverse-Skill Methodology Router (`MASTER-ROUTING.md`)**, **Scope Compliance Contract (`scope.md`)**, **Tool Indexing Scripts (`scripts/refresh_tool_index.py`)**, **Engagement Scaffolding CLI (`scripts/scaffold_engagement.py`)**, **Ethical Framing & Refusal Prevention Rules (`.clinerules`, `.cursorrules`, `AGENTS.md`)**, **Automated GitHub CodeQL & Gitleaks Security Scans**, **Model Context Protocol (MCP)** tool call mappings, **CISA Known Exploited Vulnerabilities (KEV)** dynamic feeds, **Few-Shot Learning Real-World Write-ups**, **Payloads & Wordlists**, **Automated Vulnerability Reporting Templates**, and a **Workflow Orchestrator CLI (`agent.py`)**.

---

## 🛡️ Repository Security & Hardening Guide

To keep this public repository secure against malicious PRs or accidental secret leaks, enable the following native GitHub features under **Settings**:

### 1. Branch Protection Rules (`main`)
- Navigate to **Settings > Branches > Add branch protection rule**.
- Set **Branch name pattern** to `main`.
- Enable **Require a pull request before merging** and **Require approvals** (1 approval).

### 2. Code Security & Secret Scanning
- Navigate to **Settings > Code security and analysis**.
- Enable: **Dependency graph**, **Dependabot alerts**, **Secret scanning**, and **Secret scanning -> Push protection**.

### 3. Automated Actions Security Scan
This repo includes automated CodeQL & Gitleaks workflows:
- [`.github/workflows/security-scan.yml`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/.github/workflows/security-scan.yml)

---

## 🛡️ Ethical Framing & Automatic Profile Routing (.clinerules / .cursorrules)

Prevents commercial LLM refusal blocks ("I cannot assist with this") by framing queries within authorized defensive audit contexts and automatically routes queries to the exact profile:

- **Cline / Roo Code Rules**: [`.clinerules`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/.clinerules)
- **Cursor IDE Rules**: [`.cursorrules`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/.cursorrules)
- **OpenCode Agent Rules**: [`AGENTS.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/AGENTS.md)

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

## 📚 Real-World Write-ups & Few-Shot Studies (`knowledge/writeups/`)

Enable your AI Agent to replicate high-bounty attack chains using real-world case studies:
- **Uber OAuth Takeover**: [`knowledge/writeups/uber-oauth-account-takeover-chain.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/knowledge/writeups/uber-oauth-account-takeover-chain.md)
- **Shopify GraphQL BFLA/IDOR**: [`knowledge/writeups/shopify-graphql-idor-bfla.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/knowledge/writeups/shopify-graphql-idor-bfla.md)
- **AWS Cloud IMDSv2 SSRF Pivot**: [`knowledge/writeups/aws-imdsv2-ssrf-cloud-pivot.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/knowledge/writeups/aws-imdsv2-ssrf-cloud-pivot.md)

---

## ⚡ Dynamic CISA KEV Exploits Feed (`profiles/wild-exploits.json`)

Automatically updated every week via GitHub Actions (`scripts/fetch_cisa_kev.py`):
- Tracks top actively exploited vulnerabilities in the wild (Ivanti RCE, Citrix Bleed, ScreenConnect Auth Bypass, Confluence Admin Creation).

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

## 🚀 Integration Profiles

| Profile | Manifest Path | Focus Area |
| :--- | :--- | :--- |
| **🔍 Recon & OSINT** | [`profiles/profile-recon-osint.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-recon-osint.json) | Subdomain discovery, ASNs, CT logs, Dorks, SpiderFoot, Amass |
| **🌐 Web & API Audit** | [`profiles/profile-web-api-audit.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-web-api-audit.json) | XSS, SQLi, IDOR, GraphQL, JWT, JS Recon, SSRF, CORS |
| **☁️ Cloud & DevOps** | [`profiles/profile-cloud-devops.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-cloud-devops.json) | AWS S3, Docker, Kubernetes RBAC, IAM, Nuclei fast scans |
| **🔥 Advanced Exploitation** | [`profiles/profile-advanced-exploitation.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-advanced-exploitation.json) | Request Smuggling, Turbo Intruder, BChecks, Race Conditions |
| **📱 Mobile, IoT & Binary** | [`profiles/profile-mobile-iot-binary.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-mobile-iot-binary.json) | Android/iOS, IoT Firmware (Binwalk), ELF/PE Binaries, KYC Deepfakes |
| **🔄 Reverse-Skill Router** | [`profiles/profile-reverse-skill-routing.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-reverse-skill-routing.json) | APK JADX/Frida, JS AST Deobfuscation, Binary CTF, Scope Obedience, Firmware |
| **🏹 BugHunter Workflow** | [`profiles/profile-claude-bughunter-workflow.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-claude-bughunter-workflow.json) | 7-Question Gate, Enterprise Identity Matrix, Burp MCP, Scaffolding |
| **⚡ Wild Exploits** | [`profiles/wild-exploits.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/wild-exploits.json) | Actively exploited CISA KEV catalog vulnerabilities |

---

## 📁 Repository Structure

```
bug-bounty-skills/
├── README.md                           # Master documentation & selection guide
├── skills.json                         # Master Manifest (100 skills)
├── .clinerules                         # 🛡️ Cline & Roo Code Ethical Framing & Auto-Routing
├── .cursorrules                        # 🛡️ Cursor IDE Ethical Framing & Auto-Routing
├── AGENTS.md                           # 🛡️ OpenCode Ethical Framing & Auto-Routing
├── agent.py                            # 🤖 Workflow Orchestrator CLI
├── install.sh                          # One-line Linux/macOS installer
├── install.ps1                         # One-line Windows PowerShell installer
├── .github/workflows/validate.yml      # CI/CD integrity & JSON validation workflow
├── .github/workflows/security-scan.yml# 🛡️ CodeQL & Gitleaks secret scan workflow [NUEVO]
├── .github/workflows/auto-update-feeds.yml# 🔄 Weekly CISA KEV feed auto-update
├── scripts/
│   └── fetch_cisa_kev.py               # ⚡ Python CISA KEV feed fetcher
├── knowledge/writeups/                 # 📚 Real-world case studies for few-shot learning
├── mcp/                                # 🛠️ MCP Configuration & Tool Mappings
├── payloads/                           # 💣 XSS and SQLi polyglots
├── wordlists/                          # 📝 API routes and subdomain dictionaries
├── templates/                          # 📋 HackerOne and Bugcrowd report templates
├── profiles/                           # 🚀 Dynamic Lightweight Profiles (including wild-exploits.json)
├── rag/                                # 🧠 Persistent Knowledge & RAG Datasets
└── skills/                             # 100 Modular skills (SKILL.md + references/)
```

---

## 📄 License & Legal Notice
Maintained for educational purposes and authorized security research within defined program scopes.
