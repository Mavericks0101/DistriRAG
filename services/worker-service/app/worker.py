import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("worker-service")


async def process_queue():
    """Worker event loop consuming task queue for document processing."""
    logger.info("Worker service started. Listening for tasks...")
    # Entrypoint for chunking and embedding pipeline worker
    while True:
        await asyncio.sleep(10)


if __name__ == "__main__":
    try:
        asyncio.run(process_queue())
    except KeyboardInterrupt:
        logger.info("Worker service stopped.")
