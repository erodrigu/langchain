from fastapi import FastAPI, Query
import main

app = FastAPI()

# TODO: uvicorn webapp:app --reload  add to make file
# TODO add example http://127.0.0.1:8000/generate_prompts?user_input=How%20does%20photosynthesis%20work%3F


@app.post("/generate_prompts")
async def generate_prompts(user_input: str):
    main.main(user_input)
    return {"message": "Prompts generated and executed successfully."}


@app.get("/generate_prompts")
async def generate_prompts_get(user_input: str = Query(..., alias="user_input")):
    main.main(user_input)
    return {"message": "Prompts generated and executed successfully."}
