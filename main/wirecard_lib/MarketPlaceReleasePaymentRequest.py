from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring

#MarketPlaceReleasePaymentRequest Xml  çağrısının yapıldığı alanı temsil eder.
#Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
#İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class MarketPlaceReleasePaymentRequest:
     ServiceType=""
     OperationType=""
     Token=""
     CommissionRate=""
     SubPartnerId=""
     MPAY=""
     OrderId=""
     Description=""

     def execute(self, req,configs):     
        helper = Helper()
        result= HttpClient.post(configs.BaseUrl,self.convert_to_xml(req))
        return result

     def convert_to_xml(self,req):
        main_root=Element('WIRECARD')
        ServiceType=SubElement(main_root, 'ServiceType')
        ServiceType.text= req.ServiceType
        OperationType=SubElement(main_root,'OperationType')
        OperationType.text=req.OperationType
        MPAY=SubElement(main_root,'MPAY')
        MPAY.text=req.MPAY
        SubPartnerId=SubElement(main_root,'SubPartnerId')
        SubPartnerId.text=req.SubPartnerId
        CommissionRate=SubElement(main_root,'CommissionRate')
        CommissionRate.text=req.CommissionRate
        OrderId=SubElement(main_root,'OrderId')
        OrderId.text=req.OrderId
        Description=SubElement(main_root,'Description')
        Description.text=req.Description

        token_root=SubElement(main_root, 'Token')
        UserCode = SubElement(token_root, 'UserCode')
        UserCode.text = req.Token.UserCode
        Pin = SubElement(token_root, 'Pin')
        Pin.text = req.Token.Pin       
        result = tostring(main_root).decode('utf-8')
        return (result)
