from langchain.llms import Ollama

llm = Ollama(model="orca-mini")

print(llm("What are the advantages of a petrol lawn mower"))
print(llm("what type of mower are there"))
print(llm("Write a sql query to join two tables on employee id")) 
