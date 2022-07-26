from web3 import Web3
from requests import get
from pathlib import Path
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

apiKey= os.getenv("OPEN_WEATHER_API_KEY")
contractAddress = os.getenv("CONTRACT_ADDRESS");


with open(Path("./bin/WeatherOracle.abi")) as file:
    contractABI = json.load(file)


contract = w3.eth.contract(address=contractAddress, abi=contractABI)


def getWeather(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": apiKey

    }

    return get("https://api.openweathermap.org/data/2.5/weather", params=params).json()

def KtoF(tempK):
    return ((tempK - 273.15) * (9/5)) + 32

event_filter = contract.events.NewJob().createFilter(fromBlock="0x0")
print("starting event loop...")
while True:
    # scan contract events
    events = event_filter.get_new_entries()

    # if events updated, call getWeather 
    if (events):
        newEvent = events[0].args
        jobId = newEvent.jobId
        weatherDict = getWeather(newEvent.lat, newEvent.lon)
        tempK = weatherDict["main"]["temp"]
        tempF = round(KtoF(tempK)) # using uint datatype in updateWeather on contract

        # update contract using updateWeather
        tx_hash = contract.functions.updateWeather(tempF, jobId).transact({"from":w3.eth.accounts[1]})
        
        print(f"""
        tx_hash: {tx_hash}
        jobId: {jobId}
        """)
    time.sleep(3)