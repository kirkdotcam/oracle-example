//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;

contract WeatherOracle {
    mapping(uint =>bool) public jobStatus;
    mapping(uint=>uint) public jobResults;

    uint jobId;

    event NewJob(uint lat, uint lon, uint jobId);

    constructor(){
        jobId = 1;
    } 

    function getWeather(uint lat, uint lon) public {
        emit NewJob( lat, lon, jobId);

        jobId++;

    }

    function updateWeather(uint temp, uint _jobId) public{

        jobResults[_jobId] = temp;
        jobStatus[_jobId] = true;
        
    }
}

// based on https://betterprogramming.pub/building-a-simple-blockchain-oracle-with-solidity-and-node-js-29eacdad31f1