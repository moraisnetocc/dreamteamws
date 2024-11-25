from django.db import models


class Country(models.Model):
    name = models.CharField("Nome do país", max_length=200, blank=False, null=False)
    flag = models.ImageField("Bandeira", blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "01. País"
        verbose_name_plural = "01. Países"


# Create your models here.
class PlayerModel(models.Model):
    MAIN_FOOT = (
        (1, "Destro"),
        (2, "Canhoto"),
        (3, "Ambidestro"),
    )
    name = models.CharField("Jogador", max_length=200, blank=False, null=False)
    age = models.IntegerField("Idade", blank=False, null=False)
    start = models.BooleanField("Estrela", default=False)
    nationality = models.ForeignKey(Country, verbose_name="País", blank=False, null=False, on_delete=models.CASCADE)
    salary = models.FloatField("Salário", blank=False, null=False)
    value = models.FloatField("Passe", blank=False, null=False)
    strong = models.IntegerField("Força", default=1)
    crossing = models.FloatField("Cruzamento", default=1.0)
    velocity = models.FloatField("Velocidade", default=1.0)
    kick = models.FloatField("Chute", default=1.0)
    head = models.FloatField("Cabecear", default=1.0)
    disarm = models.FloatField("Desarme", default=1.0)
    resistence = models.FloatField("Resistência", default=1.0)
    creation = models.FloatField("Armacao", default=1.0)
    touch = models.FloatField("Passe", default=1.0)
    dribble = models.FloatField("Drible", default=1.0)
    main_foot = models.IntegerField("Pé principal", choices=MAIN_FOOT, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "02. Jogador"
        verbose_name_plural = "03. Jogadores"


class Team(models.Model):
    name = models.CharField("Nome do país", max_length=200, blank=False, null=False)
    arms = models.ImageField("Brasão")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "01. País"
        verbose_name_plural = "01. Países"
