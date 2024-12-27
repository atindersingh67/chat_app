# """
# ASGI config for chat_app project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

# application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = ProtocolTypeRouter({
    # HTTP requests are handled by Django ASGI application
    "http": get_asgi_application(),
    
    # WebSocket requests are routed to the Channels consumers
    "websocket": AllowedHostsOriginValidator(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})