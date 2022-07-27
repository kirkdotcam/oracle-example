//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;

contract Quote { 
    string public latestQuote;

    event NewQuote(string quote);

    function createQuote(string memory quote) public {
        emit NewQuote(quote);

        latestQuote = quote;

    }


}