from django.shortcuts import render
from .forms import CSVUploadForm
from .models import Customer
from .utils.csv_importer import CSVImporter

def import_customers(request):
    result = None

    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():
            importer = CSVImporter(
                model=Customer,
                field_mapping={
                    "Name": "name",
                    "Email": "email",
                    "Age": "age"
                },
                unique_field="email"
            )

            result = importer.process_file(request.FILES['file'])
    else:
        form = CSVUploadForm()

    return render(request, "customers/import.html", {
        "form": form,
        "result": result
    })