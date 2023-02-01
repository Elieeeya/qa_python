# qa_python
### Описание реализованных unit tests

#### test_init_book_rating_empty_true
1. Изначальный словарь рейтинга (books_rating) пуст

#### test_init_favorites_empty_true
2. Изначальный список "Избранное" пуст
    
#### test_add_new_books_books_added
3. В словарь books_rating можно добавить две книги с разным названием

#### test_add_new_books_add_two_identical_books
4. В словарь books_rating нельзя добавить одну и ту же книгу более одного раза

#### test_add_one_book_to_books_rating_true
5. Базовый рейтинг каждой книги равен единице (при добавлении в словарь рейтинга (books_rating))

#### test_set_one_book_with_a_rating_from_1_to_11
6. Для добавленной книги можно установить рейтинг в пределах от 1 до 10

#### test_add_3_books_set_rating
7. Граничные значения рейтинга соблюдены

#### test_add_5_books_set_rating
8. Можно получить список книг с заданным рейтингом

#### test_get_books_rating_return_dict_with_book_with_preset_rating
9. Можно получить словарь рейтинга

#### test_add_book_in_favorites_add_one_book_in_favorites
10. Книга добавляется в список "Избранное" 

#### test_add_book_in_favorites_book_not_in_books_rating_cant_be_added_true
11. Книга не добавляется в список "Избранное" 

#### test_delete_book_from_favorites_delete_one_book
12. Книгу можно удалить из списка "Избранное"

#### test_get_list_of_favorites_books_return_list_with_one_book 
13. Можно получить список "Избранное"