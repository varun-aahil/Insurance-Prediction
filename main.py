from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
import pickle
import pandas as pd

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()


class user_input(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    sex: Annotated[Literal['female', 'male'], Field(..., description='Sex of the user')]
    bmi: Annotated[
        float,
        Field(..., gt=0, lt=50, description='BMI of the user, calculated using weight/height**2'),
    ]
    children: Annotated[int, Field(..., ge=0, lt=10, description='No of childern of the user')]
    smoker: Annotated[Literal['no', 'yes'], Field(..., description='Is the user a smoker')]
    region: Annotated[
        Literal['southwest', 'southeast', 'northwest', 'northeast'],
        Field(..., description='region of the user'),
    ]

    @field_validator('smoker', mode='before')
    @classmethod
    def normalize_smoker(cls, value):
        if isinstance(value, bool):
            return 'yes' if value else 'no'
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {'yes', 'no'}:
                return normalized
        return value

    @computed_field
    @property
    def lifestyle_risk(self) -> Literal['high', 'low']:
        if self.smoker == 'yes' or self.age >= 50:
            return 'high'
        return 'low'


UserInput = user_input


@app.post('/predict')
def predict(data: user_input):
    df = pd.DataFrame(
        [
            {
                'age': data.age,
                'sex': data.sex,
                'bmi': data.bmi,
                'children': data.children,
                'smoker': data.smoker,
                'region': data.region,
                'lifestyle_risk': data.lifestyle_risk,
            }
        ]
    )

    pred = float(model.predict(df)[0])

    return JSONResponse(status_code=200, content={'prediction': pred})
