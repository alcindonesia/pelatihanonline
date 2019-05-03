from django import template
from account.models import Membership

register = template.Library()

@register.filter(name='grid')
def grid(value, arg):
    return (value * 10) + arg + 1


@register.filter(name='get')
def get(value, arg):
    return value['no' + str(arg)]


@register.filter(name='convert')
def convert(value):
    S = ' selected="selected"'
    A = B = C = D = E = U = ''
    if value == 'A':
        A = S
    elif value == 'B':
        B = S
    elif value == 'C':
        C = S
    elif value == 'D':
        D = S
    elif value == 'E':
        E = S
    elif value == '-':
        U = S
    return '''<option value="-"{U}>-</option>
              <option value="A"{A}>A</option>
              <option value="B"{B}>B</option>
              <option value="C"{C}>C</option>
              <option value="D"{D}>D</option>
              <option value="E"{E}>E</option>'''.format(U=U, A=A, B=B, C=C, D=D, E=E)

@register.filter(name='registered')
def registered(value, arg):
    return Membership.objects.filter(event=value, userprofile=arg).exists()

@register.filter(name='accepted')
def accepted(value, arg):
    return Membership.objects.filter(event=value, userprofile=arg, confirmed=True).exists()
