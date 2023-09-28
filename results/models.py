from django.db import models

class Results(models.Model):
    sport = models.CharField('Вид спорта',max_length=100)
    tournament = models.CharField('Турнир',max_length=100)
    team_1 = models.CharField('Команда 1',max_length=100)
    team_2 = models.CharField('Команда 2',max_length=100)
    score_1 = models.IntegerField('Очки команды 1')
    score_2 = models.IntegerField('Очки команды 2')
    date_1 = models.DateField('Дата матча')

    def __str__(self):
        return f"{self.sport} | {self.team_1} | {self.team_2} | {self.date_1}"

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
