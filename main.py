import requests
from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class IssRequest(BaseModel):
    message: str
    timestamp: int
    position: Coordinates = Field(alias='iss_position')


api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)
if response.status_code == 200:
    iss = IssRequest.model_validate_json(response.text)
    print(iss.position)
else:
    print(response.status_code)