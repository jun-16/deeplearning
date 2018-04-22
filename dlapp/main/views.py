from django.shortcuts import render, redirect
from django.views import generic
import base64
from cnn.predict import predict_file

class Home(generic.TemplateView):
    template_name = 'main/home.html'

def upload(request):
    files = request.FILES.getlist("files[]")

    if request.method == 'POST' and files:
        labels = []
        for file in files:
            labels.append(predict_file(file))

        result = []
        file = files[0]
        for file, label in zip(files, labels):
            file.seek(0)
            src = base64.b64encode(file.read()).decode("utf-8")
            result.append((src, label))
        context = {
            'result': result,
        }
        return render(request, 'main/result.html', context)
    else:
        return redirect('home')
