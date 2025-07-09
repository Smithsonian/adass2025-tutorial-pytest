# -------------------------------
# Python Requests Solutions
# -------------------------------

# NOTE:
# requests (plural) is a python package for http/https requests
# request (singular) is a fixture from inside the pytest package
import os
import json
import requests


# Exercise
# Make a python header request to https://chandra.harvard.edu/photo/2024/ and verify
# a success http code (success codes [200, 400)
def test_chandra_head():
    url = "https://chandra.harvard.edu/photo/2024/"
    resp = requests.head(url)
    assert 200 <= resp.status_code < 400


# Exercise
# Make a python GET request to
# url = "https://cda.cfa.harvard.edu/csccli/getProperties?query=select%20top%201%20name,%20ra,%20dec%20from%20master_source"
# with a 10 second timeout
# Decode the binary response content with utf-8
# Assert that the text 'right ascension' is in the content
def test_chandra_get():
    url = "https://cda.cfa.harvard.edu/csccli/getProperties?query=select%20top%201%20name,%20ra,%20dec%20from%20master_source"
    resp = requests.get(url, timeout=10)
    assert "right ascension" in resp.content.decode("utf-8")


# Exercise
# Make a POST request with data payload data ={"instrument": "ACIS"} to
# url = "https://httpbin.org/post"
# Assert the status code is a success
# Assert ACIS is in the response text (since that was what was posted).
# resp.text automatically applies character encoding to the binary content response.
def test_chandra_post():
    url = "https://httpbin.org/post"
    data = {"instrument": "ACIS"}
    resp = requests.post(url, data=data)
    assert 200 <= resp.status_code < 400
    assert "ACIS" in resp.text


# Exercise
# Make get request to the NED service which returns a json response
# Use the json package to parse the response.text
# or directly get the response with response.json
# See: https://ned.ipac.caltech.edu/Documents/Guides/Interface/ObjectLookup
def test_nameresolver_notObjectName():
    """Test resolution of fictional target."""
    url_ned = "https://ned.ipac.caltech.edu/NED::OLU::Egret"
    url = os.path.join(url_ned, "?name=abcNameOfTargetThatDoesNotExist")
    resp = requests.get(url)

    dict_expected = {
        "ResultCode": 0,
        "QueryTime": "Fri Jan 31 08:14:46 2025",
        "Copyright": "(C) 2025 California Institute of Technology",
        "Supplied": "abcNameOfTargetThatDoesNotExist",
        "Version": "2.0",
        "NameResolver": "NED-Egret",
        "StatusCode": 100,
    }
    dict_actual = json.loads(resp.content.decode("utf-8"))
    assert (
        dict_actual["Version"].split(".")[0] == dict_expected["Version"].split(".")[0]
    )  # Only compare major version since minor should be non-breaking change
    assert dict_actual["StatusCode"] == dict_expected["StatusCode"]
    assert dict_actual["ResultCode"] == dict_expected["ResultCode"]
    assert dict_actual["Supplied"] == dict_expected["Supplied"]
    assert dict_actual["NameResolver"] == dict_expected["NameResolver"]
