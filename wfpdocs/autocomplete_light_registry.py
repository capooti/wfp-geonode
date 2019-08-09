# d: migration
#import autocomplete_light
#from models import WFPDocument

from autocomplete_light.registry import register
from autocomplete_light.autocomplete.shortcuts import AutocompleteModelTemplate
from models import WFPDocument


class WFPDocumentWfpDocsAutocomplete(AutocompleteModelTemplate):
    choice_template = 'autocomplete_response.html'

register(
    WFPDocument,
    WFPDocumentWfpDocsAutocomplete,
    search_fields=['title'],
    order_by=['title'],
    limit_choices=30,
    autocomplete_js_attributes={
        'placeholder': 'Staticmap name..',
    },
)
