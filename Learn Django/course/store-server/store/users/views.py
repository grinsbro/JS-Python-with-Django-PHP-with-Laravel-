from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from users.models import User, EmailVerification
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin
# Create your views here.

class UserLoginView(TitleMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'Авторизация'


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data = request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return redirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


class UserRegistrationView(SuccessMessageMixin, TitleMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегистрированы'
    title = 'Регистрация'



# def registration(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляем! Вы успешно зарегистрировались')
#             return redirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Профиль пользователя'

    def get_success_url(self):
        return reverse('users:profile', args=(self.object.id,))


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     context = {
#         'title':'Store - Профиль',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user),
#
#     }
#     return render(request, 'users/profile.html', context)


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Подтверждение почты'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('index'))