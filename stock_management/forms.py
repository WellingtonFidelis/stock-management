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
                    Field("category", css_class="form-control col-4 mb-0"),
                    Field("item_name", css_class="form-control col-4 mb-0"),
                    Field("quantity", css_class="form-control col-4 mb-0"),
                ),
                css_class="mb-3",
            ),
            Row(Submit("submit", "Salvar", css_class=""), css_class="col-6 mx-auto"),
        )

    category = forms.CharField(
        label="Categoria",
        # max_length=80,
        required=True,
    )

    item_name = forms.CharField(
        label="Nome",
        # max_length=80,
        required=True,
    )

    quantity = forms.IntegerField(
        label="Quantidade",
        # max_length=80,
        initial=0,
        max_value=1000000,
        min_value=1,
        step_size=1,
        help_text="O valor dever estar entre 1 e 1.000.000",
        error_messages={
            "required": "Por favor insira um valor",
            "invalid": "O valor tem que ser maior que 0 e menor que 1.000.000.",
        },
        required=True,
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
                Column("category", css_class="form-group col-4 mb-0"),
                Column("item_name", css_class="form-group col-4 mb-0"),
                Column(
                    Submit("submit", "Pesquisar"),
                    css_class="form-group col-2 mb-0 mt-3",
                ),
                css_class="form-row align-items-center justify-content-center",
            ),
        )

        # self.helper.add_input(Submit("Pesquisar", "Submit"))

    category = forms.CharField(
        label="Categoria",
        # max_length=80,
        required=False,
    )
    item_name = forms.CharField(
        label="Nome",
        # max_length=80,
        required=False,
    )
