from langchain.agents import create_json_chat_agent, AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage

class JsonChatAgent:
    def __init__(self, llm, tools, prompt):
        self.llm = llm
        self.tools = tools
        self.prompt = prompt
        self.memory = [
            HumanMessage(content='Hello There'),
            AIMessage(content='Hi, I am maxx. How can I help you today?')
        ]
        
        self.agent_executor = AgentExecutor(
            agent=create_json_chat_agent(self.llm, self.tools, self.prompt),
            tools=self.tools,
            handle_parsing_errors=True,
        )

    def invoke(self, query : str) -> str:
        resp = self.agent_executor.invoke({"input" : query, 'chat_history' : self.memory})
        self.memory.append(HumanMessage(content=query))
        self.memory.append(AIMessage(content=resp['output']))
        return resp['output']