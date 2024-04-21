from langchain_groq import ChatGroq

def get_llm(model='mixtral-8x7b-32768'):
    llm = ChatGroq(model=model)
    return llm