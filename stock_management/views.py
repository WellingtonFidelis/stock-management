from django.shortcuts import render, redirect
from stock_management.models import Stock
from stock_management.forms import (
    StockCreateForm,
    StockSearchForm,
    StockUpdateForm,
    StockDeleteForm,
)

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
    form = StockSearchForm(request.POST or None)

    context = {
        "title": title,
        "sub_title": sub_title,
        "products": queryset,
        "form": form,
    }

    if request.method == "POST":
        queryset = Stock.objects.filter(
            category__icontains=form["category"].value(),
            item_name__icontains=form["item_name"].value(),
        )

        context = {
            "title": title,
            "sub_title": sub_title,
            "products": queryset,
            "form": form,
        }

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


def updateItemView(request, pk):
    title = "Atualizar produto"
    sub_title = "Deixe tudo atualizado."
    template = "pages/update-item.html"

    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)

    if request.method == "POST":
        form = StockUpdateForm(request.POST, instance=queryset)

        if form.is_valid():
            form.save()
            return redirect("/list-items")

    context = {
        "form": form,
        "product": queryset,
        "title": title,
        "sub_title": sub_title,
    }

    return render(request=request, context=context, template_name=template)


def deleteItemView(request, pk):
    title = "Excluir produto"
    sub_title = "Cuidado. Após a exclusão do produto não conseguirá mais consultá-lo."
    template = "pages/delete-item.html"

    queryset = Stock.objects.get(id=pk)
    form = StockDeleteForm(instance=queryset)

    if request.method == "POST":
        queryset.delete()
        return redirect("/list-items")

    context = {
        "form": form,
        "product": queryset,
        "title": title,
        "sub_title": sub_title,
    }

    return render(request=request, context=context, template_name=template)
