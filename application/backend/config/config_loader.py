import os
import json


def load_config():
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to config.json
        config_file_path = os.path.join(script_dir, "config.json")

        # Load configuration from the JSON file
        with open(config_file_path, "r") as config_file:
            config = json.load(config_file)

        # Check for environment variable overrides
        if "MODEL_TYPE" in os.environ:
            config["model_type"] = os.environ["MODEL_TYPE"]
        if "MODEL_NAME" in os.environ:
            config["model_name"] = os.environ["MODEL_NAME"]
        if "CACHE" in os.environ:
            config["cache"] = os.environ["CACHE"]
        if "TEMPERATURE" in os.environ:
            config["temperature"] = float(os.environ["TEMPERATURE"])
        if "API_KEY" in os.environ:
            config["api_key"] = float(os.environ["API_KEY"])

        return config

    except Exception as e:
        raise ConfigurationError(f"Error loading configuration: {str(e)}")


class ConfigurationError(Exception):
    pass
