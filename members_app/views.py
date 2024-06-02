from django.shortcuts import render, redirect
from .models import UserInput

def input_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        user_input_obj = UserInput.objects.create(input_text=user_input)
        request.session['user_input_id'] = user_input_obj.id
        return redirect('members_app:display_view')
    return render(request, 'input.html')

def display_view(request):
    user_input_id = request.session.get('user_input_id')
    if user_input_id:
        user_input_obj = UserInput.objects.get(id=user_input_id)
        user_input = user_input_obj.input_text
    else:
        user_input = 'No input received'
    return render(request, 'display.html', {'user_input': user_input})


def session_view(request):
    user_inputs = UserInput.objects.all()
    session_data = [input.input_text for input in user_inputs]
    request.session['user_inputs'] = session_data
    return render(request, 'session.html', {'user_inputs': session_data})
