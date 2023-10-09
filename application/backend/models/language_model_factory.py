from langchain.llms import Ollama
from langchain.llms import OpenAI
from langchain.llms import VertexAI


class LanguageModelFactory:
    @staticmethod
    def create_model(model_type, model_name, temperature, api_key=None):
        if model_type.lower() == "ollama":
            return Local(model_type, model_name, temperature, api_key)
        elif model_type.lower() == "openai":
            if api_key is None:
                raise ValueError("External model requires a configuration")
            return OAI(model_type, model_name, temperature, api_key)
        elif model_type.lower() == "vertexai":
            if api_key is None:
                raise ValueError("External model requires a configuration")
            return VAI(model_type, model_name, temperature, api_key)
        else:
            raise ValueError(f"Invalid model type: {model_type}")


class BaseModel:
    def run_prompt(self, prompt):
        raise NotImplementedError("Subclasses must implement run_prompt")


class Local(BaseModel):
    def __init__(self, model_type, model_name, temperature, apikey):
        self.model_type = model_type
        self.model_name = model_name
        self.temperature = temperature
        self.apikey = apikey

    def run_prompt(self, prompt):
        return Ollama(model=self.model_name, 
                      temperature=self.temperature)(prompt)


class OAI(BaseModel):
    def __init__(self, model_type, model_name, temperature, apikey):
        self.model_type = model_type
        self.model_name = model_name
        self.temperature = temperature
        self.apikey = apikey

    def run_prompt(self, prompt):
        return OpenAI(
            openai_api_key=self.apikey,
            model=self.model_name,
            temperature=self.temperature,
        )(prompt)


class VAI(BaseModel):
    def __init__(self, model_type, model_name, temperature, apikey):
        self.model_type = model_type
        self.model_name = model_name
        self.temperature = temperature
        self.apikey = apikey

    def run_prompt(self, prompt):
        return VertexAI(
            openai_api_key=self.apikey,
            model=self.model_name,
            temperature=self.temperature,
        )(prompt)
