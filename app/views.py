from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe

from .models import Item


def index(request, item_id):
    item = Item.objects.get(id=item_id)
    response = render(request, 'index.html', context={'item': item})
    return response


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {"publicKey": settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request, item_id):
    if request.method == "GET":
        domain_url = "http://localhost:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item = get_object_or_404(Item, pk=item_id)
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url,
                cancel_url=domain_url,
                payment_method_types=["card"],
                mode="payment",
                line_items=[
                    {
                        "price_data": {
                            "currency": item.currency,
                            "product_data": {
                                "name": item.name,
                            },
                            "unit_amount": item.price * 100,
                        },
                        "quantity": 1,
        },
                ]
            )
            return JsonResponse({"sessionId": checkout_session["id"]})
        except Exception as e:
            return JsonResponse({"error": str(e)})
