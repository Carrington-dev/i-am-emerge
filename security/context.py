def show(request):
    context = dict()
    context['address'] = """59 Nottingham Rd <br>Randpark Ridge, GP 2169<br>Johannesburg <br><br>"""
    context['contact_address'] = """59 Nottingham Rd <br>Randpark Ridge, GP 2169<br>"""
    context['tel'] = '(+27) 11 346 5233'
    context['tel2'] = '(+27) 81 506 1174'
    context['email'] = 'brian@multimediavilla.co.za'
    context['company'] = 'Multimedia Villa'
    return context