from django.shortcuts import render

def about_page(request):
  template = 'pages/about.html'

  context = {}
  return render(request, template_name=template, context=context)

def privacy_page(request):
  template = 'pages/privacy.html'
  
  context = {}
  return render(request, template_name=template, context=context)

def policy_page(request):
  template = 'pages/policy.html'
  
  context = {}
  return render(request, template_name=template, context=context)