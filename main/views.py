from django.shortcuts import render_to_response
from django.shortcuts import render
from main.wirecard_lib.configs import Configs
from main.wirecard_lib.Helper import Helper
from main.wirecard_lib.ProApiRequest import ProApiRequest
from main.wirecard_lib.ApiPlusRequest import ApiPlusRequest
from main.wirecard_lib.SendInformationSmsRequest import SendInformationSmsRequest
from main.wirecard_lib.SubscriberSelectRequest import SubscriberSelectRequest
from main.wirecard_lib.SubscriberDetailRequest import SubscriberDetailRequest
from main.wirecard_lib.SubscriberDeactivateRequest import SubscriberDeactivateRequest
from main.wirecard_lib.CCProxySaleRequest import CCProxySaleRequest
from main.wirecard_lib.MarketPlaceAddSubPartnerRequest import MarketPlaceAddSubPartnerRequest
from main.wirecard_lib.MarketPlaceUpdateSubPartnerRequest import MarketPlaceUpdateSubPartnerRequest
from main.wirecard_lib.MarketPlaceDeactiveRequest import MarketPlaceDeactiveRequest
from main.wirecard_lib.MarketPlaceSale3DSecOrMpSaleRequest import MarketPlaceSale3DSecOrMpSaleRequest
from main.wirecard_lib.MarketPlaceReleasePaymentRequest import MarketPlaceReleasePaymentRequest
from main.wirecard_lib.WDTicketSale3DURLOrSaleUrlProxyRequest import WDTicketSale3DURLOrSaleUrlProxyRequest
from main.wirecard_lib.MarketPlaceMPSaleRequest import MarketPlaceMPSaleRequest
from main.wirecard_lib.Token import Token
from main.wirecard_lib.Input import Input
from main.wirecard_lib.ContactInfo import ContactInfo
from main.wirecard_lib.FinancialInfo import FinancialInfo
from main.wirecard_lib.CreditCardInfo import CreditCardInfo
from main.wirecard_lib.CardTokenization import CardTokenization
from main.wirecard_lib.Product import Product
from zeep import Client
from dateutil import parser
import uuid
from random import *
import xml.etree.ElementTree as ET
import json

config = Configs(
    #"Public Magaza Anahtarı
    # size mağaza başvurunuz sonucunda gönderilen public key (açık anahtar) bilgisini kullanınız.",
    '',
    #"Private Magaza Anahtarı
    # size mağaza başvurunuz sonucunda gönderilen privaye key (gizli anahtar) bilgisini kullanınız.",
    '',
    #Wirecard xml servisleri API url'lerinin  bilgisidir.
    'https://www.wirecard.com.tr/SGate/Gate', #BaseUrl
)

def BasicApi(request):
    return render(request,'index.html',locals())


def ProApi(request):
    message=""
    if request.POST:
        input_request= Input()
        input_request.MPAY = ""
        input_request.Content = "TLFN01-Telefon"
        input_request.SendOrderResult ="true"
        input_request.PaymentTypeId =request.POST.get('paymentTypeId')
        input_request.ReceivedSMSObjectId = "00000000-0000-0000-0000-000000000000"

        #region Product
        input_request.ProductList = []
        product = input_request.Product()
        product.ProductId = 0
        product.ProductCategory =request.POST.get('productCategoryId')
        product.ProductDescription="Telefon"
        product.Price = 0.01
        product.Unit = 1
        input_request.ProductList.append(product)
        #endregion
        
        input_request.SendNotificationSMS="true"
        input_request.OnSuccessfulSMS="basarili odeme yaptiniz"
        input_request.OnErrorSMS="basarisiz odeme yaptiniz"
        input_request.RequestGsmOperator=0
        input_request.RequestGsmType=0
        input_request.Url="http://127.0.0.1:8000/ProApi"
        input_request.SuccessfulPageUrl="http://127.0.0.1:8000/success"
        input_request.ErrorPageUrl="http://127.0.0.1:8000/fail"
        input_request.Country=""
        input_request.Currency=""
        input_request.Extra=""
        input_request.TurkcellServiceId="20923735"

        #region Token
        token_request= Token()
        token_request.UserCode=config.UserCode
        token_request.Pin=config.Pin
        #region EndToken
        req= ProApiRequest() 
        message =  req.execute(token_request,input_request) #Soap servis çağrısının başlatıldığı kısım. 
    return render_to_response('proApi.html', {'message': message})



