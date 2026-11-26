from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'service', 'purpose', 'duration', 'location', 'comment', 'consent']
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Иванов Иван / ООО Ромашка'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@mail.ru'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7 (999) 123-45-67'}),
            'purpose': forms.Textarea(attrs={'rows': 3}),
            'duration': forms.TextInput(attrs={'placeholder': 'Например: 3 дня'}),
            'location': forms.TextInput(attrs={'placeholder': 'Например: г. Якутск, ул. Ленина 1'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 10:
            raise forms.ValidationError("Пожалуйста, введите корректный номер телефона.")
        return phone
        
    def clean_consent(self):
        consent = self.cleaned_data.get('consent')
        if not consent:
            raise forms.ValidationError("Вы должны согласиться с политикой конфиденциальности.")
        return consent