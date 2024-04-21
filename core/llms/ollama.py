from langchain_community.llms import Ollama

def get_llm(model="mistral"):
    llm = Ollama(model=model)
    return llm