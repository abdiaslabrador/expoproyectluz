from django import forms
from .models import Lesson_det
from apps.exercise.models import Hour, Exercise


#------------------------------------------------------------------------------------------
#lesson
#------------------------------------------------------------------------------------------
class CreateLessonForm(forms.Form):
	
	day_lesson = forms.DateField(label = "Día:", required=True)
	


class CreateLessonSearchForm(forms.Form):
	#I create the exercise variable to show the exercise name
	exercise = forms.CharField(label='Tipo de ejercicio',required=True, max_length=64, widget=forms.TextInput(attrs={'readonly':'readonly'}))
	day_lesson = forms.DateField(label='Fecha', required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
	hour = forms.ModelChoiceField(label='Hora', required=True, queryset=Hour.objects.all())
	cant_max = forms.IntegerField(label='Cant max',required=True, min_value=0)


class SearchClassesForm(forms.Form):
	since = forms.DateField(required=True)
	until = forms.DateField(required=True)

	def clean(self):
		#here we have the username and the id
		clean = super().clean()
		since 	= self.cleaned_data.get("since")
		until 	= self.cleaned_data.get("until")

		if since is not None  and until is not None:
			if since > until:
				raise forms.ValidationError("'DESDE' no puede se mayor que 'HASTA'")
			return clean

class UpdateLessonForm(forms.ModelForm):
	day_lesson = forms.DateField(label='Fecha:', required=True, widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}))
	hour_chance = forms.TimeField(label="Hora chance:", required=True)
	hour_lesson	= forms.TimeField(label="Hora clase:", required=True)
	hour_end = forms.TimeField(label="Hora final: ", required=True)
	cant_max = forms.IntegerField(min_value = 0, required=True)

	class Meta:
		model= Lesson_det
		fields= (
					'day_lesson',
					'hour_chance',
					'hour_lesson',
					'hour_end',
					'cant_max',
				)
	def clean(self):
		#here we have the username and the id
		clean = super().clean()
		hour_chance 	= self.cleaned_data.get("hour_chance")
		hour_lesson 	= self.cleaned_data.get("hour_lesson")
		hour_end 	= self.cleaned_data.get("hour_end")

		
		if not(hour_chance != hour_lesson and hour_lesson != hour_end and hour_chance != hour_end):
			raise forms.ValidationError("Las horas no pueden ser iguales")
		

		if not (hour_chance < hour_lesson and hour_lesson < hour_end):
			raise forms.ValidationError("Hora de chance tiene que ser menor a la hora de la clase y la hora de la clase menor a la hora de finalización.")
		return clean