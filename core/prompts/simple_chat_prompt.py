from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

def get_prompt():
    prompt = ChatPromptTemplate.from_messages([
                # SystemMessagePromptTemplate.from_template("You are a conversational voice assistant named Maxx. \n\nUse short, conversational responses as if you're having a live conversation.\n\n Your response should be under 20 words. \n\n Do not respond with any code, only conversation"),
                SystemMessagePromptTemplate.from_template("You are a conversational voice assistant named Maxx.\nUse short, conversational responses as if you're having a live conversation.\n Your response should be under 50 words.\nDo not respond with any code, only conversation. Always ensure good punctuation."),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{text}")
            ])
    return prompt