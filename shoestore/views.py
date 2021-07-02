#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.urls import reverse
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from api.models import Shoe, Order
import json
import boto3
import uuid


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class HomeView(TemplateView):

    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def get(
        self,
        request,
        *args,
        **kwargs
        ):
        context = {'shoe_list': Shoe.objects.all().order_by('reference'
                   )}
        return render(request, self.template_name, context)


class OrderView(View):

    def post(
        self,
        request,
        *args,
        **kwargs
        ):
        pid = request.POST.get('shoe_id', None)
        shoe = Shoe.objects.get(id=pid)

        order = Order()
        order.order_id = str(uuid.uuid4())
        order.client = str(get_client_ip(request))
        order.shoe_reference = shoe
        order.size = shoe.available_sizes.first()
        order.save()

        json_data = {
            'order_id': order.order_id,
            'client': order.client,
            'shoe': shoe.reference,
            'amount': str(shoe.price),
            }

        s3 = boto3.resource('s3',
                            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        filename = str(uuid.uuid4()) + '.json'
        s3object = s3.Object('garyk-static', filename)
        s3object.put(Body=bytes(json.dumps(json_data).encode('UTF-8')))

        json_data.update({'id': order.id})
        return HttpResponse(json.dumps(json_data), content_type="application/json")


class SummaryView(TemplateView):

    template_name = 'order_summary.html'

    def get(
        self,
        request,
        *args,
        **kwargs
        ):
        order = Order.objects.get(id=kwargs['order_pid'])
        shoe = Shoe.objects.get(reference=order.shoe_reference)
        context = {
            'order_id': order.order_id,
            'client': order.client,
            'shoe': shoe.reference,
            'amount': str(shoe.price),
            }
        return render(request, self.template_name, context)


