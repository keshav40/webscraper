from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).parent / "settings.yaml"

def load_settings():
    """Loads YAML settings."""
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)
