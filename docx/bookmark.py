# encoding: utf-8

"""Objects related to bookmarks."""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from docx.shared import lazyproperty


class Bookmarks(object):
    """Sequence of |Bookmark| objects."""

    def __init__(self, document_part):
        self._document_part = document_part

    def __len__(self):
        return len(self._finder.bookmark_pairs)

    @lazyproperty
    def _finder(self):
        """_DocumentBookmarkFinder instance for this document."""
        raise NotImplementedError


class _DocumentBookmarkFinder(object):
    """Provides access to bookmark oxml elements in an overall document."""

    @property
    def bookmark_pairs(self):
        """List of (bookmarkStart, bookmarkEnd) element pairs for document.

        The return value is a list of two-tuples (pairs) each containing
        a start and its matching end element.

        All story parts of the document are searched, including the main
        document story, headers, footers, footnotes, and endnotes. The order
        of part searching is not guaranteed, but bookmarks appear in document
        order within a particular part. Only well-formed bookmarks appear.
        Any open bookmarks (start but no end), reversed bookmarks (end before
        start), or duplicate (name same as prior bookmark) bookmarks are
        ignored.
        """
        raise NotImplementedError
