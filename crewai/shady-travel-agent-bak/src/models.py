from crewai import LLM

llm = LLM(
    model="bedrock/us.amazon.nova-pro-v1:0",    # Use Amazon Bedrock models 
    temperature=0.7, max_tokens=4*1024,
)