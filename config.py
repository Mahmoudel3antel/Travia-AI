"""
Configuration module for TRAVIA v2.0
Handles environment variables and deployment settings
"""

import os
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # Database Configuration
    database_url: str = Field(
        default="postgresql://postgres.cqcsgwlskhuylgbqegnz:traviaSupabase@aws-0-eu-central-1.pooler.supabase.com:5432/postgres",
        env="DATABASE_URL"
    )
    
    # Server Configuration
    environment: str = Field(default="production", env="ENVIRONMENT")
    port: int = Field(default=8000, env="PORT")
    host: str = Field(default="0.0.0.0", env="HOST")
    
    # Database Pool Configuration
    db_min_size: int = Field(default=5, env="DB_MIN_SIZE")
    db_max_size: int = Field(default=20, env="DB_MAX_SIZE")
    
    # Security Configuration
    jwt_secret_key: Optional[str] = Field(default=None, env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", env="JWT_ALGORITHM")
    
    # CORS Configuration
    allowed_origins: str = Field(default="*", env="ALLOWED_ORIGINS")
    
    # Logging Configuration
    log_level: str = Field(default="info", env="LOG_LEVEL")
    
    # App Information
    app_name: str = "TRAVIA AI Travel Planner API"
    app_version: str = "2.0.0"
    app_description: str = "FastAPI backend for TRAVIA travel recommendation system with Flutter mobile support"
    
    @property
    def allowed_origins_list(self) -> List[str]:
        """Convert allowed origins string to list"""
        if self.allowed_origins == "*":
            return ["*"]
        return [origin.strip() for origin in self.allowed_origins.split(",")]
    
    @property
    def is_production(self) -> bool:
        """Check if running in production environment"""
        return self.environment.lower() == "production"
    
    @property
    def is_development(self) -> bool:
        """Check if running in development environment"""
        return self.environment.lower() == "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings() 