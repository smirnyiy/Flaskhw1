# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask
from faker import Faker
from datetime import datetime


app = Flask(__name__)
fake = Faker('ru-RU')


def get_news_list() -> list[dict]:
    """Example function to get news list for the website"""
    news = []
    for _ in range(10):
        news.append(
            {
                'article': fake.paragraph(nb_sentences=1),
                'description': fake.paragraph(),
                'date': fake.date('%H:%M %d.%m.%Y'),
            }
        )

    return sorted(
        news,
        key=lambda x: datetime.strptime(x['date'], '%H:%M %d.%m.%Y'),
        reverse=True,
    )


@app.route('/')
def index():
    news_list = get_news_list()
    page_content = [
        """<head>
    <title>News List</title>
    <style type="text/css">
        .article{background: #ccc;}
    </style>
</head>
<body>
    <h1>Список новостей</h1>"""
    ]
    for el in news_list:
        # print(el)
        page_content.append(
            f"""    <div>
        <p class="article">{el["article"]}</p>
        <p>{el["description"]}</p>
        <p>{el["date"]}</p>
    </div>"""
        )
    page_content.append('</body>')
    return '\n'.join(page_content)


if __name__ == '__main__':
    app.run(debug=True)