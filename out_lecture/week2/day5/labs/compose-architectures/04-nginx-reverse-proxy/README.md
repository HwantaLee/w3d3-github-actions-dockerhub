# Architecture 04: Nginx Reverse Proxy + Multiple Web Services

```bash
docker compose config
docker compose up -d
docker compose ps
curl -s http://localhost:18089/a/
curl -s http://localhost:18089/b/
docker compose logs --tail 80
docker compose down
```

`web-a`와 `web-b`는 host port를 직접 공개하지 않는다. 외부 접근은 `proxy` service의 host port `18089`로만 들어온다.
