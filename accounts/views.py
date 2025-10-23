from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Parolingiz muvaffaqiyatli o\'zgartirildi!')
            return redirect('home')  # O'zgartirishingiz mumkin
        else:
            messages.error(request, 'Iltimos, xatolarni to\'g\'rilang.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})