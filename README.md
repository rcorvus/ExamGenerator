# Exam Generator
This REST API is designed to be consumed by a UI app in order to allow a user to upload a file which is read by an AI that generates an entire exam with multiple choice questions and answers.  

You can run this directly then go to it's Swagger UI to see it in action (you can also call it from Postman):  
```
http://127.0.0.1:8000/docs
```
Press "Try it out":  
![image](https://github.com/rcorvus/ExamGenerator/assets/5025458/2c8753bd-5bbc-4938-b776-368248880a9a)

Choose your text file with the information you'd like to test on and press "Execute":  
In the example uploaded, it's a selection of pages from the Washington state drivers manual that shows the new information changed in this version of the manual.  

![image](https://github.com/rcorvus/ExamGenerator/assets/5025458/389ed2a3-9c35-424c-8c37-b0bafa333910)

One nice feature of Mistral is that it can easily return responses already formatted in JSON so there's no need to use a json formatter or wrapper.  
As you can see, it creates a list of questions each with the correct answer and additional "correctly" incorrect answers as alternatives, including multiple correct answers such as "A and B".  
This allows the UI to easily consume the data in order to create or modify the exam.
![image](https://github.com/rcorvus/ExamGenerator/assets/5025458/42041190-d3d3-4231-a79d-5adad95614a3)

Built with Python, FastAPI, and Mistral.
You'll need to install the following:  
``` 
pip install mistralai fastapi uvicorn python-multipart  
```
Enjoy!
