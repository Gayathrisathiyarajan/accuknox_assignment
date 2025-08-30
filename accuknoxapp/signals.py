import time, threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("\n=== SIGNAL TEST START ===")
    
    # Q1: Sync check
    print("Signal handler started...")
    time.sleep(2)
    print("Signal handler finished.")

    # Q2: Thread check
    print("Signal Thread:", threading.current_thread().name)

    # Q3: Transaction check
    print("Signal: Inside transaction? ->", connection.in_atomic_block)

    print("=== SIGNAL TEST END ===\n")
