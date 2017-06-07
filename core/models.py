from django.db import models

class Banner(models.Model):
	image = models.ImageField('Banner', upload_to='banner')
	nome = models.CharField('Nome', max_length=100)
	promovido = models.BooleanField("Página principal")

	class Meta:
		verbose_name = 'Banner'
		verbose_name_plural = 'Banners'

	def __str__(self):
		return self.nome
