from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring

#MarketPlaceDeactiveRequest Xml  çağrısının yapıldığı alanı temsil eder.
#Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
#İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class MarketPlaceDeactiveRequest:

    ServiceType=""
    OperationType=""
    UniqueId=""
    Token= ""

    def execute(self, req,configs):
       
        helper = Helper()
        result= HttpClient.post(configs.BaseUrl,self.convert_to_xml(req))
        return result

    def convert_to_xml(self, req):

        main_root = Element('WIRECARD')
        ServiceType=SubElement(main_root, 'ServiceType')
        ServiceType.text= req.ServiceType
        OperationType=SubElement(main_root,'OperationType')
        OperationType.text=req.OperationType
        UniqueId=SubElement(main_root, 'UniqueId')
        UniqueId.text= req.UniqueId
        token_root=SubElement(main_root, 'Token')
        UserCode = SubElement(token_root, 'UserCode')
        UserCode.text = req.Token.UserCode
        Pin = SubElement(token_root, 'Pin')
        Pin.text = req.Token.Pin
        xml_string = "<?xml version='1.0' encoding='UTF-8'?>"
        myresult = tostring(main_root).decode('utf-8')
        return (myresult)

