from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import stripe
import datetime
from .models import Account

def customer_data():
    customers = stripe.Customer.list()
    customer_data = []
    for customer in customers.data:
        userD = {
            "Customer ID": customer.id,
            "Email Address": customer.email if customer.email else "Unknown",
            "Name": customer.name if customer.name else "Unknown",
            "Phone Number": customer.phone if customer.phone else "Unknown",
            "City": customer.address.city if customer.address and customer.address.city else "Unknown",
            "State": customer.address.state if customer.address and customer.address.state else "Unknown",
            "Country": customer.address.country if customer.address and customer.address.country else "Unknown",
            "Creation Date": format_date(customer.created) if customer.created else "Unknown"
        }
        customer_data.append(userD)
    
    return customer_data

def subscription_data():
    subscriptions = stripe.Subscription.list()
    subscription_data = []
    for subscription in subscriptions.data:
        subscription_info = {
            "Subscription ID": subscription.id,
            "Status": subscription.status,
            "Plan Name": subscription.plan.nickname if subscription.plan and subscription.plan.nickname else "Unknown",
            "Plan Amount": subscription.plan.amount if subscription.plan and subscription.plan.amount else "Unknown",
            "Billing Cycle": subscription.plan.interval if subscription.plan and subscription.plan.interval else "Unknown",
            "Start Date": format_date(subscription.start_date) if subscription.start_date else "Unknown",
            "End Date": format_date(subscription.current_period_end) if subscription.current_period_end else "Unknown",
            "Trial Period": subscription.plan.trial_period_days if subscription.plan else None,
            "Renewal Date": format_date(subscription.current_period_end) if subscription.current_period_end else "Unknown"
        }
        subscription_data.append(subscription_info)
    
    return subscription_data

def payment_data():
    payments = stripe.PaymentIntent.list()
    payment_data = []
    for payment in payments.data:
        payment_info = {
            "Payment ID": payment.id,
            "Amount": payment.amount,
            "Currency": payment.currency,
            "Payment Method": payment.payment_method if payment.payment_method else "Unknown",
            "Status": payment.status if payment.status else "Unknown",
            "Payment Date": format_date(payment.created) if payment.created else "Unknown"
        }
        payment_data.append(payment_info)
    
    return payment_data

def invoice_data():
    invoices = stripe.Invoice.list()
    invoice_data = []
    for invoice in invoices.data:
        invoice_data.append({
            "Invoice ID": invoice.id,
            "Customer ID": invoice.customer,
            "Amount Due": invoice.amount_due,
            "Amount Paid": invoice.amount_paid,
            "Due Date": invoice.due_date,
            "Status": invoice.status,
            "Invoice Date": format_date(invoice.created)
        })
    return invoice_data

def format_date(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date

def event_data():
    events = stripe.Event.list()
    event_data = []
    for event in events.data:
        event_info = {
            "Event ID": event.id,
            "Type": event.type,
            "Created Date": format_date(event.created),
            "Object Id":event.data.object.id if event.data and event.data.object else "Unknown",
            "Livemode":event.livemode,
            "Data Payload": event.data.object.object if event.data and event.data.object else "Unknown"
        }
        event_data.append(event_info)
    
    return event_data

def get_keys_by_name(name):
    try:
        account = Account.objects.get(name=name)
        return account.key
    except Account.DoesNotExist:
        return None
@api_view(['GET'])
def getCustomers(requests,account_name):
    
    stripe.api_key=get_keys_by_name(account_name)
    
    return Response(customer_data())
@api_view(['GET'])
def getInvoices(requests,account_name):
    
    stripe.api_key=get_keys_by_name(account_name)
    return Response(invoice_data())
@api_view(['GET'])
def getSubscriptions(requests,account_name):
    
    stripe.api_key=get_keys_by_name(account_name)
    return Response(subscription_data())
@api_view(['GET'])
def getEvents(requests,account_name):
    
    stripe.api_key=get_keys_by_name(account_name)
    return Response(event_data())
@api_view(['GET'])
def getPayments(requests,account_name):

    stripe.api_key=get_keys_by_name(account_name)
    return Response(payment_data())
@api_view(['GET'])
def getAdmins(requests):
    accounts = Account.objects.all().values('name', 'created')
    return Response(list(accounts))

@api_view(['POST'])
def createAccount(request):
    name = request.data.get('name')
    key = request.data.get('key')
    account = Account(name=name, key=key)
    account.save()
    return Response({"message": "Account created successfully"})
@api_view(['GET'])
def account_delete(request, account_name):
    account = get_object_or_404(Account, name=account_name)
    account.delete()
    return Response({'message': f'Account "{account_name}" deleted successfully.'})

