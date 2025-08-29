# Документация по модулю colorama

**colorama** — это библиотека Python, которая упрощает работу с цветным и стилизованным текстом в терминале. Она делает ваш вывод совместимым с Windows и другими платформами, поддерживающими ANSI escape sequences.

## Установка

```bash
pip install colorama

```

## Быстрый старт

```python
from colorama import init, Fore, Back, Style

init()  # Инициализация colorama (на Windows обязательно)

print(Fore.RED + 'Этот текст красный')
print(Back.GREEN + 'Зеленый фон')
print(Style.BRIGHT + 'Яркий стиль')
print(Style.RESET_ALL + 'Сброс стилей')
```

## Основные возможности

- **Fore** — цвета текста (например, `Fore.BLUE`, `Fore.YELLOW`)
- **Back** — цвета фона (например, `Back.WHITE`, `Back.MAGENTA`)
- **Style** — стили текста (`Style.DIM`, `Style.NORMAL`, `Style.BRIGHT`, `Style.RESET_ALL`)

## Пример использования

```python
from colorama import init, Fore, Back, Style

init(autoreset=True)  # После каждого print стили сбрасываются

print(Fore.GREEN + 'Успех!')
print(Fore.RED + Back.YELLOW + 'Ошибка!')
print(Style.BRIGHT + 'Яркий текст')
```

## Советы

- Используйте `init(autoreset=True)`, чтобы не сбрасывать стили вручную.
- Коды цветов и стилей можно комбинировать.
- Colorama работает во всех популярных терминалах.

## Ссылки

- [Документация colorama на PyPI](https://pypi.org/project/colorama/)
- [Исходный код на GitHub](https://github.com/tartley/colorama)
