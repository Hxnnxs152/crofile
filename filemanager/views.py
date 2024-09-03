from django.shortcuts import render, redirect
from .models import UploadedFile  # Model für die Dateien
from .forms import FileUploadForm  # Formular für den Datei-Upload

# Funktion für Datei-Liste und Datei-Upload
def file_list(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')  # Redirect zurück zur Liste nach dem Upload
    else:
        form = FileUploadForm()
    
    files = UploadedFile.objects.all()  # Alle hochgeladenen Dateien abrufen
    return render(request, 'filemanager/file_list.html', {'files': files, 'form': form})
