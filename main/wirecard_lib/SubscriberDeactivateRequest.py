from zeep import Client

#SubscriberDeactivateRequest Soap Servis çağrısının yapıldığı alanı temsil eder.
#Soap çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
class SubscriberDeactivateRequest:
    def execute(self, token,inputrequest):
        client = Client('https:/www.wirecard.com.tr/services/SubscriberManagementService.asmx?WSDL')
        result = client.service.DeactivateSubscriber(vars(token),inputrequest.subscriberId)
        return result