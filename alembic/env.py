from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from database import Base  # Импортируем Base из вашего файла database.py, где он определен

# Записывайте конфигурацию логирования
fileConfig(context.config.config_file_name)

# Интерфейс для работы с метаданными
target_metadata = Base.metadata

def run_migrations_online():
    # Здесь логика подключения к базе
    configuration = context.config
    connectable = engine_from_config(
        configuration.get_section(configuration.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_bind_param=process_bind_param,
        )

        with context.begin_transaction():
            context.run_migrations()

def process_bind_param(value, dialect):
    return value

run_migrations_online()
