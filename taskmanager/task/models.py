from django.db import models


# Create your models here.


class Task(models.Model):

    RESPONSIBLES_DEFAULT = [
        ('AN', 'André Rodrigues'),
        ('WN', 'Wanderson Neres'),
        ('DS', 'Daniel Santos')
    ]

    PRIORITY = [
        ('LOW', 'Baixa'),
        ('AVERAGE', 'Média'),
        ('HIGH', 'Alta')
    ]

    title = models.CharField(max_length=150, blank=True,  verbose_name="Título")
    description = models.TextField(max_length=500, blank=True, verbose_name="Descrição")
    solution = models.TextField(max_length=500, null=True, blank=True, verbose_name="Solução")
    responsible = models.CharField(max_length=50, choices=RESPONSIBLES_DEFAULT, verbose_name="Responsável")
    priority = models.CharField(max_length=50, choices=PRIORITY, verbose_name="Prioridade")
    created_in = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    finalized_in = models.DateTimeField(null=True, blank=True, verbose_name="Finalizado em")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        db_table = "TBTarefas"
