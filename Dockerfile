FROM python:3.9.7
RUN pip install fastapi uvicorn
COPY ./index /index
CMD [ "uvicorn",'a-RESTful-app-using-Python-and-FastAPI.index:app','--host','0.0.0.0','--port','8000' ]