from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel


app = FastAPI()

#CORS Setting 
origins = ["*"] #Allow all origins {can be modified and restrict access}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#now well decide input and output should be like 

class QuestionRequest(BaseModel):
    question: str 

class AnswerResponse(BaseModel):
    answer: str 

#post endpoint 
@app.post("/ask", response_model=AnswerResponse) 
def answer_question(request: QuestionRequest): 
    question = request.question 
    answer = "This is a generic answer." # Replace with actual logic to get the answer 
    return {"answer": answer} 

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)