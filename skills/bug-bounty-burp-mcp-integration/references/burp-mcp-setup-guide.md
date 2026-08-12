# 🛠️ Technical Reference: Burp Suite MCP Setup Guide

## ⚙️ Configuration Snippet (`mcp-config.json`)
```json
{
  "mcpServers": {
    "burp-suite": {
      "command": "node",
      "args": ["/path/to/burp-mcp-server/index.js"],
      "env": {
        "BURP_API_URL": "http://127.0.0.1:1337",
        "BURP_API_KEY": "YOUR_BURP_REST_API_KEY"
      }
    }
  }
}
```

## 🔍 Intercept & Replay API Commands
- **Fetch Proxy History**: `GET http://127.0.0.1:1337/v1.0/proxy/history`
- **Send to Repeater**: `POST http://127.0.0.1:1337/v1.0/repeater`
