import os
from dotenv import load_dotenv
from app import app

load_dotenv()

# Use environment variables to set database URI
if os.environ.get('DATABASE_URL'):
    # This will be used for Vercel (production)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
else:
    # This will be used for local development
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

# Additional configurations
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["IMAGES"] = os.getenv("IMAGES")