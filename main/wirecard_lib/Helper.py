import hashlib
import datetime
import base64
import requests
import xml.dom.minidom as MND


class Helper(object):

    @staticmethod
    def formatXML(input):
        doc = MND.parseString(input)
        output = doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8").decode('UTF-8')        
        return output;

class HttpClient(object):
   #Xml çağrılarını Url bilgisi ve xml metinleri ile birlikte belirtilen url adresine post edilmesini sağlar.
    @staticmethod
    def post(url, content):
        print("----IN HTTP POST----")
        print("URL: ", url)
        print("DATA:", content)
        client= requests.post(url,content)
        return client.text