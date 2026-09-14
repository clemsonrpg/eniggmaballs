from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse
from .forms import EnigmaForm
from enigma.models import Enigma
from django.http import FileResponse
from django.conf import settings
from pathlib import Path


def memento(request):

    form = EnigmaForm()

    if request.method == "POST":

        form = EnigmaForm(request.POST)

        if form.is_valid():

            resposta = form.cleaned_data["senha"].strip().lower()

            try:
                enigma = Enigma.objects.get(id=2)

            except Enigma.DoesNotExist:

                if request.headers.get(
                    "X-Requested-With"
                ) == "XMLHttpRequest":

                    return JsonResponse({
                        "success": False
                    })

                form.add_error(
                    "senha",
                    "Arquivo não encontrado."
                )

                return render(
                    request,
                    "memento.html",
                    {
                        "form": form
                    }
                )


            senha_banco = enigma.senha.strip().lower()


            if resposta == senha_banco:

                if request.headers.get(
                    "X-Requested-With"
                ) == "XMLHttpRequest":

                    return JsonResponse({
                        "success": True,
                        "redirect": reverse("origem")
                    })

                return redirect("origem")


            if request.headers.get(
                "X-Requested-With"
            ) == "XMLHttpRequest":

                return JsonResponse({
                    "success": False
                })


            form.add_error(
                "senha",
                "Resposta incorreta."
            )


    return render(
        request,
        "memento.html",
        {
            "form": form
        }
    )


from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from pathlib import Path


def origem(request):

    return render(
        request,
        "origem.html"
    )


def download_memento(request):

    arquivo = (
        Path(settings.MEDIA_ROOT)
        / "memento_002.rar"
    )

    if not arquivo.exists():

        raise Http404(
            "Arquivo memento_002.rar não encontrado."
        )

    return FileResponse(
        open(arquivo, "rb"),
        as_attachment=True,
        filename="memento_002.rar"
    )