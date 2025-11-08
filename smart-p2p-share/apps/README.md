# Java Applications

This directory hosts IntelliJ-friendly modules for the Smart P2P ecosystem.

- `p2p-node` – UDP node responsible for discovery, chunk transfer, and integration with AI/n8n.
- `p2p-client` – Desktop/CLI client that interfaces with the node for uploading and downloading files.
- `shared` – Reusable classes (DTOs, protocol definitions, utilities) consumed by both modules.

Add Gradle build files (`build.gradle.kts`) in each module and register them inside a root `settings.gradle.kts` to turn this into a multi-module project.
