from django.shortcuts import render

from To_Deploy.app_to_deploy.models import KeyWord


def show_hello_world(request):
    context = {
        'message': 'Hello, World!',
        # 'secret_message': KeyWord.objects.all().get()
    }
    return render(request, 'hello.html', context)
