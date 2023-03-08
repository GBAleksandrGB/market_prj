from django.db import models
from django.conf import settings
from mainapp.models import Accommodation


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket')
    accommodation = models.ForeignKey(Accommodation,
                                      on_delete=models.CASCADE)
    nights = models.PositiveIntegerField(verbose_name='кол-во ночей',
                                         default=0)
    add_datetime = models.DateTimeField(verbose_name='время',
                                        auto_now_add=True)

    @property
    def accommodation_cost(self):
        """стоимость одного предложения компании"""

        return self.accommodation.price * self.nights

    @property
    def total_nights(self):
        """общее количество ночей по всем заказам в корзине"""

        _accommodation = Basket.objects.filter(user=self.user)
        _total_nights = sum(list(map(lambda x: x.nights, _accommodation)))
        return _total_nights

    @property
    def total_cost(self):
        """общая стоимость всех предложений пользователя в корзине"""

        _accommodation = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.accommodation_cost, _accommodation)))
        return _total_cost

    @staticmethod
    def get_items(pk):
        return Basket.objects.filter(pk=pk).first()
