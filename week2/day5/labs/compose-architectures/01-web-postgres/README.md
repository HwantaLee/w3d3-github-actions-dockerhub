# Architecture 01: Web + PostgreSQL

```bash
docker compose config
docker compose up -d
docker compose ps
curl -I http://localhost:18085
docker compose exec db psql -U postgres -d app -c "SELECT current_database();"
docker compose logs --tail 80
docker compose down
```

`docker compose down -v`는 `pgdata` volume까지 삭제한다. 실습 DB를 초기화할 때만 사용한다.