def ApiPlus(request):
     message=""
     if request.POST:
        input_request= Input()
        input_request.MPAY = ""
        input_request.Gsm =request.POST.get('gsm')
        input_request.Content = "TLFN01-Telefon"
        input_request.SendOrderResult ="true"
        input_request.PaymentTypeId =request.POST.get('paymentTypeId')
        input_request.ReceivedSMSObjectId = "00000000-0000-0000-0000-000000000000"

      
        #region Product
        input_request.ProductList = []
        product = input_request.Product()
        product.ProductId = 0
        product.ProductCategory =request.POST.get('productCategoryId')
        product.ProductDescription="Telefon"
        product.Price = 0.01
        product.Unit = 1
        input_request.ProductList.append(product)
        #endregion
       

        input_request.SendNotificationSMS="true"
        input_request.OnSuccessfulSMS="basarili odeme"
        input_request.OnErrorSMS="basarisiz odeme"
        input_request.Url="localhost:3000/home/apiplus"
        input_request.RequestGsmOperator=0
        input_request.RequestGsmType=0
        input_request.Extra=""
        input_request.TurkcellServiceId="20923735"
        input_request.CustomerIpAddress="http://127.0.0.1:8000/ApiPlus"

        #region Token
        token_request= Token()
        token_request.UserCode=config.UserCode
        token_request.Pin=config.Pin
        #region EndToken

        req= ApiPlusRequest() 
        message =  req.execute(token_request,input_request) #Soap servis çağrısının başlatıldığı kısım. 
 
     return render_to_response('apiPlus.html', {'message': message})



def SendInformationSmsService(request):
    message=""
    if request.POST:
       input_request= Input()
       input_request.Gsm=request.POST.get('gsm') 
       input_request.Content=request.POST.get('content')
       input_request.RequestGsmOperator=0
       input_request.RequestGsmType=0

       #region Token
       token_request= Token()
       token_request.UserCode=config.UserCode
       token_request.Pin=config.Pin
       #region EndToken

       req= SendInformationSmsRequest() 
       message =  req.execute(token_request,input_request) #Soap servis çağrısının başlatıldığı kısım. 

    return render_to_response('sendInformationSms.html', {'message': message})

#Abonelik Listeleme Servisi
def SelectSubscriber(request):
    message=""
    if request.POST:

       #region Input 
       input_request=Input()
       input_request.ProductId=0 
       input_request.Gsm=request.POST.get('gsm') 
       input_request.OrderChannelId=request.POST.get('orderChannelId') 
       input_request.Active=request.POST.get('activeTypeId')  
       input_request.SubscriberType=request.POST.get('subscriberTypeId')  
       input_request.StartDateMin=parser.parse(request.POST.get('startDateMin')) 
       input_request.StartDateMax=parser.parse(request.POST.get('startDateMax')) 
       input_request.LastSuccessfulPaymentDateMin=parser.parse(request.POST.get('lastSuccessfulPaymentDateMin')) 
       input_request.LastSuccessfulPaymentDateMax=parser.parse(request.POST.get('lastSuccessfulPaymentDateMax')) 
       #endregion

       #region Token
       token_request= Token()
       token_request.UserCode=config.UserCode
       token_request.Pin=config.Pin
       #region EndToken

       req= SubscriberSelectRequest() 
       message =  req.execute(token_request,input_request) #Soap servis çağrısının başlatıldığı kısım. 
    return render_to_response('subscriberselect.html', {'message': message})

