# run.py
from main import app
from main.common.logger import Logger

if __name__ == "__main__":
    logger = Logger("sample")
    logger.info("begin start simple web server...")
    app.run(debug=True, host='127.0.0.1', port=5000)



