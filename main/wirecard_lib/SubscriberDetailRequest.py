from zeep import Client

#SubscriberDetail Soap Servis çağrısının yapıldığı alanı temsil eder.
#Soap çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
class SubscriberDetailRequest:
    def execute(self, token,inputrequest):
        client = Client('https://www.wirecard.com.tr/services/SubscriberManagementService.asmx?WSDL')
        result = client.service.SelectSubscriberDetail(vars(token),inputrequest.subscriberId)
        return result
      