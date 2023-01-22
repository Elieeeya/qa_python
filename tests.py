class TestBooksCollector:

    def test_init_book_rating_empty_true(self, cb):
        assert len(cb.books_rating) == 0

    def test_init_favorites_empty_true(self, cb):
        assert len(cb.favorites) == 0

    def test_add_new_books_books_added(self, cb):
        cb.add_new_book('Так говорил Заратустра'),
        cb.add_new_book('Сверхчеловек против супер-эго')

        assert len(cb.get_books_rating()) == 2

    def test_add_new_books_add_two_identical_books(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.add_new_book('Так говорил Заратустра')

        assert len(cb.get_books_rating()) == 1

    def test_add_one_book_to_books_rating_true(self, cb):
        cb.add_new_book('Так говорил Заратустра')

        assert cb.books_rating['Так говорил Заратустра'] == 1

    def test_set_one_book_with_a_rating_from_1_to_11(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.set_book_rating('Так говорил Заратустра', 5)

        assert cb.books_rating['Так говорил Заратустра'] == 5

    def test_set_one_book_with_a_negative_rating(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.set_book_rating('Так говорил Заратустра', -2)

        assert cb.get_books_rating() != -2

    def test_set_one_book_with_max_rating(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.set_book_rating('Так говорил Заратустра', 15)

        assert cb.get_books_rating() != 15

    def test_add_3_books_set_rating(self, cb):
        cb.add_new_book('Так')
        cb.add_new_book('говорил')
        cb.add_new_book('Заратустра')

        cb.set_book_rating('Так', 1)
        cb.set_book_rating('говорил', 5)
        cb.set_book_rating('Заратустра', 10)

        assert cb.get_book_rating('Так') == 1
        assert cb.get_book_rating('говорил') == 5
        assert cb.get_book_rating('Заратустра') == 10

    def test_add_5_books_set_rating(self, cb):
        cb.add_new_book('Так')
        cb.add_new_book('говорил')
        cb.add_new_book('Заратустра')
        cb.add_new_book('Ретеcт')
        cb.add_new_book('Сколько можно')

        cb.set_book_rating('Так', 2)
        cb.set_book_rating('говорил', 2)
        cb.set_book_rating('Ретеcт', 5)
        cb.set_book_rating('Заратустра', 5)
        cb.set_book_rating('Сколько можно', 5)

        books_with_rating_two = cb.get_books_with_specific_rating(2)
        books_with_rating_three = cb.get_books_with_specific_rating(5)

        assert len(cb.get_books_with_specific_rating(2)) == 2
        assert ['Так', 'говорил'] == books_with_rating_two
        assert len(cb.get_books_with_specific_rating(5)) == 3
        assert ['Заратустра', 'Ретеcт', 'Сколько можно'] == books_with_rating_three

    def test_get_books_rating_return_dict_with_book_with_preset_rating(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.set_book_rating('Так говорил Заратустра', 2)

        assert type(cb.books_rating) == dict
        assert cb.books_rating['Так говорил Заратустра'] == 2

    def test_add_book_in_favorites_add_one_book_in_favorites(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.add_book_in_favorites('Так говорил Заратустра')

        assert 'Так говорил Заратустра' in cb.get_list_of_favorites_books()
        assert len(cb.favorites) == 1

    def test_add_book_in_favorites_book_not_in_books_rating_cant_be_added_true(self, cb):
        cb.add_book_in_favorites('Так говорил Заратустра')

        assert 'Так говорил Заратустра' not in cb.get_list_of_favorites_books()
        assert len(cb.favorites) == 0

    def test_delete_book_from_favorites_delete_one_book(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.add_book_in_favorites('Так говорил Заратустра')

        assert 'Так говорил Заратустра' in cb.get_list_of_favorites_books()
        assert len(cb.favorites) == 1

        cb.delete_book_from_favorites('Так говорил Заратустра')

        assert 'Так говорил Заратустра' not in cb.get_list_of_favorites_books()
        assert len(cb.favorites) == 0

    def test_get_list_of_favorites_books_return_list_with_one_book(self, cb):
        cb.add_new_book('Так говорил Заратустра')
        cb.add_book_in_favorites('Так говорил Заратустра')

        assert type(cb.favorites) == list
        assert 'Так говорил Заратустра' in cb.get_list_of_favorites_books()
        assert len(cb.favorites) == 1