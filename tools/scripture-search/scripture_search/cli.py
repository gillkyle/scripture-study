"""Command-line interface for scripture search."""

import argparse
import sys
from pathlib import Path

from .db import ScriptureDB, DEFAULT_DB_PATH
from .search import search_verses, get_verse, get_chapter, get_context, get_volumes, get_book_list


def cmd_search(args):
    """Handle search command."""
    query = " ".join(args.query)
    results = search_verses(query, volume=args.volume, limit=args.limit)

    if not results:
        print(f"No results found for: {query}")
        return 1

    print(f"Found {len(results)} results for: {query}\n")

    for r in results:
        print(f"📖 {r['reference']}")
        print(f"   {r['text'][:200]}{'...' if len(r['text']) > 200 else ''}")
        print()

    return 0


def cmd_verse(args):
    """Handle verse lookup command."""
    reference = " ".join(args.reference)
    verse = get_verse(reference)

    if not verse:
        print(f"Verse not found: {reference}")
        return 1

    print(f"📖 {verse['reference']}")
    print(f"\n{verse['text']}")
    return 0


def cmd_chapter(args):
    """Handle chapter lookup command."""
    book = " ".join(args.book)
    verses = get_chapter(book, args.chapter)

    if not verses:
        print(f"Chapter not found: {book} {args.chapter}")
        return 1

    print(f"📖 {book} {args.chapter}\n")

    for v in verses:
        print(f"{v['verse']}. {v['text']}")
        print()

    return 0


def cmd_context(args):
    """Handle context lookup command."""
    reference = " ".join(args.reference)
    verses = get_context(reference, before=args.before, after=args.after)

    if not verses:
        print(f"Verse not found: {reference}")
        return 1

    print(f"📖 Context for {reference}\n")

    for v in verses:
        marker = "→ " if v['reference'] == reference else "  "
        print(f"{marker}{v['reference']}")
        print(f"  {v['text']}")
        print()

    return 0


def cmd_list(args):
    """Handle list command."""
    if args.what == "volumes":
        volumes = get_volumes()
        print("Available volumes:")
        for v in volumes:
            print(f"  - {v}")
    elif args.what == "books":
        books = get_book_list(volume=args.volume)
        title = f"Books in {args.volume}" if args.volume else "All books"
        print(f"{title}:")
        for b in books:
            print(f"  - {b}")
    return 0


def cmd_stats(args):
    """Handle stats command."""
    with ScriptureDB() as db:
        total = db.get_verse_count()
        print(f"Scripture Database Statistics\n")
        print(f"Total verses: {total:,}")
        print()

        for volume in db.get_volumes():
            count = db.get_verse_count(volume)
            books = len(db.get_books(volume))
            print(f"  {volume}:")
            print(f"    {count:,} verses in {books} books")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Scripture search and lookup tool",
        prog="scripture-search"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Search command
    search_parser = subparsers.add_parser("search", aliases=["s"], help="Search scriptures")
    search_parser.add_argument("query", nargs="+", help="Search terms")
    search_parser.add_argument("-v", "--volume", help="Filter by volume")
    search_parser.add_argument("-l", "--limit", type=int, default=20, help="Max results")
    search_parser.set_defaults(func=cmd_search)

    # Verse command
    verse_parser = subparsers.add_parser("verse", aliases=["v"], help="Look up a verse")
    verse_parser.add_argument("reference", nargs="+", help="Verse reference (e.g., '1 Nephi 3:7')")
    verse_parser.set_defaults(func=cmd_verse)

    # Chapter command
    chapter_parser = subparsers.add_parser("chapter", aliases=["ch"], help="Look up a chapter")
    chapter_parser.add_argument("book", nargs="+", help="Book name")
    chapter_parser.add_argument("chapter", type=int, help="Chapter number")
    chapter_parser.set_defaults(func=cmd_chapter)

    # Context command
    context_parser = subparsers.add_parser("context", aliases=["ctx"], help="Get verse with context")
    context_parser.add_argument("reference", nargs="+", help="Verse reference")
    context_parser.add_argument("-b", "--before", type=int, default=2, help="Verses before")
    context_parser.add_argument("-a", "--after", type=int, default=2, help="Verses after")
    context_parser.set_defaults(func=cmd_context)

    # List command
    list_parser = subparsers.add_parser("list", aliases=["ls"], help="List volumes or books")
    list_parser.add_argument("what", choices=["volumes", "books"], help="What to list")
    list_parser.add_argument("-v", "--volume", help="Filter books by volume")
    list_parser.set_defaults(func=cmd_list)

    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Show database statistics")
    stats_parser.set_defaults(func=cmd_stats)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
