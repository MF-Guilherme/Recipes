from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1
        )
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_make_sure_middle_ranges_are_correct(self):  # noqa: E501
        # Current Page = 10 | Qty Page = 2 | Middle Page = 10
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10
        )
        self.assertEqual([9, 10, 11, 12], pagination)

        # Current Page = 44 | Qty Page = 2 | Middle Page = 44
        pagination = make_pagination_range(
            page_range=list(range(1, 51)),
            qty_pages=4,
            current_page=44
        )
        self.assertEqual([43, 44, 45, 46], pagination)
