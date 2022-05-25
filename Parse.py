import os

import requests
from bs4 import BeautifulSoup

chapter_title_number = [
    "০০",
    "০১",
    "০২",
    "০৩",
    "০৪",
    "০৫",
    "০৬",
    "০৭",
    "০৮",
    "০৯",
    "১০",
    "১১",
    "১২",
    "১৩",
    "১৪",
    "১৫",
    "১৬",
    "১৭",
    "১৮",
    "১৯",
    "২০",
    "২১",
    "২২",
    "২৩",
    "২৪",
    "২৫",
    "২৬",
    "২৭",
    "২৮",
    "২৯",
    "৩০",
    "৩১",
    "৩২",
    "৩৩",
    "৩৪",
    "৩৫",
    "৩৬",
    "৩৭",
    "৩৮",
    "৩৯",
    "৪০",
    "৪১",
    "৪২",
    "৪৩",
    "৪৪",
    "৪৫",
    "৪৬",
    "৪৭",
    "৪৮",
    "৪৯",
    "৫০",
    "৫১",
    "৫২",
    "৫৩",
    "৫৪",
    "৫৫",
    "৫৬",
    "৫৭",
    "৫৮",
    "৫৯",
    "৬০",
    "৬১",
    "৬২",
    "৬৩",
    "৬৪",
    "৬৫",
    "৬৬",
    "৬৭",
    "৬৮",
    "৬৯",
    "৭০",
]

chapter_title_ordinal = [
    "শুন্য",
    "প্রথম",
    "দ্বিতীয়",
    "তৃতীয়",
    "চতুর্থ",
    "পঞ্চম",
    "ষষ্ঠ",
    "সপ্তম",
    "অষ্টম",
    "নবম",
    "দশম",
    "একাদশ",
    "দ্বাদশ",
    "ত্রয়োদশ",
    "চতুর্দশ",
    "পঞ্চদশ",
    "ষোড়শ",
    "সপ্তদশ",
    "অষ্টাদশ",
    "ঊনবিংশ",
    "বিংশ",
    "একবিংশ",
    "দ্বাবিংশ",
    "ত্রয়োবিংশ",
    "চতুর্বিংশ",
    "পঞ্চবিংশ",
    "ষট্‌বিংশ",
    "সপ্তবিংশ",
    "অষ্টাবিংশ",
    "ঊনত্রিংশ",
    "ত্রিংশ",
    "একত্রিংশ",
    "দ্বাত্রিংশ",
    "ত্রয়োত্রিংশ",
    "চতুর্ত্রিংশ",
    "চতুর্ত্রিংশ",
    "ষট্‌ত্রিংশ",
    "সপ্তত্রিংশ",
    "অষ্টাত্রিংশ",
    "ঊনচত্বারিংশ",
    "চত্বারিংশ",
    "একচত্বারিংশ",
    "দ্বিচত্বারিংশ",
    "ত্রয়শ্চত্বারিংশ",
    "চতুঃচত্বারিংশ",
    "পঞ্চচত্বারিংশ",
    "ষট্‌চত্বারিংশ",
    "সপ্তচত্বারিংশ",
    "অষ্টচত্বারিংশ",
    "ঊনপঞ্চাশৎ",
    "পঞ্চাশৎ",
]

chapter_title_word = [
    "শুন্য",
    "এক",
    "দুই",
    "তিন",
    "চার",
    "পাঁচ",
    "ছয়",
    "সাত",
    "আট",
    "নয়",
    "দশ",
    "এগারো",
    "বারো",
    "তেরো",
    "চৌদ্দ",
    "পনেরো",
    "ষোল",
    "সতেরো",
    "আঠারো",
    "উনিশ",
    "কুড়ি",
    "একুশ",
    "বাইশ",
    "তেইশ",
    "চব্বিশ",
    "পঁচিশ",
    "ছাব্বিশ",
    "সাতাশ",
    "আঠাশ",
    "ঊনত্রিশ",
    "ত্রিশ",
    "একত্রিশ",
    "বত্রিশ",
    "তেত্রিশ",
    "চৌত্রিশ",
    "পঁয়ত্রিশ",
    "ছত্রিশ",
    "সাঁয়ত্রিশ",
    "আটত্রিশ",
    "ঊনচল্লিশ",
    "চল্লিশ",
    "একচল্লিশ",
    "বিয়াল্লিশ",
    "তেতাল্লিশ",
    "চুয়াল্লিশ",
    "পঁয়তাল্লিশ",
    "ছেচল্লিশ",
    "সাতচল্লিশ",
    "আটচল্লিশ",
    "ঊনপঞ্চাশ",
    "পঞ্চাশ",
    "একান্ন",
    "বাহান্ন",
    "তিপ্পান্ন",
    "চুয়ান্ন",
    "পঞ্চান্ন",
    "ছাপ্পান্ন",
    "সাতান্ন",
    "আটান্ন",
    "ঊনষাট",
    "ষাট",
    "একষট্টি",
    "বাষট্টি",
    "তেষট্টি",
]


