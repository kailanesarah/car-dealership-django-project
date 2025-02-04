from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openIA_API.client import open_ai_bio


def update_CarInventory():
    cars_count = Car.objects.count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] or 0
    
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        bio_ia = open_ai_bio(
            instance.model, instance.brand, instance.model_year)
        instance.bio = bio_ia


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print("POST_SAVE")
    update_CarInventory()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print("POST_DELETE")
    update_CarInventory()
