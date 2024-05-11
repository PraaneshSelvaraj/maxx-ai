from core import agents
from core.llms import groqLLM, ollama
from core.tools import get_tools
from core.prompts import structured_chat_prompt, simple_chat_prompt
from core.chat import SimpleChat
from langchain.memory import ConversationBufferMemory

class Brain:
    def __init__(self, agentMode=True) -> None:
        self.agentMode= agentMode
        self.llm = groqLLM.get_llm()

        if agentMode:
            self.tools = get_tools()
            self.prompt = structured_chat_prompt.get_prompt()
            self.agent = agents.JsonChatAgent(self.llm, self.tools, self.prompt)
        else:
            self.prompt = simple_chat_prompt.get_prompt()
            self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
            self.simpleChat = SimpleChat(self.llm, self.prompt, self.memory)

    def invoke(self, query : str) -> str:
        if self.agentMode:
            return self.agent.invoke(query)
        else:
            return self.simpleChat.invoke(query)