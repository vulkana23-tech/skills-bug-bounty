"""
Unified Stealth Intelligence Engine: Scrapling + Agent-Reach
Combines Scrapling's anti-bot stealth scraping with Agent-Reach's community & developer platform extraction.
"""

import sys
import re
import json
import logging
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")
logger = logging.getLogger("stealth_intel")


def fetch_with_scrapling(
    url: str,
    impersonate: str = "chrome",
    extraction_type: str = "markdown",
    timeout: int = 25,
    max_chars: int = 15000,
) -> Dict[str, Any]:
    """
    Fetch any web page using Scrapling's stealth TLS impersonation (bypasses Cloudflare & WAF)
    and extracts clean Markdown or text for LLM consumption.
    """
    try:
        from scrapling.fetchers import Fetcher
        from scrapling.core.shell import Convertor

        logger.info(f"Scrapling stealth fetch (TLS impersonate={impersonate}): {url}")
        page = Fetcher.get(
            url,
            impersonate=impersonate,
            stealthy_headers=True,
            timeout=timeout,
            follow_redirects=True,
        )

        if page.status >= 400:
            return {
                "ok": False,
                "status": page.status,
                "engine": "scrapling",
                "url": url,
                "error": f"HTTP {page.status}",
                "content": "",
            }

        # Extract markdown or clean text
        chunks = list(
            Convertor._extract_content(
                page,
                extraction_type=extraction_type,
                main_content_only=True,
            )
        )
        content = "".join(chunks).strip()
        if len(content) > max_chars:
            content = content[:max_chars] + f"\n\n[... Truncado a {max_chars} caracteres para el contexto ...]"

        # Extract title
        title_el = page.css("title")
        title = title_el[0].text.strip() if title_el else ""

        return {
            "ok": True,
            "status": page.status,
            "engine": "scrapling",
            "url": page.url,
            "title": title,
            "content": content,
        }
    except Exception as e:
        logger.error(f"Scrapling error on {url}: {e}")
        return {
            "ok": False,
            "engine": "scrapling",
            "url": url,
            "error": str(e),
            "content": "",
        }


def fetch_with_agent_reach(url: str) -> Dict[str, Any]:
    """
    Fetch platform-specific intelligence (GitHub, Reddit, YouTube, etc.) using Agent-Reach.
    """
    try:
        import subprocess

        python_exe = sys.executable
        cmd = [python_exe, "-m", "agent_reach.cli", "read", url]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        if res.returncode == 0 and res.stdout:
            data = json.loads(res.stdout)
            if data.get("ok") and data.get("items"):
                item = data["items"][0]
                text = item.get("text", "")
                title = item.get("title", "")
                raw = item.get("raw", {})
                return {
                    "ok": True,
                    "engine": "agent-reach",
                    "channel": data.get("channel", "unknown"),
                    "url": url,
                    "title": title,
                    "content": text,
                    "metadata": raw,
                }
        return {
            "ok": False,
            "engine": "agent-reach",
            "url": url,
            "error": res.stderr or res.stdout or "No data returned",
            "content": "",
        }
    except Exception as e:
        logger.error(f"Agent-Reach error on {url}: {e}")
        return {
            "ok": False,
            "engine": "agent-reach",
            "url": url,
            "error": str(e),
            "content": "",
        }


def search_web_ddg(query: str, max_results: int = 4) -> list:
    """Búsqueda web en vivo sin API keys utilizando el motor DuckDuckGo HTML."""
    import html
    import urllib.request
    import urllib.parse
    encoded = urllib.parse.quote(query)
    url = f"https://html.duckduckgo.com/html/?q={encoded}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    results = []
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            page = resp.read().decode("utf-8", errors="ignore")
        
        matches = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', page, re.DOTALL)
        urls = re.findall(r'<a class="result__url"[^>]*href="([^"]+)"[^>]*>', page, re.DOTALL)
        
        for idx, m in enumerate(matches[:max_results]):
            clean = html.unescape(re.sub(r"<[^>]+>", "", m)).strip()
            link = urls[idx] if idx < len(urls) else "Web Result"
            if "uddg=" in link:
                match_u = re.search(r"uddg=([^&]+)", link)
                if match_u:
                    link = urllib.parse.unquote(match_u.group(1))
            if clean:
                results.append({"snippet": clean, "url": link})
    except Exception as e:
        logger.error(f"Error en búsqueda web DDG: {e}")
    return results


def smart_fetch(target: str, max_chars: int = 15000) -> Dict[str, Any]:
    """
    Intelligently routes target:
    - GitHub / Reddit / YouTube -> Agent-Reach (with fallback to Scrapling)
    - Any other web URL -> Scrapling stealth fetcher
    - Search query -> Web search + Scrapling top page extraction
    """
    target = target.strip()
    is_url = bool(re.match(r"^https?://", target, re.IGNORECASE))

    if not is_url:
        # Búsqueda web normal por términos o preguntas
        logger.info(f"Búsqueda web solicitada: '{target}'")
        results = search_web_ddg(target, max_results=4)
        
        if not results:
            return {"ok": False, "error": "No se encontraron resultados en la web.", "content": ""}

        summary_parts = [f"Resultados de búsqueda web para: '{target}'\n"]
        for idx, r in enumerate(results, 1):
            summary_parts.append(f"### {idx}. {r.get('url')}\n{r.get('snippet')}\n")
        
        # Extracción profunda con Scrapling del resultado más relevante
        first_url = results[0].get("url")
        if first_url and first_url.startswith("http"):
            logger.info(f"Scrapling stealth deep-fetch del primer resultado: {first_url}")
            deep_res = fetch_with_scrapling(first_url, max_chars=5000)
            if deep_res.get("ok") and deep_res.get("content"):
                summary_parts.append(f"\n--- Contenido profundo extraído con Scrapling ({first_url}) ---\n")
                summary_parts.append(deep_res["content"])

        return {
            "ok": True,
            "engine": "hybrid_search_scrapling",
            "url": first_url or "",
            "title": f"Búsqueda: {target}",
            "content": "\n".join(summary_parts),
        }

    # If it is a URL, determine best route:
    domain_match = re.search(r"https?://([^/]+)", target, re.IGNORECASE)
    domain = domain_match.group(1).lower() if domain_match else ""

    agent_reach_domains = ["github.com", "reddit.com", "youtube.com", "youtu.be", "x.com", "twitter.com"]

    if any(d in domain for d in agent_reach_domains):
        reach_res = fetch_with_agent_reach(target)
        if reach_res.get("ok") and reach_res.get("content"):
            return reach_res
        logger.warning("Agent-Reach did not return content, falling back to Scrapling stealth fetch...")

    # Default to Scrapling
    return fetch_with_scrapling(target, max_chars=max_chars)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python stealth_intel.py <url o consulta>")
        print("Ejemplos:")
        print("  python stealth_intel.py https://github.com/D4Vinci/Scrapling")
        print("  python stealth_intel.py https://portswigger.net/web-security/cross-site-scripting")
        print("  python stealth_intel.py 'CVE-2026-115897 serialize-javascript'")
        sys.exit(0)

    target_input = " ".join(sys.argv[1:])
    res = smart_fetch(target_input)
    print(f"\n=== Resultado ({res.get('engine', 'unknown')}) ===")
    print(f"Título: {res.get('title', 'N/A')}")
    print(f"URL: {res.get('url', 'N/A')}")
    print(f"Estado OK: {res.get('ok')}")
    print("\n--- Contenido ---\n")
    print(res.get("content", "")[:1000] + "\n...")

