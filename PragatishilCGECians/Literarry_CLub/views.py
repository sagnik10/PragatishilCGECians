from django.shortcuts import render
from .forms import PragatishilModelForm,PepTalksUserModelForm,AriettaUserModelForm,DebateUserModelForm,LiterarryUserModelForm,PratibimbaUserModelForm,RongmilantiUserModelForm,TechonicsUserModelForm
from django.conf import settings
from .models import PragatishilModel,PepTalksUserModel,AriettaUserModel,DebateUserModel,LiterarryUserModel,PratibimbaUserModel,RongmilantiUserModel,TechonicsUserModel
from django.core.mail import EmailMultiAlternatives

def home(request):
    return render(request, 'welcome_page_pragatishils.html')


def main_page(request):
    return render(request, 'PragatishilCGECians_Home_Page.html')


def register(request):
    if request.method == 'POST':
        form = PragatishilModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = PragatishilModel(name = name, email = email)
            subject = 'welcome to PragatishilCGECians'
            message = f'Hi {user.name}'
            html_content='<br><div><img src="https://drive.google.com/uc?export=download&id=14q6aQNKwqqBiQdavOlasY3gczm40y_R_" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering in PragatishilCGECians. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?export=download&id=17OPSdMsQ8k0-b1Fa8Z-ONIIZ0ARhkOEe" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Tapasree Kait</b>, contact number- 8420913317. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'PragatishilCGECians_Home_Page.html')
    else:
        form = PragatishilModelForm()
    return render(request, 'pragatishil_register.html', {'form': form})

def peptalks(request):
    return render(request,'PEP-TALKS.html')

def peptalksregister(request):
    if request.method == 'POST':
        form = PepTalksUserModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = PepTalksUserModel(name = name, email = email)
            subject = 'welcome to PepTalks CGEC'
            message = f'Hi {user.name}'
            html_content='<br><div><img src="https://drive.google.com/uc?export=download&id=14qd7cYWZG3TgV-IkS8Vj8uO8DwrzzugW" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering in PepTalks CGEC. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?id=1sVDI--4tLutfDvEut4jH1dZxDyH9S1Ju" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Sagnik Sen</b>, contact number- 6295862826. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'PEP-TALKS.html')
    else:
        form = PepTalksUserModelForm()
    return render(request, 'peptalksregister.html', {'form': form})

def Arietta_Home_Page(request):
    return render(request,'Arietta_Home_Page.html')

def Arietta_Register(request):
    if request.method == 'POST':
        form = AriettaUserModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = AriettaUserModel(name = name, email = email)
            subject = 'welcome to Arietta Music Club CGEC'
            message = f'Hi {user.name}'
            html_content='<br><div><img src=" https://drive.google.com/uc?export=download&id=1N-x1v8KBl-rQ8m-ND1YHIuvnUJJuQibS" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering in Arietta Music Club CGEC. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?export=download&id=1uiRO28NRqwGstYgmiLuwzU4dopNJbXQW" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Ayan Chakrabarty</b>, contact number- 7477868319. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'Arietta_Home_Page.html')
    else:
        form = AriettaUserModelForm()
    return render(request, 'Arietta_Register.html', {'form': form})


def Debate_Home_Page(request):
    return render(request,'Debate_Home_Page.html')

def Debate_Register(request):
    if request.method == 'POST':
        form = DebateUserModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = DebateUserModel(name = name, email = email)
            subject = 'welcome to Debate Club CGEC'
            message = f'Hi {user.name}'
            html_content='<br><div><img src=" https://drive.google.com/uc?export=download&id=1xgL1gRbgHZhfU4IR1GJX225hKoM6kAp1" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering in Debate Club CGEC. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?id=1Nxkm9eVUWObTi5S9sJWI3P13KgD9ReB1" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Sahasrak Bhattacharya</b>, contact number- 9064309163. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'Debate_Home_Page.html')
    else:
        form = DebateUserModelForm()
    return render(request, 'Debate_Register.html', {'form': form})

