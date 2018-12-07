from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Object, Description, Contribution

import utilities


class ObjectListView(View):
    template_name = 'whatsit/object_list.html'

    def get(self, request):
        objects = Object.objects.filter(publish=True)
        context = {'memory':utilities.get_random_memory(), 'objects': objects}
        return render(request, self.template_name, context)


class SingleObjectView(View):

    def get(self, request, object_number):
        try:
            object = Object.objects.get(number=object_number)
        except:
            return redirect('whatsit:object_list')
        else:
            if object.stage == object.ONE:
                self.template_name = 'whatsit/stage_one.html'
                context = {'memory': utilities.get_random_memory(), 'object': object, 'description': None}
                description = Description.objects.filter(object=object, author=request.user)
                if len(description) == 1:
                    context['description'] = description[0]

        return render(request, self.template_name, context)

    def post(self, request, object_number):
        try:
            object = Object.objects.get(number=object_number)
        except:
            return redirect('whatsit:object_list')
        else:
            if object.stage == object.ONE:
                self.template_name = 'whatsit/stage_one.html'
                if request.POST['button'] == 'cancel':
                    return redirect('whatsit:object_list')
                # an elif will go here checking for deletions
                else:
                    try:
                        old_description = Description.objects.get(object=object, author=request.user)
                    except:
                        old_description = None
                    description_text = request.POST['description_text']
                    if description_text:                    # there is something here to save, else an error
                        if old_description:                 # user is editing a former description
                            old_description.description = description_text
                            old_description.save()
                        else:                               # this is a new description
                            new_description = Description(object=object, author=request.user,
                                                          description=description_text)
                            new_description.save()
                            contribution = Contribution(object=object, user=request.user, type=Contribution.DESCRIPTION)
                    else:
                        context = {'memory': utilities.get_random_memory(), 'object': object, 'description': None,
                                   'error_message': 'Some text must appear in the box below or Save will not work.'}
                        if old_description:
                            context['description'] = old_description.description
                        return render(request, self.template_name, context)
                    return redirect('whatsit:object_view', object_number)



class DescriptionEditView(View):
    template_name = 'whatsit/stage_one.html'





