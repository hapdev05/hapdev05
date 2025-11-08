# Smart P2P Share Workspace

This repository contains exploratory scaffolding for a UDP-based peer-to-peer file sharing system that integrates AI-driven file classification and n8n automation workflows. The structure is intended to help you bootstrap an IntelliJ (JDK 17) multi-module project together with infrastructure assets such as Docker, AI services, and n8n workflows.

The highlight of this update is the `smart-p2p-share/` directory tree, which organises application code, automation workflows, AI assets, and deployment scripts.

## Directory overview

- `smart-p2p-share/apps/` – Gradle/IntelliJ modules for the P2P node, desktop client, and shared libraries.
- `smart-p2p-share/automation/` – n8n workflow exports, credentials, and helper scripts for classifying files and moving them into AI-generated folders.
- `smart-p2p-share/ai/` – AI model assets (training notebooks, datasets, exported models) and a Python-based inference service.
- `smart-p2p-share/docker/` – Docker Compose setup plus images for n8n and the AI model server.
- `smart-p2p-share/infra/` – Environment configuration and orchestration scripts.
- `smart-p2p-share/docs/` – Design documents for architecture, AI pipeline, and workflow integration.
- `smart-p2p-share/scripts/` – Convenience scripts for local development.

Each subdirectory contains `.gitkeep` placeholders so the folders stay tracked even before real source files are added.

## Next steps

1. Convert the Java module folders into Gradle subprojects by adding `build.gradle.kts` files and a root `settings.gradle.kts`.
2. Implement the UDP messaging stack under `apps/p2p-node/src/main/java/com/example/smartp2p/network` and reuse clients in `apps/shared`.
3. Export your n8n workflows (e.g., auto-folder creation for `.img`, `.png`, `.jpg` extensions) into `automation/workflows/`.
4. Use the provided Docker skeleton to run n8n locally with volumes mounted to your host machine so workflows can manipulate local directories directly.

Feel free to expand or tailor this layout as the project evolves.
