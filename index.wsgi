import sae
from a11ns import wsgi

application = sae.create_wsgi_app(wsgi.application)