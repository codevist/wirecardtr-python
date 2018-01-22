from zeep import Client
# import xml.etree.ElementTree as ElementTree

#SendInformationSmsRequest Soap Servis çağrısının yapıldığı alanı temsil eder.
#Soap çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
class SendInformationSmsRequest:
  
    def execute(self, token,inputrequest):

        client = Client('http://vas.mikro-odeme.com/services/msendsmsservice.asmx?WSDL')
        result = client.service.SendSMS(vars(token),vars(inputrequest))
        return result
    
        # xml = client.create_message(client.service,"SendSMS",vars(token),vars(inputt))
        # xmlstr = ElementTree.tostring(xml, encoding='utf8', method='xml')
        #        print(xmlstr)
      

