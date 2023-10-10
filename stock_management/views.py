from django.shortcuts import render
from stock_management.models import Stock

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


def listItemsView(request):
    title = "Produtos"
    sub_title = "Aqui você a lista de seus produtos"
    template = "pages/list-items.html"
    queryset = Stock.objects.all()
    context = {"title": title, "sub_title": sub_title, "products": queryset}

    return render(request=request, context=context, template_name=template)
