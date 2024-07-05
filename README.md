# Exam Generator
This REST API is designed to be consumed by a UI app in order to allow a user to upload a file which is read by an AI that generates an entire exam with multiple choice questions and answers  
### Run the REST API's Swagger page 
You can run this directly in VSCode or from a terminal and go to it's Swagger UI to see it in action (you can also call the REST API from Postman):  
```
http://127.0.0.1:8000/docs
```
### Press "Try it out"  
![image](https://github.com/rcorvus/ExamGenerator/assets/5025458/2c8753bd-5bbc-4938-b776-368248880a9a)

### Choose your text file with the information you'd like to create your multiple choice exam  
The example in this repo is a selection of pages from the Washington state drivers manual that shows the new information changed in this version of the manual.  
![image](https://github.com/rcorvus/ExamGenerator/assets/5025458/9fbf198e-a2ab-4b31-96bc-2ed5cb0c5d16)

### Press "Execute"  
![image](https://github.com/rcorvus/ExamGenerator/assets/5025458/389ed2a3-9c35-424c-8c37-b0bafa333910)

### Returns the exam in JSON format  
One nice feature of Mistral is that you can easily train it to return responses already formatted in JSON so there's no need to use a json formatter or wrapper.  
As you can see, based on the provided text and no other information, it creates a list of questions each with the correct answer and additional "correctly" incorrect answers as alternatives, including multiple correct answers such as "A and B".  
This allows the UI to easily consume the data in order to create or modify the exam.
![image](https://github.com/rcorvus/ExamGenerator/assets/5025458/40e2a968-c565-484a-9a6a-ac7357697fd2)


### Built with Python, FastAPI, and Mistral  
You'll need to install the following:  
``` 
pip install mistralai fastapi uvicorn python-multipart  
```
Go to the mistral-ai.com site in order to create your api key and store it in a "MISTRAL_API_KEY" environmental variable on your computer.

### Enjoy!
