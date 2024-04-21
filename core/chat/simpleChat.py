from langchain.chains import LLMChain

class SimpleChat:
    def __init__(self, llm, prompt, memory):
        self.llm = llm
        self.prompt = prompt
        self.memory = memory

        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory
        )

    def invoke(self, query : str) -> str:
        resp = self.chain.invoke({"text":query})
        print(resp['text'])
        return resp['text']