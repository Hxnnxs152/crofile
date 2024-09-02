from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'filemanager/upload.html', {'form': form})

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'filemanager/file_list.html', {'files': files})
