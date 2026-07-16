from fastapi import FastAPI


app = FastAPI()


questions = [
    {
        "question_id": 1,
        "question": "What does HTTP stand for?",
        "choices": [
            "HyperText Transfer Protocol",
            "High Transfer Text Process",
            "Hyper Tool Transfer Program"
        ],
        "correct_answer": "HyperText Transfer Protocol"
    },
    {
        "question_id": 2,
        "question": "Which status code means Not Found?",
        "choices": ["200", "404", "500"],
        "correct_answer": "404"
    },
    {
        "question_id": 3,
        "question": "Which Python framework are you learning?",
        "choices": ["React", "FastAPI", "PostgreSQL"],
        "correct_answer": "FastAPI"
    }
]

answers=[]


@app.get("/quiz")
async def get_all_questions():
    return questions



