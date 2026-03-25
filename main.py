import os
from fastapi import FastAPI, Body
from agent import summarizer_agent
from google.adk.runners import Runner

app = FastAPI()


@app.post("/summarize")
async def handle_request(text: str = Body(..., embed=True)):
    # The Runner executes the agent logic
    runner = Runner(agent=summarizer_agent)

    # Run the agent with the user input
    result = runner.run(text)

    return {"summary": result.text}


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0. 0.0.0", port=port)