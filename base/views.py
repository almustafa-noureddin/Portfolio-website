from django.shortcuts import render
from django.contrib import messages

from .models import (
		Skill,
		Social,
		UserProfile,
		BlogPost,
		Project,
		SkillCategory
	)

from django.views import generic
from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "base/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		blogs = BlogPost.objects.filter(is_active=True)
		projects = Project.objects.filter(is_active=True)
		skill_categories = SkillCategory.objects.all()
		skills = Skill.objects.all()
		socials = Social.objects.all()

		context["projects"] = projects
		context["blogs"] = blogs
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

class ProjectView(generic.ListView):
    model = Project
    template_name = "base/projects.html"
    context_object_name = "projects"
    paginate_by = 10

    def get_queryset(self):
        return Project.get_queryset().filter(is_active=True)

class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = "base/project-detail.html"
	context_object_name = "project"

class BlogView(generic.ListView):
    model = BlogPost
    template_name = "base/blog.html"
    context_object_name = "blogposts"
    paginate_by = 10
	
    def get_queryset(self):
        return BlogPost.get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
	model = BlogPost
	template_name = "base/blog-detail.html"
	context_object_name = "blogpost"
