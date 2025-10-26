from crewai import Agent
from textwrap import dedent
from models import llm
from tools import search_with_duckduckgo


researcher_agent = Agent(
    role="Travel Researcher",
    goal="Research and compile interesting activities and attractions for a given location",
    backstory=dedent(
        """You are an experienced travel researcher with a knack for 
        discovering highly rated locations.
        Your expertise lies in gathering comprehensive 
        information about various locations, user feedbacks/reviews and vibe.
        """),
    llm=llm,
    allow_delegation=False, max_iter=4,
    tools=[search_with_duckduckgo],
    verbose=True,
)

content_writer = Agent(
    role="Content Writer",
    goal="Write a listicle of 5+ cafes/shooping locations for a given location",
    backstory=dedent(
        """You are a content writer with a knack for creating engaging
        and informative content for short contents. Your expertise lies in
        crafting engaging and informative content for shorter blogs and social media platfoirms.
        You have to provide the absoultely necessary information to the user
        """),
    llm=llm,
    allow_delegation=False, max_iter=4,
    verbose=True,
)

editor_agent = Agent(
    role="Content Editor",
    goal="Ensure the listicle is well-structured, engaging, and error-free",
    backstory=dedent(
        """You are a meticulous editor with years of experience in
        travel content. Your keen eye for detail helps polish articles
        to perfection. You focus on improving flow, maintaining
        consistency, and enhancing the overall readability of the
        content while ensuring it appeals to the target audience.
        """),
    llm=llm,
    allow_delegation=False, max_iter=4,
    verbose=True,
)