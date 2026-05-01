import csv

class CSVImporter:
    def __init__(self, model, field_mapping, unique_field=None):
        self.model = model
        self.field_mapping = field_mapping
        self.unique_field = unique_field

    def process_file(self, file):
        decoded = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded)

        results = {"created": 0, "updated": 0, "errors": []}

        for i, row in enumerate(reader, start=1):
            try:
                data = self.map_fields(row)
                data = self.clean_data(data)

                obj, created = self.save(data)

                if created:
                    results["created"] += 1
                else:
                    results["updated"] += 1

            except Exception as e:
                results["errors"].append(f"Row {i}: {str(e)}")

        return results

    def map_fields(self, row):
        return {
            model_field: row.get(csv_col)
            for csv_col, model_field in self.field_mapping.items()
        }

    def clean_data(self, data):
        # Example cleaning
        if data.get("age"):
            data["age"] = int(data["age"])
        return data

    def save(self, data):
        if self.unique_field:
            lookup = {self.unique_field: data[self.unique_field]}
            obj, created = self.model.objects.update_or_create(
                defaults=data, **lookup
            )
        else:
            obj = self.model.objects.create(**data)
            created = True

        return obj, created