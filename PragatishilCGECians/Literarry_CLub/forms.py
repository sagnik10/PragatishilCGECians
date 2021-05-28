from django import forms
from .models import PragatishilModel,PepTalksUserModel,AriettaUserModel,DebateUserModel,LiterarryUserModel,PratibimbaUserModel,TechonicsUserModel,RongmilantiUserModel


# create a ModelForm
class PragatishilModelForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = PragatishilModel
        fields = "__all__"

class PepTalksUserModelForm(forms.ModelForm):
    class Meta:
        model = PepTalksUserModel
        fields = "__all__"

class AriettaUserModelForm(forms.ModelForm):
    class Meta:
        model = AriettaUserModel
        fields = "__all__"

class DebateUserModelForm(forms.ModelForm):
    class Meta:
        model = DebateUserModel
        fields = "__all__"

class LiterarryUserModelForm(forms.ModelForm):
    class Meta:
        model = LiterarryUserModel
        fields = "__all__"

class PratibimbaUserModelForm(forms.ModelForm):
    class Meta:
        model = PratibimbaUserModel
        fields = "__all__"

class RongmilantiUserModelForm(forms.ModelForm):
    class Meta:
        model = RongmilantiUserModel
        fields = "__all__"

class TechonicsUserModelForm(forms.ModelForm):
    class Meta:
        model = TechonicsUserModel
        fields = "__all__"