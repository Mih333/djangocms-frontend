from django.test import TestCase

from djangocms_frontend.contrib.grid.forms import GridColumnForm, GridContainerForm
from djangocms_frontend.contrib.grid.models import GridColumn, GridContainer, GridRow


class GridModelTestCase(TestCase):
    def test_grid_instance(self):
        instance = GridContainer.objects.create()
        instance.initialize_from_form(GridContainerForm)
        self.assertEqual(str(instance), "GridContainer (1)")
        self.assertEqual(instance.get_short_description(), "(Container)")

    def test_row_instance(self):
        instance = GridRow.objects.create()
        self.assertEqual(str(instance), "GridRow (1)")
        self.assertEqual(instance.get_short_description(), "(0 columns)")

    def test_column_instance(self):
        instance = GridColumn.objects.create()
        instance.initialize_from_form(GridColumnForm)
        self.assertEqual(str(instance), "GridColumn (1)")
        self.assertEqual(instance.get_short_description(), "(auto)")
        instance.config["xs_col"] = 12
        self.assertEqual(
            instance.get_short_description(),
            "(col-12)",
        )
        instance.config["column_type"] = "column"
        self.assertEqual(
            instance.get_short_description(),
            "(col-12) .column",
        )
        instance.config["md_col"] = 12
        instance.config["md_offset"] = 12
        instance.config["xs_offset"] = 12
        self.assertEqual(
            instance.get_short_description(),
            "(col-12) .column",
        )
        instance.config["xs_ml"] = 12
        instance.config["md_ml"] = 12
        self.assertEqual(
            instance.get_short_description(),
            "(col-12) .column",
        )
