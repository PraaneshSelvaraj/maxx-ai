from langchain.agents import create_json_chat_agent, AgentExecutor

class JsonChatAgent:
    def __init__(self, llm, tools, prompt):
        self.llm = llm
        self.tools = tools
        self.prompt = prompt

        self.agent_executor = AgentExecutor(
            agent=create_json_chat_agent(self.llm, self.tools, self.prompt),
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
        )

    def invoke(self, query : str) -> str:
        resp = self.agent_executor.invoke({"input" : query})
        return resp['output']