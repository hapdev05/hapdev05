# n8n Automation Workflows

This folder stores n8n workflows that receive classification events from the P2P node and organise files on the host machine. Mount this directory into your n8n container using the `docker/docker-compose.yml` stack.

## Suggested workflows

- `file-routing.json` – Webhook-triggered flow that accepts metadata from the Java node, calls the AI classifier if necessary, and routes the file to the folder generated from the predicted label.
- `notify-user.json` – Optional notification pipeline (email/Slack) confirming that a file has been archived.

Place exported `.json` files inside `workflows/`. Use the `scripts/` directory for helper scripts invoked via the n8n “Execute Command” node to create directories and move files.
