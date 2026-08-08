# Reconnaissance & Asset Discovery Reference Checklist

## 1. Passive Subdomain Gathering Sources
- **Certificate Transparency Logs**: `https://crt.sh/?q=%.target.com&output=json`
- **SecurityTrails API / HackerTarget API**
- **Wayback Machine / Gau / Waybackurls**: Extraer URLs históricas para descubrir subdominios descontinuados pero activos.

## 2. Subdomain Takeover Fingerprints
Comprobar CNAMEs apuntando a servicios de terceros no reclamados:
- **AWS S3**: `NoSuchBucket` / `The specified bucket does not exist`
- **GitHub Pages**: `There isn't a GitHub Pages site here.`
- **Heroku**: `No such app`
- **Shopify**: `Sorry, this shop is currently unavailable.`
- **Azure**: `404 Web Site not found.`
- **Surge.sh**: `project not found`

## 3. JavaScript Analysis & Secret Mining
- **Patrones de Regex útiles**:
  - AWS Key: `AKIA[0-9A-Z]{16}`
  - JWT Tokens: `eyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*`
  - Google API Key: `AIza[0-9A-Za-z-_]{35}`
  - Endpoints de API: `/(api|v1|v2|v3|auth|user|admin)\/[a-zA-Z0-9_-]+/`

## 4. Parameter Discovery
- Utilizar fuzzying de parámetros en entradas HTTP GET/POST para encontrar parámetros no documentados (`debug=true`, `admin=1`, `test=1`, `redirect=`, `url=`, `file=`, `config=`).
