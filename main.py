import json, unittest, datetime

# Load input and expected data
with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)



# STEP 1: Convert Format 1 (Flat)

def convertFromFormat1(jsonObject):
    # Split location string
    location_parts = jsonObject["location"].split("/")
    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": location_parts[0],
            "city": location_parts[1],
            "area": location_parts[2],
            "factory": location_parts[3],
            "section": location_parts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }



# STEP 2: Convert Format 2 (Nested + ISO time)
#
def convertFromFormat2(jsonObject):
    # Convert ISO timestamp to milliseconds
    dt = datetime.datetime.strptime(jsonObject["timestamp"],
                                    "%Y-%m-%dT%H:%M:%S.%fZ")
    millis = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": millis,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": jsonObject["data"]
    }



# STEP 3: Main router function

def main(jsonObject):
    if jsonObject.get('device') is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)


# STEP 4: Unit tests

class TestSolution(unittest.TestCase):

    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 1 failed')

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 2 failed')


print("\nRunning Tests...\n")
unittest.main(argv=[''], exit=False)
