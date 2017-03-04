from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string

from catalog import models as cmod

@view_function
def process_request(request):
    print('>>>>>>> Details Process Request')
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/index')

    print(product.name)
    if product.id in request.last5:
        request.last5.remove(product.id)

    request.last5.insert(0, product.id)

    context = {
        'product': product
    }

    return dmp_render(request, 'details.html', context)