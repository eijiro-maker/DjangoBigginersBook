from django.core.mail import send_mail , EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . forms import ContactForm
from django.shortcuts import redirect

# Create your views here.

class Top(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    template_name = 'contact/top.html'

    def form_valid(self, form):
        subject = 'お問い合わせがありました'
        message = render_to_string('contact/mail.txt', form.cleaned_data, self.request)
        from_email = 'ejrhys@gmail.com'
        recipient_list = ['ejrhys@gmail.com']
        email = EmailMessage(subject, message, from_email, recipient_list)
#        send_mail(subject, message, from_email, recipient_list)
        email.attach_file('contact/img/test.jpg')
        email.send()
        return redirect('contact:thanks')

class Thanks(generic.TemplateView):
    template_name = 'contact/thanks.html'