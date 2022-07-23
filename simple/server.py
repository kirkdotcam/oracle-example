from web3 import Web3
from requests import get
from pathlib import Path
from dotenv import load_dotenv
import os
import time

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

apiKey= os.getenv("OPEN_WEATHER_API_KEY")
contractAddress = os.getenv("CONTRACT_ADDRESS");



with open(Path("./bin/WeatherOracle.json")) as file:
    contractABI = file.json()


contract = w3.eth.contract(contractAddress, contractABI)


def getWeather(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": apiKey

    }

    return get("https://api.openweathermap.org/data/2.5/weather", params=params).json()


while True:
    # scan contract events
    
    # if events updated, call getWeather and store as variable
    
    # update contract using updateWeather

    contract.functions.updateWeather(temp, jobId).transact()
