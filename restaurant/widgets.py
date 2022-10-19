from django.forms import DateInput


class FengyuanChenDatePickerInput(DateInput):
    """
    It inherits from DateInput class and it is associated with
    a template.
    """
    template_name = 'widgets/fengyuanchen_datepicker.html'

