library_rules = ("Библиотека «Техно»", 21, 5)
book_requests = [501, 507, 512, 526, 531, 544]
debtors = {507, 526, 544}

books_catalog = {
    "B-101": "«Чистый код»",
    "B-102": "«Алгоритмы»",
    "B-103": "«Совершенный код»"
}

print(f"Правила выдачи: {library_rules[0]}, {library_rules[1]} день, не более {library_rules[2]} книг")
print(f"Заявки в порядке поступления: {', '.join(map(str, book_requests))}")
print(f"Читатели c задолженностью: {', '.join(map(str, debtors))}")
print("Книги:", ", ".join([f"{k} - {v}" for k, v in books_catalog.items()]))
print("-" * 50)

new_request = 558
book_requests.append(new_request)

check_reader = 526
is_debtor = "да" if check_reader in debtors else "нет"

search_inventory = "B-102"
book_title = books_catalog.get(search_inventory, "Книга не найдена")

print(f"После добавления заявки: {', '.join(map(str, book_requests))}")
print(f"Читатель {check_reader} имеет задолженность: {is_debtor}")
print(f"Книга с номером {search_inventory}: {book_title}")
