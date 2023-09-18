from django.shortcuts import render, redirect
from django.urls import reverse
from apps.core.models import Course, Video, Chat

class CourseView:
  template = 'core/course_view.html'
  course_model = Course

  course_list_url = reverse('course_list')
  course_preview_url = reverse('course_preview')
  course_view_url = reverse('course_view')

  def get(self, request):
    
    context = {
      'course': self.course_model
    }
    return render(request, template_name=self.template, context=context)
  
  def post(self, request):
    
    return redirect(self.course_preview_url)