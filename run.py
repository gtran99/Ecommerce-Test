from app import app
import os

# Set default host and port
host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
port = os.getenv('FLASK_RUN_PORT', 5000)

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)