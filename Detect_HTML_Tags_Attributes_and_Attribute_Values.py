from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print('->', attr, '>', value)


html = ''
N = int(input())
for _ in range(N):
    html += input().strip() + '\n'

parser_obj = MyHTMLParser()
parser_obj.feed(html)