def prettify(html):
    html_soup = BeautifulSoup(html, features="lxml")
    return html_soup.prettify()


def get_format(chapter_url):
    response = requests.get(chapter_url)
    soup = BeautifulSoup(response.text, features="lxml")
    chapter = soup.find("span", class_="current-item").string

    if chapter[:4] == "০১. " or chapter[:4] == "০০. " or chapter[:4] == "১.০১":
        chapter_title_format = "first"
    elif chapter[:3] == "১. " or chapter[:3] == "০. ":
        chapter_title_format = "one"
    elif chapter[-4:] == "– ০১" or chapter[-4:] == "– ০০":
        chapter_title_format = "last"
    else:
        chapter_title_format = "full"

    titleFinder = soup.find("a", rel="tag")

    if titleFinder is None:
        title = "Not Found"
    else:
        title = soup.find("a", rel="tag").string

    # title = soup.find('a', rel='tag').string

    return chapter_title_format, title


def parse_chapter(chapter_url, chapter_format="full", book_title="book", i=1):
    response = requests.get(chapter_url)
    soup = BeautifulSoup(response.text, features="lxml")

    # fp = open("sample1.html", encoding='utf-8')
    # soup = BeautifulSoup(fp.read(), features="lxml")

    # print(soup.prettify())

    # title = soup.find('a', rel='tag').string
    chapter = soup.find("span", class_="current-item").string
    # chapter_number = str(i)
    # chapter_text = chapter

    try:
        previous_url = soup.find("a", rel="prev").get("href")
        # print(previous_url)
    except:
        previous_url = ""
        # print("First Chapter ... No previous Link")

    try:
        next_url = soup.find("a", rel="next").get("href")
        # print(next_url)
    except:
        next_url = ""
        # print("Last Chapter ... No next link")

    if chapter_format == "first":
        (chapter_number, chapter_text) = (chapter[:2], chapter[4:])
    elif chapter_format == "one":
        (chapter_number, chapter_text) = (chapter[0], chapter[3:])
    elif chapter_format == "last" and next_url != "":
        (chapter_number, chapter_text) = (chapter[-2:], chapter[:-4])
    elif chapter_format == "last" and next_url == "":
        chapter = chapter.replace(" (শেষ)", "")
        (chapter_number, chapter_text) = (chapter[-2:], chapter[:-4])
    else:
        # chapter_number, chapter_text = str(i).zfill(2), chapter
        chapter_number, chapter_text = "", chapter

    # soup.find("div", class_='scriptlesssocialsharing').decompose()
    body = soup.find("div", class_="entry-content")
    body["class"] = "body-style"

    # print(title)
    # print(chapter_text)
    # print(chapter_number)
    # print(str(body))
    flag = True
    file_name = "chapter" + str(i).zfill(3) + ".xhtml"

    fw = open(
        "book/" + book_title + "/" + file_name.replace("?", ""), "w", encoding="utf-8"
    )
    # ................................................................................
    if chapter_format == "first" or chapter_format == "one":
        temp_head = chapter_text
        temp_number = chapter_title_ordinal[i]
        temp_title = chapter_text

    elif chapter_format == "last":
        temp_head = book_title + " | " + chapter_title_ordinal[i]
        temp_number = book_title
        temp_title = chapter_title_ordinal[i]

    # elif chapter_format == 'full' and flag:
    else:
        temp_head = chapter_text
        temp_number = chapter_title_number[i]
        temp_title = chapter_text

    # else:
    #     temp_head = chapter_title_number[i]
    #     temp_number = book_title
    #     temp_title = chapter_title_ordinal[i]
    # ................................................................................

    head = r'<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><head><title>'
    fw.write(head)
    fw.write(temp_head)
    fw.write(
        r'</title><link href="../Styles/style.css" type="text/css" rel="stylesheet"/></head><body>'
    )

    if temp_number:
        fw.write(r'<h1 class="right sigil_not_in_toc">' + temp_number + "</h1>")
    fw.write(
        r'<br/><h1 class="chapter darkblue">' + temp_title + "</h1>\n<hr/>\n<br/><br/>"
    )

    fw.write(str(body).replace("</p>", "</p><br/>"))  # .replace("<br/>","<br/><br/>"))
    fw.write(r"</body></html>")
    fw.close()

    fr = open("book/" + book_title + "/" + file_name.replace("?", ""), encoding="utf-8")
    html = prettify(fr.read())
    fr.close()

    fw = open(
        "book/" + book_title + "/" + file_name.replace("?", ""), "w", encoding="utf-8"
    )
    fw.write(html)
    fw.close()

    return next_url


