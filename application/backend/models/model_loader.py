from models.language_model_factory import LanguageModelFactory


def load_model(config):
    """
    Load the language model based on the provided configuration.
    """
    return LanguageModelFactory.create_model(
        config["model_type"],
        config["model_name"],
        config["temperature"],
        config["api_key"],
    )
