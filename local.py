import ast
import requests
import json


def running_processes():
    res = requests.get("http://10.10.10.241:8080/engine-rest/process-definition?latest=true")
    res = res.json()
    result = ''
    for person in res:
        result += 'Name:' + str(person['name']) + '\n'
        result += 'Version:'+ str(person['version']) + '\n'
        countRequest = 'http://10.10.10.241:8080/engine-rest/process-instance/count?processDefinitionKey=' + person['key']
        cnt = requests.get(countRequest)
        cnt = cnt.json()
        if cnt['count'] == 1:
            result += 'Count: defined' + '\n'
        else:
            result += 'Count: undefined' + '\n'
        result += '\n'
    return result
#print(running_processes())
