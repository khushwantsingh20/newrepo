from django import views
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
# from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.template import loader
from accounts.models import Profile

from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ProfileForm
def signin(request):
    
    if request.method=="POST":
        username = request.POST.get('uname')
        password = request.POST.get('passw')
        print(username, password)

        # check if user has entered correct credentials
        user = auth.authenticate(username=username, password=password)
        print(user)
        
        
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            # print("stage 3")
            messages.warning(request, f'account done not exit plz sign in')   
            # No backend authenticated the credentials
            return render(request, 'signin.html')
        
              
     
    return render(request,'signin.html')
       
    

# from django.views.generic import TemplateView


# class index(TemplateView):
#     template_name = "index.html"

# def index(request):
    
#     return render(request,'index.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),

            })
            to_email = form.cleaned_data.get('email')

        
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()
            messages.success(request, "we sent you the mail for confirmation please check...")
            return render(request, 'signin.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('signin')
        # login(request, user)
        # return redirect('home')
        # return render(request,'signin')
    else:
        return HttpResponse('Activation link is invalid!')
    



    #resetpassword
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):

#     template_name = 'password_reset.html'
#     email_template_name = 'password_reset_email.html'
#     subject_template_name = 'password_reset_subject.txt'
#     success_message = "We've emailed you for confirmation, " \
#                      "Please Check." \
                  
#     success_url = reverse_lazy('signin')
    
    

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you for confirmation, Please Check."
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            messages.error(self.request, 'No account with this email address exists.')
            return super().form_invalid(form)
        return super().form_valid(form)


def logout_user(request):
 logout(request)
#  messages.success(request, "You Have Been Logged Out...")
 return redirect('home')



# views.py


# @login_required
# def profile(request):
#     profile = Profile.objects.get(user=request.user)
#     return render(request, 'profile.html', {'profile': profile})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# @login_required
# def profile(request):
#     try:
#         profile = Profile.objects.get(user=request.user)
#         return render(request, 'profile.html', {'profile': profile})
#     except Profile.DoesNotExist:
#         if request.method == 'POST':
#             form = ProfileForm(request.POST)
#             if form.is_valid():
#                 profile = form.save(commit=False)
#                 profile.user = request.user
#                 profile.save()
#                 return render(request, 'profile.html', {'profile': profile})
#         else:
#             form = ProfileForm()

#         return render(request, 'create_profile.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'profile.html'
    create_profile_template = 'create_profile.html'

    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
            return render(request, self.template_name, {'profile': profile})
        except Profile.DoesNotExist:
            form = ProfileForm()
            return render(request, self.create_profile_template, {'form': form})

    def post(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None

        form = ProfileForm(request.POST, request.FILES, instance=profile )

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, self.template_name, {'profile': profile})

        return render(request, self.create_profile_template, {'form': form})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST , request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

# class EditProfileView(View):
#     template_name='edit_profile.html'

#     def get(request,self, *args, **kwargs):
#         # profile=Profile.objects.get(user=request.user)
#         form = ProfileForm()
#         return render(request,self.template_name,{'form':form})
    
#     def post(self, request, *args, **kwargs):
#         profile = Profile.objects.get(user=request.user)
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#         return render(request, self.template_name, {'form': form})



# views.py

# accounts/views.py

# views.py
# from django.shortcuts import render, get_object_or_404

# from .forms import UserProfileForm

# def checkout_page(request):
#     user_profile = get_object_or_404(Profile, user=request.user)

#     if request.method == 'POST' and request.is_ajax():
#         form = UserProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'Address updated successfully'})
#         else:
#             return JsonResponse({'error': 'Form is not valid'}, status=400)

#     return render(request, 'order.html', {'user_profile': user_profile})


# accounts/views.py
# myapp/views.py

from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomPasswordChangeForm

def change_password(request):
    if request.method == 'POST':
        try:  
            form = CustomPasswordChangeForm(request.user, request.POST)
        
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Update the session to prevent the user from being logged out
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')  # Redirect to the user's profile or any other desired page
        except Exception as e:
                messages.error(request, 'incorrect password.')
                return render(request, 'change_password.html', {'form': form})
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})

   