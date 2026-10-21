# Dashboard demo checklist

1. Install Docker Desktop and start Docker.
2. Run `docker compose up -d` in this directory.
3. Open Grafana at http://localhost:3000 and change the initial admin password.
4. In Grafana, Dashboards > New > Import, upload `dashboard.json`, and select Prometheus.
5. In Prometheus at http://localhost:9090/targets, confirm node-exporter is UP.
6. In Grafana, verify all four panels return numeric metrics.
7. Capture your own screenshot with a visible timestamp and write down what each panel means.

**Note:** node-exporter runs inside a container; its view of the host may be incomplete. These configurations are examples, not evidence of a deployed dashboard.
