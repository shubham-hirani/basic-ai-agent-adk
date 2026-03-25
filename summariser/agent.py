from google.adk.agents import Agent

# Rename summarizer_agent to root_agent
root_agent = Agent(
    name="summarizer", # This is the ID used internally
    model="gemini-2.5-flash",
    description="An agent that summarizes long text into concise bullet points.",
    instruction="You are a professional editor. Summarize the provided text into 3-5 key bullet points."
)