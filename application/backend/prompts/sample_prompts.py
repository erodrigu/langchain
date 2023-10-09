from langchain.prompts import PromptTemplate


def generate_prompts(user_input=None):
    context_01 = """ in a clear and concise manner to a child in one sentence. """
    context_02 = """ with a focus on scientific details explain to a scientist """

    prompt = PromptTemplate.from_template(
        "Respond to the user's question that is delimited by triple backticks "
        + "to provide some context {context}"
        + "text: ```{user_input}``"
    )

    prompt_01 = prompt.format(user_input=user_input, context=context_01)
    prompt_02 = prompt.format(user_input=user_input, context=context_02)

    return [prompt_01, prompt_02]
