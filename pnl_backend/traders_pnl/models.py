from django.db import models


class TradersPnl(models.Model):
    trader_name = models.CharField(max_length=50)
    trading_pnl = models.FloatField()
    position_pnl = models.FloatField()

    def __str__(self):
        return f'{self.trader_name}: ({self.trading_pnl}, {self.position_pnl})'
