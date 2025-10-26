import asyncio
from travel_agent_flow import TravelAgentFlow


async def main() -> None:
	# Run the flow
	flow = TravelAgentFlow()
	final_output = await flow.kickoff_async({"city": "Johor Bahru, Malayasia"})
	print("---- Final Output ----")
	print(final_output)


if __name__ == "__main__":
	asyncio.run(main())