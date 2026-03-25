from django.shortcuts import render, redirect
from datetime import datetime
import pytz
from .forms import useraccountForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import useraccount


def home(request):
    return render(request, 'adminapp/projecthomepage.html')


def printer(request):
    user_input = ""

    if request.method == "POST":
        user_input = request.POST.get('klu')

    context = {'klu': user_input}
    return render(request, 'adminapp/printer.html', context)


def timetable(request):
    return render(request, 'adminapp/timetable.html')


def time1(request):
    timezone_input = ""
    current_time = ""

    if request.method == "POST":
        timezone_input = request.POST.get('klu')

        try:
            tz = pytz.timezone(timezone_input)
            current_time = datetime.now(tz)
        except Exception:
            current_time = "Invalid Timezone!"

    context = {
        "klu": timezone_input,
        "time": current_time
    }

    return render(request, 'adminapp/time1.html', context)


def signup(request):
    if request.method == "POST":
        form = useraccountForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # 👈 IMPORTANT: capture object

            # 🔐 hash password before saving
            user.password = make_password(form.cleaned_data['password'])

            user.save()  # 👈 now save properly
            return redirect('admin_home')
    else:
        form = useraccountForm()

    return render(request, 'adminapp/signup.html', {'form': form})
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = useraccount.objects.get(email=email)

            # 🔐 check hashed password
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('admin_home')
            else:
                error = "Invalid password"

        except useraccount.DoesNotExist:
            error = "User does not exist"

        return render(request, 'adminapp/login.html', {'error': error})

    return render(request, 'adminapp/login.html')