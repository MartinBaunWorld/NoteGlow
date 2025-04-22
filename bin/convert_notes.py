#!./venv/bin/python3
import setup # noqa

from app.models import Note
from utils import markdown
from bs4 import BeautifulSoup



if __name__ == "__main__":
    for note in Note.objects.all():
        soup = BeautifulSoup(markdown(note.body), 'html.parser')

        for tag in soup.find_all(['ul', 'ol']):
            for li in tag.find_all('li'):
                new_p = soup.new_tag('p')
                new_p.string = li.get_text()
                tag.insert_before(new_p)
            tag.decompose()
        note.body = soup.prettify()
        print(note.body)
        print("-" * 50)
        note.save()
