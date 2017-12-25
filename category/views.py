# -*- coding: utf-8 -*-



from django.shortcuts import render
from .models import Category
from django.views.generic import ListView
from django import forms



class Category_List_Form(forms.Form):

    order_by = forms.ChoiceField(choices = (
        ('title','Title asc'),
        ('-title', 'Title desc'),
        ('id','ID'),
    ),required = False)
    search = forms.CharField(required = False)

class Category_list(ListView):

    model = Category
    context_object_name = 'categories'
    template_name = "category/category_list.html"
    paginate_by = 5

    def get_queryset(self):
        q = super(Category_list, self).get_queryset()
        self.form = Category_List_Form(self.request.GET)
        if self.form.is_valid():

            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(Category_list, self).get_context_data(**kwargs)
        context['searchform'] = self.form
        return context



def Category_page (request, pk=None):
    category = Category.objects.get(pk=pk)
    return render (request, 'category/category_page.html', {'category': category}, )



