# from dotenv import load_dotenv
# load_dotenv()

# from langchain_groq import ChatGroq

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
# )

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:1.5b",
    temperature=0,
)

def get_answer(question):
    # Use the LLM to get an answer to the question
    answer = llm.invoke(question)
    answer=answer.content
    return answer 

# result=get_answer("what is ML")

# print(result)