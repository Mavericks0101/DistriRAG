def test_worker_imports():
    from app.worker import process_queue

    assert callable(process_queue)
