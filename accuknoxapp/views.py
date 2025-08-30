from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import transaction, connection
import threading
import time


def test_signal(request):
    print("Before creating user")
    username = f"signal_test_{int(time.time())}"
    User.objects.create(username=username)
    return HttpResponse("Signal test completed! Check console logs.")

def test_signal_thread(request):
    print("Caller Thread:", threading.current_thread().name)
    username = f"thread_test_{int(time.time())}"
    User.objects.create(username=username)
    return HttpResponse("Thread test completed! Check console logs.")

def test_signal_transaction(request):
    with transaction.atomic():
        print("View: Inside transaction ->", connection.in_atomic_block)
        username = f"txn_test_{int(time.time())}"
        User.objects.create(username=username)

    return HttpResponse("Transaction test completed! Check console logs.")
