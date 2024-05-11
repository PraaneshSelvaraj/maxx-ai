from langchain.agents import create_json_chat_agent, AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage
from core.tools import reset_all_tools, get_tools_used

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
        reset_all_tools()
        resp = self.agent_executor.invoke({"input" : query, 'chat_history' : self.memory})
        self.memory.append(HumanMessage(content=query))
        tools_used = get_tools_used()
        if len(tools_used) > 0:
            self.memory.append(HumanMessage(content=f"Tools used: {tools_used}"))
        self.memory.append(AIMessage(content=resp['output']))
        return resp['output']