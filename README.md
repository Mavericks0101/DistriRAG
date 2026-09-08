# DistriRAG
DistriRAG (Distributed Vector Pipeline): Architected an event-driven document ingestion system, decoupling text chunking and LLM embedding via Redis message queues; implemented concurrent FastAPI worker pools and batched pgvector transactions to ensure fault-tolerant indexing of 10K+ documents/hr.
