from zeep import Client
import xml.etree.ElementTree as ElementTree
import json
#Api Plus Soap Servis çağrısının yapıldığı alanı temsil eder.
#Soap çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
class ApiPlusRequest:
    def execute(self, token,inputrequest):
       
        inputrequest.ProductList={'MSaleProduct': vars(inputrequest.ProductList[0])}
        client = Client('https://www.wirecard.com.tr/services/saleservice.asmx?WSDL')

        result = client.service.SaleWithConfirm(vars(token),vars(inputrequest))
        return result


    