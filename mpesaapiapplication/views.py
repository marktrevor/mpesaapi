from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def index(request):
    cl = MpesaClient()
    phone_number = '0758159045'
    amount = 1
    account_referrence = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_referrence)
    return HttpResponse(response)


def stk_push_callback(request):
    data = request.body
    return HttpResponse('Stk push in Django')
