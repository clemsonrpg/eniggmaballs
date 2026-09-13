from django.shortcuts import redirect, render
from .forms import EnigmaForm
from enigma.models import Enigma


def index(request):
    resultado = None
    enigma = Enigma.objects.first()

    if request.method == "POST":
        form = EnigmaForm(request.POST)

        if form.is_valid():
            senha_digitada = form.cleaned_data["senha"].strip().lower()

            if enigma and senha_digitada == enigma.senha.strip().lower():
                return redirect("memento")
            else:
                resultado = "error"

    else:
        form = EnigmaForm()

    return render(request, "index.html", {
        "form": form,
        "resultado": resultado
    })