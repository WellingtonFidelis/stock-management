import csv
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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

    if request.method == "POST":
        if form["category"].value() == "":
            item_name_filter = form["item_name"].value()

            queryset = Stock.objects.filter(
                item_name__icontains=form["item_name"].value(),
            )
        else:
            queryset = Stock.objects.filter(
                category=form["category"].value(),
                item_name__icontains=form["item_name"].value(),
            )

    # Setting 2 variables on seesion request to use on export data to csv
    request.session["category_filter"] = form["category"].value()
    request.session["item_name_filter"] = form["item_name"].value()

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

        messages.success(request, "O produto foi criado com sucesso.")

        print("O produto foi criado com sucesso.")

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

            messages.success(
                request, "O produto {} foi atualizado com sucesso.".format(queryset)
            )

            print(
                "=> {} => INFO => O produto {} foi atualizado com sucesso.".format(
                    datetime.datetime.now(), queryset
                )
            )

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

        messages.success(request, "O produto foi excluído permanentemente com sucesso.")

        print("O produto foi deletado com sucesso.")

        return redirect("/list-items")

    context = {
        "form": form,
        "product": queryset,
        "title": title,
        "sub_title": sub_title,
    }

    return render(request=request, context=context, template_name=template)


def exportDataView(request):
    queryset = Stock.objects.all()

    # Getting data from session
    category_filter = request.session["category_filter"]
    item_name_filter = request.session["item_name_filter"]

    if request.method == "GET":
        if not category_filter:
            queryset = Stock.objects.filter(
                item_name__icontains=item_name_filter if item_name_filter else "",
            )
        else:
            queryset = Stock.objects.filter(
                category=category_filter if category_filter else "",
                item_name__icontains=item_name_filter if item_name_filter else "",
            )

        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = 'attachment; filename="lista-produtos-{}.csv"'.format(
            datetime.datetime.now()
        )
        writer = csv.writer(response)
        writer.writerow(["ID", "CATEGORY", "ITEM_NAME", "QUANTITY"])
        instance = queryset
        for item in instance:
            writer.writerow([item.id, item.category, item.item_name, item.quantity])

        return response


def detailItemView(request, pk):
    title = "Detalhes do produto"
    sub_title = "Aqui você encontra todas as informações do seu produto."
    template = "pages/detail-item.html"

    queryset = Stock.objects.get(id=pk)

    context = {
        "title": title,
        "sub_title": sub_title,
        "product": queryset,
    }

    return render(request=request, context=context, template_name=template)
