from google.adk.agents import Agent

# Define the summarizer agent
summarizer_agent = Agent(
    name="summarizer",
    model="gemini-1.5-flash",
    description="An agent that summarizes long text into concise bullet points.",
    instruction="You are a professional editor. Summarize the provided text into 3-5 key bullet points. Do not add any conversational filler."
)