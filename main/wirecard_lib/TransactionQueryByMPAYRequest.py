from zeep import Client

#TransactionQueryByMPAYRequest Soap Servis çağrısının yapıldığı alanı temsil eder.
#Soap çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
class TransactionQueryByMPAYRequest:
    def execute(self, token,inputrequest):
        client = Client('https://www.wirecard.com.tr/services/saleservice.asmx?WSDL')
        result = client.service.GetSaleResultMPAY(vars(token),inputrequest.MPAY)
        return result