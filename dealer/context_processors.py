from .forms import SubscribeForm
from .models import Mail

def subscribe_form(request):
    if request.POST:
        form1=SubscribeForm(request.POST)
        if form1.is_valid():
            email=Mail()
            email.Email=form1.cleaned_data['Email']
            email.save()
    else:
        form1=SubscribeForm()
    return {'subscribe_form':SubscribeForm()}