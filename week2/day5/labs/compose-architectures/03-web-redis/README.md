# Architecture 03: Web + Redis Cache

```bash
docker compose config
docker compose up -d
docker compose ps
curl -I http://localhost:18088
docker compose run --rm redis-cli
docker compose exec redis redis-cli SET lesson day5
docker compose exec redis redis-cli GET lesson
docker compose logs --tail 80
docker compose down
```
