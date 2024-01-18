from django import template


register = template.Library()

TRASH_WORDS = ['душнила', 'псина']

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   for word in TRASH_WORDS:
      value = value.replace(word[1:], '*' * len(word[1:]))
   return value


