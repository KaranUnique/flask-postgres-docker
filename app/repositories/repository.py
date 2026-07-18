# Change ONLY this file to switch repositories.

from app.repositories.postgres_repository import PostgresRepository
# from app.repositories.memory_repository import MemoryRepository

repository = PostgresRepository()

# repository = MemoryRepository()