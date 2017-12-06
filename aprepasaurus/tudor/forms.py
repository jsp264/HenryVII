# Image Upload File

# -*- coding: utf-8 -*-
from django import forms

class PhotoUploadForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a photo of yourself!',
        help_text='max. 4 megabytes'
    )

SUBJECT_CHOICES = (
    ('sat_reading'  , '         SAT Reading         '),
    ('sat_writing'  , '         SAT Writing         '),
    ('sat_math'     , '       SAT Mathematics       '),
    ('sat_essay'    , '      SAT Essay Writing      '),
    ('toefl_speak'  , '        TOEFL Speaking       '),
    ('toefl_read'   , '        TOEFL Reading        '),
    ('toefl_writing', '        TOEFL Writing        '),
    ('toefl_listen' , '       TOEFL Listening       '),
    ('ap_world'     , '       AP World History      '),
    ('ap_euro'      , '     AP European History     '),
    ('ap_chem'      , '         AP Chemistry        '),
    ('ap_phys'      , '          AP Physics         '),
    ('ap_calc'      , '        AP Calculus BC       '),
    ('ap_lang'      , ' AP Language & Comp '),
    ('ap_lit'       , 'AP Literature & Comp'),
)

class SubjectsForm(forms.Form):
    subjects = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=SUBJECT_CHOICES,
    )

DEGREEES = (
	('Bachelors'  , 'Bachelors'),
	('Masters'    , 'Masters'),
	('Doctorate'  ,  'PhD'),
)

class DegreeForm(forms.Form):
	degrees = forms.ChoiceField(
		choices=DEGREEES,
		widget =forms.RadioSelect(),
	)

PARENT_CHOI = (
    ('Parent', 'Parent'),
    ('Student', 'Student'),
    )

class ParentForm(forms.Form):
    parentf = forms.ChoiceField(
        choices = PARENT_CHOI,
        widget=forms.RadioSelect(),
    )
