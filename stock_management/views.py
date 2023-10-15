from django.shortcuts import render, redirect
from stock_management.models import Stock
from stock_management.forms import StockCreateForm

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


def createItemView(request):
    form = StockCreateForm(request.POST or None)
    title = "Cadastro de Produto"
    sub_title = "Cadastre novos produtos e continue no controle."
    template = "pages/create-item.html"

    if form.is_valid():
        form.save()
        return redirect("/list-items")

    context = {
        "form": form,
        "title": title,
        "sub_title": sub_title,
    }

    return render(request=request, context=context, template_name=template)
