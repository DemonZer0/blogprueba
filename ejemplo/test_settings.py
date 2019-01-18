from .settings import *
#Database con memoria interna, para hacer pruebas rapidas con memoria interna
DATABASES = {
	"default":{
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": ":memory:",	
	}
}
#Para no enviar email a personas de verdad
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'