# Grafana Infrastructure Monitoring

Docker Compose starter configuration with Grafana, Prometheus, and Node Exporter. Requires Docker with Compose.

## Run
```bash
docker compose up -d
docker compose ps
```
Grafana: http://localhost:3000; Prometheus: http://localhost:9090. Change Grafana's initial admin password immediately. Note that container metrics may not represent the entire host without additional configuration.

## Suggested Grafana panels
- CPU utilization: `100 * (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])))`
- Memory: `100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)`
- Disk free: `node_filesystem_avail_bytes{fstype!~"tmpfs|overlay"}`
- Network received/sec: `rate(node_network_receive_bytes_total{device!="lo"}[5m])`

## Verification
Check Prometheus Targets for exporter UP, run queries in Grafana Explore, create panels, and optionally configure an alert for CPU >85% for five minutes. Save screenshots and actual observations.

**Status:** configuration files provided; not yet deployed or verified in a live environment.
