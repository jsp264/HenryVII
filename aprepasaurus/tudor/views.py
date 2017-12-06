#
# The Views module. Constructed to properly show the representations of our models appropriately
#
# Author: jsp264
# Date Modified: 12/3/2017


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .models import Tutor, Specialty, Seeker
from .forms import PhotoUploadForm, SubjectsForm, DegreeForm, ParentForm

import requests
import time

class IndexView(generic.ListView):
    template_name = 'tudor/index.html'
    context_object_name = 'available_tutors_list'

    def get_queryset(self):
        """
        Return the last five (changed to all) published questions (not including those set to be
        published in the future).
        """
        return Tutor.objects.filter(
            teaching_start_date__lte=timezone.now()
        ).order_by('-teaching_start_date')[:]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['seekers'] = Seeker.objects.all().order_by('join_date')[:]
        return context

class DetailView(generic.DetailView):
    model = Tutor
    template_name = 'tudor/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Tutor.objects.filter(teaching_start_date__lte=timezone.now())

class DetailSeekView(generic.DetailView):
    model = Seeker
    template_name = 'tudor/detail_seek.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Seeker.objects.filter(join_date__lte=timezone.now())

#################################################################################
############################ VIEW METHODS #######################################
#################################################################################

# tutor_upload logic may want to actually be in the model, not the view
def seek_upload(request):
    if request.method == 'POST':
        form  = PhotoUploadForm(request.POST, request.FILES)
        form2 = SubjectsForm(request.POST, request.FILES)
        form3 = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            newseek = Seeker(seek_name          = request.POST['name'],
                             join_date          = timezone.now(),
                             seekemail          = request.POST['tootemail'],
                             seek_photo         = request.FILES['docfile'],
                             is_parent          = True if request.POST['degree'] == 'Parent' else False,
                             seek_addr          = request.POST['address'],
                             desired_subjects   = ' '.join(request.POST.getlist('subjects')) if request.POST.getlist('subjects') else "NONE"
            )

            newseek.save()

            return HttpResponseRedirect(reverse('tudor:index'))
    else:
        form = PhotoUploadForm() # A empty, unbound form
        form2 = SubjectsForm()   # A empty, unbound form
        form3 = ParentForm()

    seeks = Seeker.objects.all()
    return render(request,
                  'tudor/seek_upload.html',
                  {'seekers': seeks, 'form': form, 'form2': form2, 'form3': form3}
    )



def tutor_upload(request):
    # Handle file upload
    if request.method == 'POST':
        #tzone = "https://maps.googleapis.com/maps/api/timezone/json?location=38.908133,-77.047119&timestamp=1458000000&key=AIzaSyDgYrnLvtV8en5ARq-MxhNM_vTsyMUf0QA"
        #taddr = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDIFo17NRLWr045Cl5UknH28ssW13pHsmI"
        form  = PhotoUploadForm(request.POST, request.FILES)
        form2 = SubjectsForm(request.POST, request.FILES)
        form3 = DegreeForm(request.POST, request.FILES)
        if form.is_valid():

            # clean address
            # TODO

            addr_info = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDIFo17NRLWr045Cl5UknH28ssW13pHsmI")
            addr_info_dict = addr_info.json()
            cur_timestamp = str(int(time.time()))

            latlng = (str(addr_info_dict['results'][0]['geometry']['location']['lat']),str(addr_info_dict['results'][0]['geometry']['location']['lng']))

            api_key  = "AIzaSyDgYrnLvtV8en5ARq-MxhNM_vTsyMUf0QA"
            tzonepre = "https://maps.googleapis.com/maps/api/timezone/json?location="
            tzone_info = requests.get(tzonepre+latlng[0]+','+latlng[1]+'&timestamp='+cur_timestamp+'&key='+api_key).json()


            newteach = Tutor(screen_name         = request.POST['name'], 
                             teaching_start_date = timezone.now(),
                             teacher_email       = tzone_info['timeZoneName'], #request.POST['tootemail'],
                             teacher_address     = request.POST['address'],
                             tutor_photo         = request.FILES['docfile'],
                             alma_mater          = request.POST['college'],
                             degree              = request.POST['degree'],
                             major               = request.POST['major'],
                             years_xp            = 2)

            newteach.save()
            mysubs = '- - -'.join(request.POST.getlist('subjects')) if request.POST.getlist('subjects') else "NONE"
            newteach.specialty_set.create(spec_text='SPECIALTIES',
                                          desc_text=mysubs)
            newteach.save()


            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('tudor:index'))
    else:
        form = PhotoUploadForm() # A empty, unbound form
        form2 = SubjectsForm()   # A empty, unbound form
        form3 = DegreeForm()


    # Load documents for the list page
    teachers = Tutor.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'tudor/tutor_upload.html',
        {'teachers': teachers, 'form': form, 'form2': form2, 'form3': form3}
    )

#class ResultsView(generic.DetailView):
#    model = Question
#    template_name = 'polls/results.html'
#
#def vote(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'polls/detail.html', {
#            'question': question,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))