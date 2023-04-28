from django.shortcuts import render
"""
return render(request, 'sb.html', context)

"""


def pages_view(request, path):
    """ Main page """

    template = 'index.html' if len(path) == 0 else f'{ path[:-1] }.html'

    print(f'Запрошенный путь: {path}')
    return render(request, template_name=template)

