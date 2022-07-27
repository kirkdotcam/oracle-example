from requests import get
from web3 import Web3
from dotenv import load_dotenv
from pathlib import Path
import time
import os
import json

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
contractAddress = os.getenv("CONTRACT_ADDRESS");

with open(Path("./bin/Quote.abi")) as file:
    contractABI = json.load(file)

contract = w3.eth.contract(address=contractAddress, abi=contractABI)


while True:
  res=get("https://api.kanye.rest/").json()
  
  contract.functions.createQuote(res["quote"], {"from": w3.eth.accounts[1]})
  print("more ye")
  time.sleep(3)

