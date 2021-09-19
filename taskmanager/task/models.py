from django.db import models


# Create your models here.


class Task(models.Model):

    RESPONSIBLES_DEFAULT = [
        ('AN', 'André Rodrigues'),
        ('WN', 'Wanderson Neres'),
        ('DS', 'Daniel Santos'),
        ('GS', 'Gláucio de Souza'),
        ('LC', 'Lumi Cassandra'),
        ('RG', 'Ricardo Galante')

    ]

    TYPE_TASK = [
        ('system change', 'Alteração de Sistema'),
        ('problem', 'Problema'),
        ('new feature', 'Novo Recurso'),
        ('sticky notes', 'Lembretes')
    ]

    PRIORITY = [
        ('LOW', 'Baixa'),
        ('AVERAGE', 'Média'),
        ('HIGH', 'Alta')
    ]

    title = models.CharField(max_length=300, blank=True,  verbose_name="Título")
    description = models.TextField(max_length=12000, blank=True, verbose_name="Descrição")
    type_task = models.CharField(max_length=50, blank=True, choices=TYPE_TASK, verbose_name="Tipo da Tarefa")
    responsible = models.CharField(max_length=50, choices=RESPONSIBLES_DEFAULT, verbose_name="Responsável")
    priority = models.CharField(max_length=50, choices=PRIORITY, verbose_name="Prioridade")
    created_in = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    solution = models.TextField(max_length=12000, null=True, blank=True, verbose_name="Solução")
    finalized_in = models.DateTimeField(null=True, blank=True, verbose_name="Finalizado em")
 
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        db_table = "TBTarefas"
