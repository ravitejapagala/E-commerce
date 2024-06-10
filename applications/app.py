from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello")
    print("I am doing my hime")
    print("HI")
    print("Version")
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


print("Hello Hi")
# Path: applications/requirements.txt
# flask

# Path: applications/Dockerfile
# FROM python:3.7-slim
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# CMD ["python", "app.py"]
