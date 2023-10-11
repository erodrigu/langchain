from langchain.llms import Ollama
from langchain.chat_models import ChatOpenAI

# llm = Ollama(model="orca-mini")
llm = ChatOpenAI(openai_api_key="sk-2342ajuL2f7Dbyqd9CRRg") # TODO Fix Chat OpenAI

print(llm("What are the advantages of a petrol lawn mower"))
print(llm("what type of mower are there"))
print(llm("Write a sql query to join two tables on employee id")) 
