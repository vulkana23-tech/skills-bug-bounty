# HTTP Desynchronization Mutations Reference

## 1. Ejemplos de Mutaciones de Encabezados

- `Transfer-Encoding: chunked\r\nTransfer-Encoding: cow`
- `Transfer-Encoding : chunked`
- `Content-Length: 44\r\nContent-Length: 11`

## 2. Remediación Segura

- Deshabilite la reutilización de conexiones TCP (HTTP Keep-Alive) entre proxies frontales y backends o fuerce el uso exclusivo del protocolo HTTP/2 end-to-end.
- Configure proxies para rechazar peticiones que contengan encabezados `Transfer-Encoding` y `Content-Length` simultáneamente conforme al RFC 7230.
