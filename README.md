#H1 Thomas' Blog

**Goal of this project is to create a personal blog.**

It will contain:
- a main page with links to the articles
- different articles about boats, cars, planes and bokes (placeholders)
- a contact page with:
    - a contact form
    - address
    - map
- short intro to the author
- and the ability to filter the article based on different categories

Techstack:
- Frontend: HTML, CSS
- Backend: Flask, jinja2

class Article():
    id = 'integer'
    author = 'string'
    date = 'date'
    content = 'text'
    topic = 'string

class Experience():
    id = 'integer'
    start_date = 'date'
    end_date = 'date'
    title = 'text'
    description = 'text'
    company = 'string'
    company_url = 'string'
    