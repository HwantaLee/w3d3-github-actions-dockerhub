# Week 2 Day 4 Hands-on Lab: Runtime Config and Observability

이 lab은 runtime config, logs, inspect, exec, stats, failure drill, cleanup audit을 다룬다.

## Phase A: env and env-file
```bash
mkdir -p week2/day4/labs/env-report
printf "APP_ENV=practice
FEATURE_FLAG=on
" > week2/day4/labs/env-report/.env.example
cp week2/day4/labs/env-report/.env.example week2/day4/labs/env-report/.env
docker run --rm --env-file week2/day4/labs/env-report/.env alpine:3.20 env
```

## Phase B: logs
```bash
docker run -d --name paperclip-day4-nginx -p 18084:80 nginx:alpine
docker logs paperclip-day4-nginx --tail 50
curl -I http://localhost:18084
```

## Phase C: inspect and exec
```bash
docker inspect paperclip-day4-nginx --format "{{json .NetworkSettings.Ports}}"
docker inspect paperclip-day4-nginx --format "{{json .Mounts}}"
docker exec paperclip-day4-nginx ls -l /usr/share/nginx/html
docker exec paperclip-day4-nginx sh -c "ps aux | head"
```

## Phase D: stats and restart policy
```bash
docker stats paperclip-day4-nginx --no-stream
docker update --restart unless-stopped paperclip-day4-nginx
docker inspect paperclip-day4-nginx --format "{{json .HostConfig.RestartPolicy}}"
```

## Phase E: failure drill
```bash
docker run --name paperclip-day4-bad postgres:16 || true
docker logs paperclip-day4-bad --tail 30 || true
```

## Phase F: cleanup/security audit
```bash
docker ps -a
docker network ls
docker volume ls
docker system df
```

```bash
docker stop paperclip-day4-nginx paperclip-day4-bad || true
docker rm paperclip-day4-nginx paperclip-day4-bad || true
```

## Compose mapping for Day 5
```text
-p host:container -> services.<name>.ports
-e KEY=value -> services.<name>.environment
-v source:target -> services.<name>.volumes
--network name -> networks
logs/exec/check -> docker compose logs/exec/run
```
