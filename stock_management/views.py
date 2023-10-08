from django.shortcuts import render

# Create your views here.


def homeView(request):
    title = "Seja muito bem vindo!"
    sub_title = "Aqui você encontrará tudo que precisa"
    template = "pages/home.html"
    context = {
        "title": title,
        "sub_title": sub_title,
    }

    return render(request=request, context=context, template_name=template)
