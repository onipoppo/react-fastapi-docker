from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/get/message')
def test():
    return [
        {
            'id': 1,
            'message': 'hello world',
        },
        # {
        #     'id': 2,
        #     'message': 'hello Japan',
        # }
        ]


origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)