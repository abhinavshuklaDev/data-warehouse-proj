"""
Configuration management for the Data Warehouse Project.

Responsibilities:
- Load application configuration from configs/app.yaml
- Load secrets from .env
- Validate configuration using Pydantic
- Expose a singleton config object
"""

from pathlib import Path
import os

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, Field


# -------------------------------------------------------------------------
# Configuration Models
# -------------------------------------------------------------------------

class ProjectConfig(BaseModel):
    name: str
    environment: str


class AWSConfig(BaseModel):
    region: str
    bucket: str


class KafkaConfig(BaseModel):
    bootstrap_servers: str


class SnowflakeConfig(BaseModel):
    warehouse: str
    database: str
    schema_name: str


class ProducerConfig(BaseModel):
    events_per_second: int = Field(gt=0)


class MasterDataConfig(BaseModel):
    customers: int = Field(gt=0)
    products: int = Field(gt=0)
    suppliers: int = Field(gt=0)
    warehouses: int = Field(gt=0)
    categories: int = Field(gt=0)


class AppConfig(BaseModel):
    project: ProjectConfig
    aws: AWSConfig
    kafka: KafkaConfig
    snowflake: SnowflakeConfig
    producer: ProducerConfig
    master_data: MasterDataConfig


# -------------------------------------------------------------------------
# Configuration Loader
# -------------------------------------------------------------------------

class ConfigLoader:

    def __init__(self):

        load_dotenv()

        config_path = Path("configs/app.yaml")

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        with open(config_path, "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

        self.config = AppConfig(**yaml_data)

        # Secrets from .env
        self.snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
        self.snowflake_user = os.getenv("SNOWFLAKE_USER")
        self.snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")

        self.aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")


# -------------------------------------------------------------------------
# Singleton Configuration Object
# -------------------------------------------------------------------------

config = ConfigLoader()