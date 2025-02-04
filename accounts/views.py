from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm



def RegisterAccounts(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect("ListViewCarlogin")
        else:
            messages.error(request, "Erro ao criar conta. Verifique os dados.")
    else:
        user_form = UserCreationForm()

    return render(
        request,
        "register.html",
        {'user_form': user_form}
    )


class LoginAccounts(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            print(f"Usuário autenticado {username}")
            return redirect('ListViewCars')
        else:
            return self.form_invalid(form)


def LogoutAccounts(request):
    logout(request)
    return redirect('ListViewCars')
