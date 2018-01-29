from main.wirecard_lib.Helper import Helper, HttpClient
from main.wirecard_lib.configs import Configs
from xml.etree.ElementTree import Element, SubElement, tostring

#MarketPlaceMpSaleRequesy Xml  çağrısının yapıldığı alanı temsil eder.
#Xml çağrısı yapılıp servis cevabı ekranda gösterilmek üzere views kısmına çağrının yapıldığı yere gönderilir.
#İstenen Xml metni convert_to_xml metodu sayesinde oluşturulur.
class MarketPlaceMPSaleRequest:
    ServiceType=""
    OperationType=""
    Token=""
    CreditCardInfo=""
    Price=""
    MPAY=""
    ExtraParam=""
    Description=""
    IPAddress=""
    Port=""
    ErrorURL=""
    SuccessURL=""
    InstallmentCount=""
    CommissionRate=""
    SubPartnerId=""
    PaymentContent=""
    CardTokenization=""

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
        Price=SubElement(main_root,'Price')
        Price.text=req.Price
        MPAY=SubElement(main_root,'MPAY')
        MPAY.text=req.MPAY
        ExtraParam=SubElement(main_root,'ExtraParam')
        ExtraParam.text=req.ExtraParam
        Description=SubElement(main_root,'Description')
        Description.text=req.Description
        IPAddress=SubElement(main_root,'IPAddress')
        IPAddress.text=req.IPAddress
        Port=SubElement(main_root,'Port')
        Port.text=req.Port
        ErrorURL=SubElement(main_root,'ErrorURL')
        ErrorURL.text=req.ErrorURL
        SuccessURL=SubElement(main_root,'SuccessURL')
        SuccessURL.text=req.SuccessURL
        InstallmentCount=SubElement(main_root,'InstallmentCount')
        InstallmentCount.text=req.InstallmentCount
        CommissionRate=SubElement(main_root,'CommissionRate')
        CommissionRate.text=req.CommissionRate
        SubPartnerId=SubElement(main_root,'SubPartnerId')
        SubPartnerId.text=req.SubPartnerId
        PaymentContent=SubElement(main_root,'PaymentContent')
        PaymentContent.text=req.PaymentContent


        token_root=SubElement(main_root, 'Token')
        UserCode = SubElement(token_root, 'UserCode')
        UserCode.text = req.Token.UserCode
        Pin = SubElement(token_root, 'Pin')
        Pin.text = req.Token.Pin   
         
        creditcardinfo_root=SubElement(main_root, 'CreditCardInfo')
        CreditCardNo = SubElement(creditcardinfo_root, 'CreditCardNo')
        CreditCardNo.text = req.CreditCardInfo.CreditCardNo
        OwnerName= SubElement(creditcardinfo_root, 'OwnerName')
        OwnerName.text = req.CreditCardInfo.OwnerName
        ExpireYear= SubElement(creditcardinfo_root, 'ExpireYear')
        ExpireYear.text = req.CreditCardInfo.ExpireYear
        ExpireMonth= SubElement(creditcardinfo_root, 'ExpireMonth')
        ExpireMonth.text = req.CreditCardInfo.ExpireMonth
        Cvv= SubElement(creditcardinfo_root, 'Cvv')
        Cvv.text = req.CreditCardInfo.Cvv

        cardTokenization_root=SubElement(main_root, 'CardTokenization')
        RequestType = SubElement(cardTokenization_root, 'RequestType')
        RequestType.text = req.CardTokenization.RequestType
        CustomerId = SubElement(cardTokenization_root, 'CustomerId')
        CustomerId.text = req.CardTokenization.CustomerId
        ValidityPeriod = SubElement(cardTokenization_root, 'ValidityPeriod')
        ValidityPeriod.text = req.CardTokenization.ValidityPeriod
        CCTokenId = SubElement(cardTokenization_root, 'CCTokenId')
        CCTokenId.text = req.CardTokenization.CCTokenId


        result = tostring(main_root).decode('utf-8')


        return (result)