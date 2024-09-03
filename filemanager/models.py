from django.db import models
import os

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    @property
    def file_type(self):
        # Ermittelt den Dateityp basierend auf der Dateiendung
        ext = os.path.splitext(self.file.name)[1].lower()
        if ext in ['.jpg', '.jpeg', '.png', '.gif']:
            return 'image'
        elif ext in ['.pdf']:
            return 'pdf'
        elif ext in ['.doc', '.docx']:
            return 'doc'
        elif ext in ['.xls', '.xlsx']:
            return 'xls'
        else:
            return 'unknown'
