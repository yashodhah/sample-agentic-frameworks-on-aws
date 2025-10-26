from crewai.flow.flow import Flow, listen, start
from agents import researcher_agent, content_writer, editor_agent


class TravelAgentFlow(Flow[str]):
    # Flow input parameters are kept in self.state (a dict)

    @start()
    async def search_online(self):
        city = self.state.get("city")
        if not city:
            raise ValueError("Missing required 'city' input. Pass via kickoff_async({\"city\": \"<name>\"}).")
        query = f"Best hair saloons for woemn in {city}"
        result = await researcher_agent.kickoff_async(query)
        return result

    @listen(search_online)
    async def write_content(self, search_result):
        city = self.state.get("city")
        if not city:
            raise ValueError("Missing required 'city' input. Pass via kickoff_async({\"city\": \"<name>\"}).")
        query = (
            f"{search_result}\n\n"
            f"Based on the search results, write a listicle of 5 places in {city}"
        )
        result = await content_writer.kickoff_async(query)
        return result
    
    @listen(write_content)
    async def edit_content(self, listicle):
        city = self.state.get("city")
        if not city:
            raise ValueError("Missing required 'city' input. Pass via kickoff_async({\"city\": \"<name>\"}).")
        query = (
            f"Review and edit the top 5 listicle article about {city}.\n\n"
            f"Content:\n{listicle}\n\n"
            "Make sure the content is well-structured, engaging, and error-free."
        )
        result = await editor_agent.kickoff_async(query)
        return result
