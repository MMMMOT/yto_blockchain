from django import forms

class TransactionForm(forms.Form):
    tx_data = forms.CharField(label='请输入', max_length=100)

class IndexQueryForm(forms.Form):
    index = forms.IntegerField(label='请输入')

