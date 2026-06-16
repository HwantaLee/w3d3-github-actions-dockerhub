# Architecture 02: Web + PostgreSQL + Adminer

```bash
docker compose config
docker compose up -d
docker compose ps
curl -I http://localhost:18086
curl -I http://localhost:18087
docker compose exec db psql -U postgres -d app -c "SELECT current_database();"
docker compose logs --tail 80
docker compose down
```

Adminer login 기준:
- Server: `db`
- Username: `postgres`
- Password: `postgres`
- Database: `app`
