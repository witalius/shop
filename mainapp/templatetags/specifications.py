from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Įstrižainė': 'diagonal',
        'Ekrano tipas': 'display_type',
        'Procesoriaus dažnis': 'processor_freq',
        'Operatyvioji atmintis': 'ram',
        'Vaizdo plokštė': 'video',
        'Akumuliatoriaus darbo laikas': 'time_without_charge'
    },
    'smartphone': {
        'Įstrižainė': 'diagonal',
        'Ekrano tipas': 'display_type',
        'Ekrano raiška': 'resolution',
        'Akumuliatoriaus talpa': 'accum_volume',
        'Operatyvioji atmintis': 'ram',
        'SD kortelės lizdas': 'sd',
        'Maksimali SD kortelės talpa': 'sd_volume_max',
        'Kamera (MP)': 'main_cam_mp',
        'Priekinė kamera (MP)': 'frontal_cam_mp'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Maksimali SD kortelės talpa', None)
        else:
            PRODUCT_SPEC['smartphone']['Maksimali SD kortelės talpa'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

