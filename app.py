from flask import Flask
import os
app = Flask(__name__)

def read_version():
    try:
        with open('/app/VERSION', 'r') as f:
            return f.read().strip()
    except Exception:
        return os.getenv('IMAGE_TAG', 'dev')
    
@app.route('/')
def hello():
    return f'Hello from simple-app Version: {read_version()}\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
