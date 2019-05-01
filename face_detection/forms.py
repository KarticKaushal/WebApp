from django import forms
from .models import ImageUploadModel

class UploadImageForm(forms.Form):
  #title = forms.CharField(max_length=50)
  #file = forms.FileField()
  image = forms.ImageField()

#######################>>>>>>>>>>>> for dface (Face_Detection) <<<<<<<<<<<<####################### 
class ImageUploadForm(forms.ModelForm):
  class Meta:
    model = ImageUploadModel
    fields = ('image', )