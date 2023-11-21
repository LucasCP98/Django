from django import forms


class LoguinForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João Silva"
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha..."
            }
        )
    )


class CadastroForms(forms.Form):
    nome_completo = forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João Silva"
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: joãosilva@gmail.com"
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha..."
            }
        )
    )
    confirmar_senha = forms.CharField(
        label='Confirmar senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente..."
            }
        )
    )

    def clean_nome_completo(self):
        nome = self.cleaned_data.get("nome_completo")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possivel inserir espaços dentro do campo Nome Completo.")
            else:
                return nome

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get("senha")
        confirmar_senha = self.cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError("Senhas não são iguais.")
            else:
                return confirmar_senha
