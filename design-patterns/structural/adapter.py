import json


class JSONAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        data_object = json.loads(self.data)
        print(data_object["name"])


class XMLAdapter(JSONAnalyzer):
    def analyze(self):
        self.data = '{"name": "abc"}'
        super().analyze()


if __name__ == '__main__':
    xml_data = "<name>abc</name>"

    analyzer = JSONAnalyzer(xml_data)
    try:
        analyzer.analyze()  # throws error as not json data
    except Exception as e:
        print(e)

    analyzer = XMLAdapter(xml_data)
    analyzer.analyze()
