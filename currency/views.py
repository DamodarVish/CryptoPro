from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')
    

def currency(request):
    url = "https://api.swapzone.io/v1/exchange/get-rate?from=btc&to=doge&amount=0.1&rateType=all&availableInUSA=false&chooseRate=best&noRefundAddress=false"
    headers = {
        'x-api-key': 'Gs7JK8J5x'
    }

    response = requests.request("GET", url, headers=headers).json()
    # breakpoint()
    return render(request, 'currency/currencies.html', context={'data':response})
    

   
