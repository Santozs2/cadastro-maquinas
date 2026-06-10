from django import forms 
from .models import Colaborador, Maquina

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'
        widgets = {
            'setor': forms.TextInput(
                attrs={'placeholder': 'Digite o setor do colaborador'}),
            'nome': forms.TextInput(
                attrs={'placeholder': 'Digite o nome do colaborador'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Digite o email do colaborador'}),
            'maquina': forms.Select(
                attrs={'placeholder': 'Selecione a máquina do colaborador'}),
        }

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__'
        widgets = {
            'nome_maquina': forms.TextInput(
                attrs={'placeholder': 'Digite o nome da máquina'}),
            'numero_patrimonio': forms.TextInput(
                attrs={'placeholder': 'Digite o número de patrimônio'}),
            'modelo': forms.TextInput(
                attrs={'placeholder': 'Digite o modelo da máquina'}),
            'setor': forms.TextInput(
                attrs={'placeholder': 'Digite o setor da máquina'}),
            'colaborador': forms.Select(
                attrs={'placeholder': 'Selecione o colaborador responsável pela máquina'}),
        }