from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring
#MarketPlaceAddSubPartnerRequest Xml  çağrısının yapıldığı alanı temsil eder.
#Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
#İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class MarketPlaceAddSubPartnerRequest:
    ServiceType=""
    OperationType=""
    Token=""
    UniqueId=""
    SubPartnerType=""
    Name=""
    ContactInfo=""
    FinancialInfo=""

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
        token_root=SubElement(main_root, 'Token')
        UserCode = SubElement(token_root, 'UserCode')
        UserCode.text = req.Token.UserCode
        Pin = SubElement(token_root, 'Pin')
        Pin.text = req.Token.Pin
        UniqueId=SubElement(main_root, 'UniqueId')
        UniqueId.text= req.UniqueId
        SubPartnerType=SubElement(main_root, 'SubPartnerType')
        SubPartnerType.text= req.SubPartnerType
        Name=SubElement(main_root, 'Name')
        Name.text= req.Name
    
        contactInfo_root=SubElement(main_root, 'ContactInfo')
        Country = SubElement(contactInfo_root, 'Country')
        Country.text = req.ContactInfo.Country
        City = SubElement(contactInfo_root, 'City')
        City.text = req.ContactInfo.City
        Address = SubElement(contactInfo_root, 'Address')
        Address.text = req.ContactInfo.Address
        BusinessPhone = SubElement(contactInfo_root, 'BusinessPhone')
        BusinessPhone.text = req.ContactInfo.BusinessPhone
        MobilePhone = SubElement(contactInfo_root, 'MobilePhone')
        MobilePhone.text = req.ContactInfo.MobilePhone
    
        financialInfo_root=SubElement(main_root, 'FinancialInfo')
        IdentityNumber = SubElement(financialInfo_root, 'IdentityNumber')
        IdentityNumber.text = req.FinancialInfo.IdentityNumber
        TaxOffice = SubElement(financialInfo_root, 'TaxOffice')
        TaxOffice.text = req.FinancialInfo.TaxOffice
        TaxNumber = SubElement(financialInfo_root, 'TaxNumber')
        TaxNumber.text = req.FinancialInfo.TaxNumber
        BankName = SubElement(financialInfo_root, 'BankName')
        BankName.text = req.FinancialInfo.BankName
        IBAN = SubElement(financialInfo_root, 'IBAN')
        IBAN.text = req.FinancialInfo.IBAN
        AccountName = SubElement(financialInfo_root, 'AccountName')
        AccountName.text = req.FinancialInfo.AccountName

        result = tostring(main_root).decode('utf-8')
        return (result)