#Abonelik Detay 
def SelectSubscriberDetail(request):
    message=""
    if request.POST:

       input_request=Input()
       input_request.subscriberId=request.POST.get('subscriberId') 
       #endregion

       #region Token
       token_request= Token()
       token_request.UserCode=config.UserCode
       token_request.Pin=config.Pin
       #region EndToken 

       req= SubscriberDetailRequest()
       message= req.execute(token_request,input_request) #Soap servis çağrısının başlatıldığı kısım. 
    return render_to_response('subscriberdetail.html', {'message': message})

def DeactivateSubscriber(request):
    message=""
    if request.POST:
       input_request=Input()
       input_request.subscriberId=request.POST.get('subscriberId') 
       #endregion

       #region Token
       token_request= Token()
       token_request.UserCode=config.UserCode
       token_request.Pin=config.Pin
       #region EndToken 

       req= SubscriberDeactivateRequest()
       message= req.execute(token_request,input_request) #Soap servis çağrısının başlatıldığı kısım. 
    return render_to_response('subscriberdeactive.html', {'message': message}) 
#Ödeme Formu aracılığı ile ödeme
def CCProxySale(request):
    message=""
    if request.POST:
        req=CCProxySaleRequest()
        req.ServiceType = "CCProxy"
        req.OperationType = "Sale"
        req.MPAY = ""
        req.IPAddress = "127.0.0.1"
        req.PaymentContent = "BLGSYR01"
        req.Description = "Bilgisayar"
        req.InstallmentCount =request.POST.get('installmentCount')
        req.ExtraParam = ""
       
        #region Token
        req.Token=Token()
        req.Token.UserCode=config.UserCode
        req.Token.Pin=config.Pin
        #endregion

        #region CreditCardInfo
        req.CreditCardInfo = CreditCardInfo()
        req.CreditCardInfo.CreditCardNo =request.POST.get('creditCardNo')
        req.CreditCardInfo.OwnerName =request.POST.get('ownerName')
        req.CreditCardInfo.ExpireYear =request.POST.get('expireYear')
        req.CreditCardInfo.ExpireMonth =request.POST.get('expireMonth')
        req.CreditCardInfo.Cvv =request.POST.get('cvv')
        req.CreditCardInfo.Price = "1";#0,01 TL
        #endregion
        message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım

       

    return render_to_response('ccProxySaleRequest.html', {'message': message}) 

def WDTicketSale3DURLProxy(request):
     message=""
     if request.POST:
         req=WDTicketSale3DURLOrSaleUrlProxyRequest()
         req.ServiceType="WDTicket"
         req.OperationType="Sale3DSURLProxy"
         req.Price = "1"; #0,01 TL
         req.MPAY = ""
         req.ErrorURL = "http://127.0.0.1:8000/Fail"
         req.SuccessURL = "http://127.0.0.1:8000/Success"
         req.ExtraParam = ""
         req.PaymentContent = "Bilgisayar"
         req.Description = "BLGSYR01"

         #region Token
         req.Token=Token()
         req.Token.UserCode=config.UserCode
         req.Token.Pin=config.Pin
         #endregion
         message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım
        
     return render_to_response('wdTicketSale3DURLProxy.html', {'message': message}) 
def WDTicketSaleURLProxy(request):
     message=""
     if request.POST:
         req=WDTicketSale3DURLOrSaleUrlProxyRequest()
         req.ServiceType="WDTicket"
         req.OperationType="SaleURLProxy"
         req.Price = "1"; #0,01 TL
         req.MPAY = ""
         req.ErrorURL = "http://127.0.0.1:8000/Fail"
         req.SuccessURL = "http://127.0.0.1:8000/Success"
         req.ExtraParam = ""
         req.PaymentContent = "Bilgisayar"
         req.Description = "BLGSYR01"

         #region Token
         req.Token=Token()
         req.Token.UserCode=config.UserCode
         req.Token.Pin=config.Pin
         #endregion
         message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım
     return render_to_response('wdTicketSaleURLProxy.html', {'message': message}) 

