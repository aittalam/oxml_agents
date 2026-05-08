from any_agent import AgentConfig, AnyAgent
from any_agent.tools import search_web, visit_webpage

agent = AnyAgent.create(
    "tinyagent",
    AgentConfig(
        model_id="openai:gpt-4.1-mini",
        instructions="""Use the tools, please.""",
        tools=[search_web, visit_webpage],
    ),
)

agent_trace = agent.run(
    "Which are the most used agentic frameworks? Do at most one web search"
)
