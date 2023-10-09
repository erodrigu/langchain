from langchain.schema import HumanMessage


def get_completion(prompt, model):
    messages = [HumanMessage(content=prompt)]
    return model.predict_messages(messages, temperature=0)