def from_first_chapter(first_chapter_url, i=1, book="", writer="UNKNOWN"):
    url = first_chapter_url

    chapter_format, book_title = get_format(url)

    book_title = book

    if not os.path.exists("book/" + book_title):
        os.makedirs("book/" + book_title)

    with open("res/about-01-title.xhtml", encoding="utf-8") as f:
        with open(
            "book/" + book_title + "/about-01-title.xhtml", "w", encoding="utf-8"
        ) as file:
            temp = f.read()
            temp = temp.replace("dummy-title", book_title)
            temp = temp.replace("dummy-writer", writer)
            file.write(temp)

    # with open('res/nav.xhtml', encoding='utf-8') as f:
    #     with open("book/" + book_title + '/0nav.xhtml', 'w', encoding='utf-8') as file:
    #         file.write(f.read())

    # with open('res/about-04-about-reader.xhtml', encoding='utf-8') as f:
    #     with open("book/" + book_title + '/about-04-about-reader.xhtml', 'w', encoding='utf-8') as file:
    #         file.write(f.read())

    # with open('res/about-05-acknowledgement.xhtml', encoding='utf-8') as f:
    #     with open("book/" + book_title + '/about-05-acknowledgement.xhtml', 'w', encoding='utf-8') as file:
    #         file.write(f.read())

    # with open('res/about-06-about-contributor.xhtml', encoding='utf-8') as f:
    #     with open("book/" + book_title + '/about-06-about-contributor.xhtml', 'w', encoding='utf-8') as file:
    #         file.write(f.read())

    with open("res/about-07-start.xhtml", encoding="utf-8") as f:
        with open(
            "book/" + book_title + "/about-07-start.xhtml", "w", encoding="utf-8"
        ) as file:
            temp = f.read()
            temp = temp.replace("dummy-title", book_title)
            file.write(temp)

    with open("res/style.css", encoding="utf-8") as f:
        with open("book/" + book_title + "/style.css", "w", encoding="utf-8") as file:
            file.write(f.read())

    while url != "":
        print(f"{str(i).zfill(2)} {url}")
        url = parse_chapter(url, chapter_format, book_title, i)
        i += 1

    with open("res/finish.xhtml", encoding="utf-8") as f:
        with open(
            "book/" + book_title + "/finish.xhtml", "w", encoding="utf-8"
        ) as file:
            file.write(f.read())


def parse_book(book_url, i=1, book="", writer="UNKNOWN"):
    # fp = open("sample3.html", encoding='utf-8')
    # soup = BeautifulSoup(fp.read(), features="lxml")

    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, features="lxml")

    first_chapter_url = soup.find(class_="more-link").get("href")

    from_first_chapter(first_chapter_url, i, book, writer)


# def parse(book_url, i=1, book, writer):
#     response = requests.get(book_url)
#     soup = BeautifulSoup(response.text, features="lxml")

#     first_chapter_url = soup.find(class_="more-link").get('href')


book_name = "দ্য টাইগার’স প্রে"
writer_name = "উইলবার স্মিথ/টম হারপার/অসীম পিয়াস"
first_chapter = 1
url = "https://www.ebanglalibrary.com/102895/%e0%a7%a7-%e0%a6%a1%e0%a6%be%e0%a6%93%e0%a6%9c%e0%a6%be%e0%a6%b0-%e0%a6%a8%e0%a6%be%e0%a6%ae%e0%a7%87%e0%a6%b0-%e0%a6%9c%e0%a6%be%e0%a6%b9%e0%a6%be%e0%a6%9c/"
# url='https://www.ebanglalibrary.com/%E0%A7%A6%E0%A7%A7-%E0%A6%B9%E0%A7%87%E0%A6%AE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%87%E0%A6%B0-%E0%A6%AA%E0%A7%9C%E0%A6%A8%E0%A7%8D%E0%A6%A4-%E0%A6%B9%E0%A6%B2%E0%A7%81%E0%A6%A6-%E0%A6%B0%E0%A7%8C/'


# book_name=input()
# writer_name=input()
# first_chapter=int(input())
# url=input()


from_first_chapter(url, i=first_chapter, book=book_name, writer=writer_name)
