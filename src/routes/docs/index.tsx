import { createFileRoute, Link } from "@tanstack/react-router";
import { source } from "@/lib/source";
import { BookOpen, Tag, Calendar } from "lucide-react";

export const Route = createFileRoute("/docs/")({
  component: DocsIndexPage,
});

function DocsIndexPage() {
  const pages = source.getPages();

  // Group pages by category
  const categories = new Map<string, typeof pages>();
  for (const page of pages) {
    const category = (page.data as { category?: string }).category ?? "uncategorized";
    if (!categories.has(category)) {
      categories.set(category, []);
    }
    categories.get(category)!.push(page);
  }

  const categoryLabels: Record<string, string> = {
    "old-testament": "Old Testament",
    "new-testament": "New Testament",
    "book-of-mormon": "Book of Mormon",
    "conference": "General Conference",
    "parallels": "Parallels & Connections",
    "personal": "Personal Reflections",
    "uncategorized": "Other Notes",
  };

  return (
    <div className="py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-4">Study Notes</h1>
        <p className="text-fd-muted-foreground">
          Browse all scripture study notes organized by category.
          {pages.length > 0 && ` ${pages.length} notes available.`}
        </p>
      </div>

      {pages.length === 0 ? (
        <div className="text-center py-12 text-fd-muted-foreground">
          <BookOpen className="h-12 w-12 mx-auto mb-4 opacity-50" />
          <p>No notes yet. Start studying to add your first note!</p>
        </div>
      ) : (
        <div className="space-y-8">
          {Array.from(categories.entries()).map(([category, categoryPages]) => (
            <section key={category}>
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                <BookOpen className="h-5 w-5" />
                {categoryLabels[category] ?? category}
              </h2>
              <div className="grid gap-4 md:grid-cols-2">
                {categoryPages.map((page) => (
                  <NoteCard key={page.url} page={page} />
                ))}
              </div>
            </section>
          ))}
        </div>
      )}
    </div>
  );
}

function NoteCard({ page }: { page: ReturnType<typeof source.getPages>[0] }) {
  const data = page.data as {
    title?: string;
    description?: string;
    tags?: string[];
    date?: string;
  };

  return (
    <Link
      to={page.url}
      className="block p-4 bg-fd-card border border-fd-border rounded-lg hover:border-fd-primary transition-colors"
    >
      <h3 className="font-medium mb-2">{data.title ?? page.slugs.join(" / ")}</h3>
      {data.description && (
        <p className="text-sm text-fd-muted-foreground mb-3 line-clamp-2">
          {data.description}
        </p>
      )}
      <div className="flex items-center gap-4 text-xs text-fd-muted-foreground">
        {data.date && (
          <span className="flex items-center gap-1">
            <Calendar className="h-3 w-3" />
            {data.date}
          </span>
        )}
        {data.tags && data.tags.length > 0 && (
          <span className="flex items-center gap-1">
            <Tag className="h-3 w-3" />
            {data.tags.slice(0, 3).join(", ")}
            {data.tags.length > 3 && ` +${data.tags.length - 3}`}
          </span>
        )}
      </div>
    </Link>
  );
}
