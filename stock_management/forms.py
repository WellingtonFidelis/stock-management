from django import forms
from stock_management.models import Stock

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Fieldset,
    Div,
    HTML,
    ButtonHolder,
    Submit,
    Row,
    Column,
)


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name", "quantity"]

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper = FormHelper()

        self.helper.form_id = "form-create-item"
        self.helper.form_class = "g-3"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column(
                    Field("item_name", css_class="form-control col-4 mb-0"),
                    Field("category", css_class="form-control col-4 mb-0"),
                    Field("quantity", css_class="form-control col-4 mb-0"),
                ),
                css_class="mb-3",
            ),
            Row(Submit("submit", "Salvar", css_class=""), css_class="col-6 mx-auto"),
        )

    def clean_category(self):
        category = self.cleaned_data.get("category")

        if not category:
            raise forms.ValidationError("Esse campo é obrigatório")

        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get("item_name")

        if not item_name:
            raise forms.ValidationError("Esse campo é obrigatório")

        for i in Stock.objects.all():
            if i.item_name == item_name:
                raise forms.ValidationError(
                    f"Já existe um produto com o nome de: {item_name}"
                )

        return item_name


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name"]

    # Creating an instance level helper
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper = FormHelper()

        self.helper.form_id = "form-search-items"
        self.helper.form_class = "form-inline"
        # self.helper.label_class = "col-4"
        # self.helper.field_class = "col-4"
        self.helper.form_method = "post"
        # self.helper.form_action = "submit_survey"

        self.helper.layout = Layout(
            Row(
                Column(
                    Field("category", css_class="form-control mb-0"),
                    Field("item_name", css_class="form-control mb-0"),
                    Submit("submit", "Pesquisar"),
                    css_class="form-group mb-0",
                ),
                css_class="form-row align-items-center justify-content-center",
            ),
        )

    item_name = forms.CharField(
        label="Nome",
        # max_length=80,
        required=False,
    )


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            "category",
            "item_name",
            "quantity",
        ]

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper = FormHelper()

        self.helper.form_id = "form-create-item"
        self.helper.form_class = "g-3"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column(
                    Field("category", css_class="form-control col-4 mb-0"),
                    Field("item_name", css_class="form-control col-4 mb-0"),
                    Field("quantity", css_class="form-control col-4 mb-0"),
                ),
                css_class="mb-3",
            ),
            Row(Submit("submit", "Salvar", css_class=""), css_class="col-6 mx-auto"),
        )


class StockDeleteForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name", "quantity"]

    category = forms.CharField(
        label="Categoria",
        # max_length=80,
        disabled=True,
        required=False,
    )

    item_name = forms.CharField(
        label="Nome",
        disabled=True,
        required=False,
    )

    quantity = forms.IntegerField(
        label="Quantidade",
        disabled=True,
        required=False,
    )


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["issue_quantity", "issue_to"]


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["receive_quantity", """receive_by"""]
