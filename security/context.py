def show(request):
    context = dict()
    context['address'] = """A108 Adam Street <br>New York, NY 535022<br>United States <br><br>"""
    context['tel'] = '(+27) 11 070 7229'
    context['email'] = 'info@iamemerge.co.za'
    context['company'] = 'I am emerge'
    return context