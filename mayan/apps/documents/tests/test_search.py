from __future__ import unicode_literals

from django.test import override_settings

from mayan.apps.common.tests import BaseTestCase
from mayan.apps.documents.permissions import permission_document_view
from mayan.apps.documents.search import document_page_search, document_search
from mayan.apps.documents.tests import DocumentTestMixin


@override_settings(OCR_AUTO_OCR=False)
class DocumentSearchTestCase(DocumentTestMixin, BaseTestCase):
    def _perform_document_page_search(self):
        return document_page_search.search(
            query_string={'q': self.document.label}, user=self.user
        )

    def _perform_document_search(self):
        return document_search.search(
            query_string={'q': self.document.label}, user=self.user
        )

    def test_document_page_search_no_access(self):
        queryset = self._perform_document_page_search()
        self.assertFalse(self.document.pages.first() in queryset)

    def test_document_page_search_with_access(self):
        self.grant_access(
            permission=permission_document_view, obj=self.document
        )
        queryset = self._perform_document_page_search()
        self.assertTrue(self.document.pages.first() in queryset)

    def test_document_search_no_access(self):
        queryset = self._perform_document_search()
        self.assertFalse(self.document in queryset)

    def test_document_search_with_access(self):
        self.grant_access(
            permission=permission_document_view, obj=self.document
        )
        queryset = self._perform_document_search()
        self.assertTrue(self.document in queryset)
