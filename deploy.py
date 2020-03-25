import json
from web3 import Web3
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
abi = json.loads('[ { "constant": false, "inputs": [ { "name": "stat", "type": "int256" } ], "name": "updatestatus", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getmedicines", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getstatus", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "status", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "medicines", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "medicine", "type": "string" } ], "name": "addmedicines", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" } ]')
bytecode = 
"608060405234801561001057600080fd5b5061063c806100206000396000f300608060405260043610610078576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063073bc8d01461007d5780632403bef7146100aa5780633b0b02901461013a578063645b8b1b1461016557806374e7711c146101bc5780637be6c88b14610278575b600080fd5b34801561008957600080fd5b506100a8600480360381019080803590602001909291905050506102e1565b005b3480156100b657600080fd5b506100bf610328565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100ff5780820151818401526020810190506100e4565b50505050905090810190601f16801561012c5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561014657600080fd5b5061014f610406565b6040518082815260200191505060405180910390f35b34801561017157600080fd5b506101a6600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061044d565b6040518082815260200191505060405180910390f35b3480156101c857600080fd5b506101fd600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610465565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561023d578082015181840152602081019050610222565b50505050905090810190601f16801561026a5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561028457600080fd5b506102df600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290505050610515565b005b80600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555050565b60606000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103fc5780601f106103d1576101008083540402835291602001916103fc565b820191906000526020600020905b8154815290600101906020018083116103df57829003601f168201915b5050505050905090565b6000600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905090565b60016020528060005260406000206000915090505481565b60006020528060005260406000206000915090508054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561050d5780601f106104e25761010080835404028352916020019161050d565b820191906000526020600020905b8154815290600101906020018083116104f057829003601f168201915b505050505081565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020908051906020019061056792919061056b565b5050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106105ac57805160ff19168380011785556105da565b828001600101855582156105da579182015b828111156105d95782518255916020019190600101906105be565b5b5090506105e791906105eb565b5090565b61060d91905b808211156106095760008160009055506001016105f1565b5090565b905600a165627a7a7230582087ef388e5e8cc6d8f9fff941a7925c483b93cafff4e9fa23e1fdc165b59f729d0029"
web3.eth.defaultAccount = web3.eth.accounts[0]
address=web3.toChecksumAddress("0x8Ed48D5B2F9bb4a3afF672B317aFEcf2eb56660d")
mcontract = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = mcontract.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(tx_receipt.contractAddress) 


