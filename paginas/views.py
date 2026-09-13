from django.shortcuts import redirect, render
from .forms import EnigmaForm
from enigma.models import Enigma


def memento(request):
    form = EnigmaForm()

    if request.method == "POST":
        form = EnigmaForm(request.POST)

        if form.is_valid():
            resposta = form.cleaned_data["senha"].strip().lower()

            if resposta == "espelho":
                return redirect("final")

            form.add_error("senha", "Resposta incorreta.")

    return render(request, "memento.html", {
        "form": form
    })
