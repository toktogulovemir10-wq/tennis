from django.conf import settings


def author(request):
    return {"AUTHOR": {
        "name": settings.AUTHOR_NAME,
        "tg": settings.AUTHOR_TG,
        "bot": settings.AUTHOR_BOT,
        "site": settings.AUTHOR_SITE,
    }}