def MarketPlaceAddSubPartner(request):
    message=""
    if request.POST:
        req= MarketPlaceAddSubPartnerRequest()
        req.ServiceType="CCMarketPlace"
        req.OperationType="AddSubPartner"
        req.UniqueId=str(randint(1, 10000))
        req.SubPartnerType=request.POST.get('subPartnerType')
        req.Name=request.POST.get('name')

        #region Token
        req.Token=Token()
        req.Token.UserCode=config.UserCode
        req.Token.Pin=config.Pin
        #endregion

        #region Contactinfo Bilgileri
        req.ContactInfo= ContactInfo()
        req.ContactInfo.Country = "TR"
        req.ContactInfo.City = "34"
        req.ContactInfo.Address = "aaaa"
        req.ContactInfo.MobilePhone =request.POST.get('mobilePhoneNumber')
        req.ContactInfo.BusinessPhone = "2121111111"
        #endregion

        #region Financialinfo Bilgileri
        req.FinancialInfo = FinancialInfo()
        req.FinancialInfo.IdentityNumber =request.POST.get('identityNumber')
        req.FinancialInfo.TaxOffice = "istanbul"
        req.FinancialInfo.TaxNumber = "11111111111"
        req.FinancialInfo.BankName = "0012"
        req.FinancialInfo.IBAN = "TR330006100519786457841326"
        req.FinancialInfo.AccountName = "Ahmet Yasar"
        #endregion
        message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım
       
    return render_to_response('marketplaceAddSubPartner.html', {'message': message})
        
def MarketPlaceUpdateSubPartner(request):
    message=""
    if request.POST:
        req=MarketPlaceUpdateSubPartnerRequest()
        req.ServiceType="CCMarketPlace"
        req.OperationType="UpdateSubPartner"
        req.UniqueId=str(randint(1, 10000))
        req.SubPartnerType=request.POST.get('subPartnerType')
        req.SubPartnerId=request.POST.get('subPartnerId')
        req.Name=request.POST.get('name')

        #region Token
        req.Token=Token()
        req.Token.UserCode=config.UserCode
        req.Token.Pin=config.Pin
        #endregion

        #region Contactinfo Bilgileri
        req.ContactInfo= ContactInfo()
        req.ContactInfo.Country = "TR"
        req.ContactInfo.City = "34"
        req.ContactInfo.Address = "Istanbul Turkey"
        req.ContactInfo.MobilePhone =request.POST.get('mobilePhoneNumber')
        req.ContactInfo.BusinessPhone = "2121111111"
        #endregion

        #region Financialinfo Bilgileri
        req.FinancialInfo = FinancialInfo()
        req.FinancialInfo.IdentityNumber =request.POST.get('identityNumber')
        req.FinancialInfo.TaxOffice = "istanbul"
        req.FinancialInfo.TaxNumber = "11111111111"
        req.FinancialInfo.BankName = "0012"
        req.FinancialInfo.IBAN = "TR330006100519786457841326"
        req.FinancialInfo.AccountName = "Ahmet Yasar"
        #endregion
        message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım
    return render_to_response('marketplaceUpdateSubPartner.html', {'message': message})
def MarketPlaceDeactiveSubPartner(request):
    message=""
    if request.POST:

        req= MarketPlaceDeactiveRequest()
        req.ServiceType="CCMarketPlace"
        req.OperationType="DeactivateSubPartner"

        #region Token
        req.Token=Token()
        req.Token.UserCode=config.UserCode
        req.Token.Pin=config.Pin
        #endregion

        req.UniqueId=request.POST.get('uniqueId')
        message = req.execute(req,config)
    return render_to_response('marketplaceDeactiveSubPartner.html', {'message': message})

