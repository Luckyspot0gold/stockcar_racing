curl -X POST --data '{
    "jsonrpc": "2.0",
    "method": "platform.getBlock",
    "params": {
        "blockID": "d7WYmb8VeZNHsny3EJCwMm6QA37s1EHwMxw1Y71V3FqPZ5EFG",
        "encoding": "json"
    },
    "id": 1
}' -H 'content-type:application/json;' 127.0.0.1:9650/ext/bc/P
