

class Configs:
    '''
    Tüm çağrılarda kullanılacak ayarların tutulduğu sınıftır.
    Bu sınıf üzerinde size özel parametreler fonksiyonlar arasında taşınabilir.
    Bu sınıf üzerinde tüm sistemde kullanacağımız ayarları tutar ve bunlara göre işlem yaparız.
    '''

    def __init__(self, UserCode, Pin, BaseUrl):
        #UserCode - size başvurunuz sonucunda gönderilen UserCode bilgisini kullanınız.
        self.UserCode = UserCode
        #PPin  - size başvurunuz sonucunda gönderilen pin bilgisini kullanınız.
        self.Pin = Pin
        #Wirecard xml servisleri API url'lerinin bilgisini içerir.
        self.BaseUrl = BaseUrl
       