def MarketPlaceSale3DSec(request):
    message=""
    if request.POST:
        req=MarketPlaceSale3DSecOrMpSaleRequest()
        req.ServiceType = "CCMarketPlace"
        req.OperationType = "Sale3DSEC"
        req.MPAY = ""
        req.IPAddress = "127.0.0.1"
        req.Port = "123"
        req.Description = "Bilgisayar"
        req.InstallmentCount =request.POST.get('installmentCount')
        req.CommissionRate = "100"; #komisyon oranı 1. 100 ile çarpılıp gönderiliyor
        req.ExtraParam = ""
        req.PaymentContent = "BLGSYR01"
        req.SubPartnerId =request.POST.get('subPartnerId')
        req.ErrorURL = "http://127.0.0.1:8000/MarketPlaceError"
        req.SuccessURL = "http://127.0.0.1:8000/home/MarketPlaceSuccess"

        #region Token
        req.Token=Token()
        req.Token.UserCode=config.UserCode
        req.Token.Pin=config.Pin
        #endregion

        #region CreditCardInfo
        req.CreditCardInfo = CreditCardInfo()
        req.CreditCardInfo.CreditCardNo =request.POST.get('creditCardNo')
        req.CreditCardInfo.OwnerName =request.POST.get('ownerName')
        req.CreditCardInfo.ExpireYear =request.POST.get('expireYear')
        req.CreditCardInfo.ExpireMonth =request.POST.get('expireMonth')
        req.CreditCardInfo.Cvv =request.POST.get('cvv')
        req.CreditCardInfo.Price = "1";#0,01 TL
        #endregion
        message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım
    return render_to_response('marketplaceSale3DSec.html', {'message': message})

def MarketPlaceMPSale(request):
    message=""
    if request.POST:
        req=MarketPlaceMPSaleRequest()
        req.ServiceType = "CCMarketPlace"
        req.OperationType = "MPSale"
        req.Price="1" #0.01 TL
        req.MPAY = "01"
        req.IPAddress = "127.0.0.1"
        req.Port = "123"
        req.Description = "Bilgisayar"
        req.InstallmentCount =request.POST.get('installmentCount')
        req.CommissionRate = "1"; #komisyon oranı 1. 100 ile çarpılıp gönderiliyor
        req.ExtraParam = ""
        req.PaymentContent = "BLGSYR01"
        req.SubPartnerId =request.POST.get('subPartnerId')
        req.ErrorURL = "http://127.0.0.1:8000/MarketPlaceError"
        req.SuccessURL = "http://127.0.0.1:8000/home/MarketPlaceSuccess"

        #region Token
        req.Token=Token()
        req.Token.UserCode=config.UserCode
        req.Token.Pin=config.Pin
        #endregion

        #region CreditCardInfo
        req.CreditCardInfo = CreditCardInfo()
        req.CreditCardInfo.CreditCardNo =request.POST.get('creditCardNo')
        req.CreditCardInfo.OwnerName =request.POST.get('ownerName')
        req.CreditCardInfo.ExpireYear =request.POST.get('expireYear')
        req.CreditCardInfo.ExpireMonth =request.POST.get('expireMonth')
        req.CreditCardInfo.Cvv =request.POST.get('cvv')
        #endregion
       
        #region CardTokenization
        req.CardTokenization = CardTokenization()
        req.CardTokenization.RequestType="0"
        req.CardTokenization.CustomerId="01"
        req.CardTokenization.ValidityPeriod="0"
        req.CardTokenization.CCTokenId=str(uuid.uuid4())

        #endregion
        message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım
    return render_to_response('marketplaceMpSale.html', {'message': message})

def MarketPlaceReleasePayment(request):
     message=""
     if request.POST:
        req=MarketPlaceReleasePaymentRequest()
        req.ServiceType = "CCMarketPlace"
        req.OperationType = "ReleasePayment"
        req.SubPartnerId =request.POST.get('subPartnerId') 
        req.CommissionRate = "100"; #%1
        req.MPAY = ""
        req.OrderId=str(uuid.uuid4())
        req.Description = "Bilgisayar ödemesi"
        #region Token
        req.Token=Token()
        req.Token.UserCode=config.UserCode
        req.Token.Pin=config.Pin
        #endregion 
        message = req.execute(req,config) # Xml servis çağrısının başlatıldığı kısım
     return render_to_response('marketplaceReleasePayment.html', {'message': message})

def success(request):
     return render(request,'success.html',locals())

def fail(request):
     return render(request,'fail.html',locals())
