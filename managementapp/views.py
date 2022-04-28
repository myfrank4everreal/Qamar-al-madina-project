from django.shortcuts import render



def index(requests):
    return render(requests, 'managementapp/index.html')



def about(requests):
    return render(requests, 'managementapp/about.html')

def contact(requests):
    return render(requests, 'managementapp/contact.html')

def services(requests):
    return render(requests, 'managementapp/services.html')

def portfolio(requests):
    return render(requests, 'managementapp/pricing.html')