def Literarry_Home_Page(request):
    return render (request,'Literarry_Club_Home_Page.html')

def Literarry_Register(request):
    if request.method == 'POST':
        form = LiterarryUserModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = LiterarryUserModel(name = name, email = email)
            subject = 'welcome to Creative Pens CGEC'
            message = f'Hi {user.name}'
            html_content='<br><div><img src=" https://drive.google.com/uc?export=download&id=1-3xNdQV0tGBdb5l4iERE5EfnE3rmlFRq" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering iat Creative Pens CGEC. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?id=1QP87qNH5x3_HhhruatzaYvx49mhJvETM" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Swatilekha Roy</b>, contact number- 8637813901. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'Literarry_Club_Home_Page.html')
    else:
        form = LiterarryUserModelForm()
    return render(request, 'Literarry_Register.html', {'form': form})

def Pratibimba_Home_Page(request):
    return render (request,'Pratibimba_Home_Page.html')

def Pratibimba_Register(request):
    if request.method == 'POST':
        form = PratibimbaUserModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = PratibimbaUserModel(name = name, email = email)
            subject = 'welcome to Pratibimba Theatre Group CGEC'
            message = f'Hi {user.name}'
            html_content='<br><div><img src="https://drive.google.com/uc?export=download&id=1jOPUT_1tSHjtbKsIWLtN6HetRTpC-FRW" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering iat Pratibimba Theatre Group CGEC. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?export=download&id=17OPSdMsQ8k0-b1Fa8Z-ONIIZ0ARhkOEe" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Tapasree Kait</b>, contact number- 8420913317. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'Pratibimba_Home_Page.html')
    else:
        form = PratibimbaUserModelForm()
    return render(request, 'Pratibimba_Register.html', {'form': form})

def Rongmilanti_Home_Page(request):
    return render (request,'Rongmilanti_Home_Page.html')

def Rongmilanti_Register(request):
    if request.method == 'POST':
        form = RongmilantiUserModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = RongmilantiUserModel(name = name, email = email)
            subject = 'welcome to Rongmilanti CGEC'
            message = f'Hi {user.name}'
            html_content='<br><div><img src="https://drive.google.com/uc?export=download&id=1-aAsW0RqfYv1sDzpUb2uM_Z5yB_Ogxun" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering at Rongmilanti CGEC. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?id=1MMqxwF_GbY3XelpJom5gvxvQAOkNP7Yb" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Soumyajeet Sinha</b>, contact number- 7872403006. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'Rongmilanti_Home_Page.html')
    else:
        form = RongmilantiUserModelForm()
    return render(request, 'Rongmilanti_Register.html', {'form': form})

def Techonics_Home_Page(request):
    return render (request,'Techonics_Home_Page.html')

def Techonics_Register(request):
    if request.method == 'POST':
        form = TechonicsUserModelForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = TechonicsUserModel(name = name, email = email)
            subject = 'welcome to Techonics CGEC'
            message = f'Hi {user.name}'
            html_content='<br><div><img src="https://drive.google.com/uc?export=download&id=1g-v_SftT_duePEbmIEuTaOxewoniLG5w" style="width:100%; height: 700px; position: relative;"></div><br> thank you for registering at Techonics CGEC. Its glad to hear from you and thanks for asking to be a part of us. Your credentials are with us and we will mail you if you are considered to be a part of us.for more details you can contact with<br><br><div><img src="https://drive.google.com/uc?id=19NioX3rpmxUfF612GtOEcAYRlwd0mfms" style="width:100%; height: 700px; position: relative;"></div><br><br> <b>Ayush Gupta</b>, contact number- 8927246040. <br>Thank You.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            msg=EmailMultiAlternatives( subject, message, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form.save()        
            return render(request, 'Techonics_Home_Page.html')
    else:
        form = TechonicsUserModelForm()
    return render(request, 'Techonics_Register.html', {'form': form})