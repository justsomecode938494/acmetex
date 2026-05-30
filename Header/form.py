from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/quote")
async def submit_quote(
    fullName: str = Form(...),
    email: str = Form(...),
    company: str = Form(None),
    requirements: str = Form(None)
):
    # Process the form here (email, save to DB, etc.)
    return {
        "message": "Quote submitted!",
        "fullName": fullName,
        "email": email,
        "company": company,
        "requirements": requirements
    }
