from settings import settings_loader

class SettingsBase:
    """Base settings class that reads configurations from config.yaml."""

    def __init__(self, client_name: str):
        self.config = self.load_config(client_name)

    def load_config(self, client_name: str) -> dict:
        """Loads configuration for the specified client."""
        config = settings_loader.load_settings()
        client_config = config.get(client_name, {})
        return {**config, **client_config}  # Merge global & client-specific configs

    def get(self, key: str, default=None):
        """Retrieve a value from the configuration."""
        return self.config.get(key, default)


class DentalstallSettings(SettingsBase):
    """Settings loader for Dentalstall client."""
    
    def __init__(self):
        super().__init__("dentalstall")
        self.base_url = self.get("base_url")
        self.image_dir = self.get("image_dir")
        self.security_token = self.get("security", {}).get("static_token")
        self.redis_host = self.get("cache", {}).get("redis_host")
        self.redis_port = self.get("cache", {}).get("redis_port")
