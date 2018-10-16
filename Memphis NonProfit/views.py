from django.shortcuts import render,redirect,get_object_or_404
from .forms import Forms

from .models import FormModel


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)
def add (request):
    if(request.method=='POST'):
        form = Forms(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("index")
        else:
            form = Forms()
        return render (request,'forms_app/addRecipe.html',{'form':form})
def edit (request,pk):
    theModel = get_object_or_404(FormModel,pk=pk)

    if(request.method=='POST'):
        form=Forms(request.POST, instance=theModel)
        if (form.is_valid()):
            form.save()
            return redirect("index")
        else:
            print(" Aint valid")
            return redirect('edit',pk=pk)
    else:
        form =Forms(instance= theModel)
    return render(request,'forms_app/addRecipe.html',{'form':form})

