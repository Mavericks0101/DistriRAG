# DistriRAG

An event-driven, multi-tenant document ingestion and retrieval substrate. Designed for enterprise reliability, DistriRAG provides at-least-once delivery with effectively-once state changes, built on PostgreSQL (pgvector) and Redis Streams.

## Architecture Highlights
- **Asynchronous Ingestion:** Public APIs record durable intent and return `202 Accepted`.
- **Effectively-Once Delivery:** Handled via deterministic identifiers, database unique constraints, and transactional outbox/inbox records.
- **Pluggable Pipeline:** Extractor, chunker, and embedder workers are decoupled via Redis Streams.

## Quickstart

### Prerequisites
- Python 3.10+
- Docker & Docker Compose (for local infrastructure)

### Local Development
To set up your local development environment:

```bash
# Create a virtual environment and install dependencies
make install

# Run the test suite
make test

# Start the API server
make run
```

## CI/CD and Project Management
This project enforces rigorous CI/CD. All branches must pass `make test` and `make lint` via Jenkins webhooks before merging.

Work tracking, iterations, and sprint planning are managed via GitHub Projects. Please refer to the internal GitHub Board for priority fields, draft issues, and current iteration status.

## License
MIT License
