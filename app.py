import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response

app = FastAPI()

@app.post("/generate-exam")
def generate_exam(file: UploadFile):
    try:
        source = file.file.read()
    except Exception as e:
        return {"message": f"There was an error uploading the file :: {str(e)}"}
    finally:
        file.file.close()

    try:
        query = """
        From the source below, please create multiple choice questions and answers in json format like this:

        { "question_text": "What is the proper position for a child safety restraint system for infants and children under two?", "choices": [{"A": "Rear-facing"}, {"B": "Forward-facing"}, {"C": "Booster seat"}, {"D": "Seat belt"}], "correct_answer": "A" }

        """
        query += f"Source: {source}"

        api_key = os.environ["MISTRAL_API_KEY"]
        model = "mistral-large-latest"

        client = MistralClient(api_key=api_key)
        chat_response = client.chat(
            model=model,
            messages=[ChatMessage(role="user", content=query)]
        )

        exam = chat_response.choices[0].message.content
        # the response from Mistral is already in json format, so don't double encode it with a JsonResponse, but instead return it as a simple Response like this:
        return Response(content=exam, media_type='application/json')
    except Exception as e:
        return {"message": f"There was an error processing the file :: {str(e)}"}

@app.get("/")
async def root():
    return {"message": "I'm alive!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)