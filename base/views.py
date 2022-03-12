from django.shortcuts import render
from django.contrib import messages

from .models import (
		Skill,
		Social,
		UserProfile,
		SkillCategory
	)

from django.views import generic
from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "base/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		skill_categories = SkillCategory.objects.all()
		skills = Skill.objects.all()
		socials = Social.objects.all()

		context["skill_categories"] = skill_categories
		context["skills"] = skills
		context["socials"] = socials
		
		return context

class ContactView(generic.FormView):
	template_name = "base/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)



