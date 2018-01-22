from zeep import Client
# import xml.etree.ElementTree as ElementTree

#SubscriberSelect Soap Servis çağrısının yapıldığı alanı temsil eder.
#Soap çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
class SubscriberSelectRequest:
    def execute(self, token,inputrequest):
        client = Client('https://www.wirecard.com.tr/services/SubscriberManagementService.asmx?WSDL')
        result = client.service.SelectSubscriber(vars(token),vars(inputrequest))
        return result
      