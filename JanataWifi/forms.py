from django import forms 
from .models import Stock



class StockForm(forms.ModelForm):
    class Meta: 
        model = Stock
        fields = ['trade_code', 'date', 'open', 'high', 'low', 'close', 'volume']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'trade_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Trade Code'}),
            'open': forms.TextInput(attrs={'class':'form-control','placeholder':'Open'}),
            'high': forms.TextInput(attrs={'class':'form-control','placeholder':'High'}),
            'low': forms.TextInput(attrs={'class':'form-control','placeholder':'Low'}),
            'close': forms.TextInput(attrs={'class':'form-control','placeholder':'Close'}),
            'volume': forms.TextInput(attrs={'class':'form-control','placeholder':'Volume'}),
            
        }
