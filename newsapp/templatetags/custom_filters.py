from django import template

register = template.Library()  # регистрация фильтра

censor_list = ['слово1', 'слово2', 'слово3', 'слово4'] # словарь нецензурных слов

@register.filter(name='cenzor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, '***') # замены слова на ***
    return value