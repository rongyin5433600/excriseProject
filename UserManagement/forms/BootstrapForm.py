from django import forms


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
