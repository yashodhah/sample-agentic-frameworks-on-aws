from crewai.tools import tool
from duckduckgo_search import DDGS

@tool('DuckDuckGoSearch')
def search_with_duckduckgo(search_query: str):
    """Search the web for information on a given topic"""
    return DDGS().text(search_query, max_results=5)