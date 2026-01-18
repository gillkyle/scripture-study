import { createFileRoute, Link } from "@tanstack/react-router";
import { HomeLayout } from "fumadocs-ui/layouts/home";
import { baseOptions } from "@/lib/layout";
import { getPagesByTag, source } from "@/lib/source";
import { ArrowLeft, Hash, Calendar, Tag, BookOpen } from "lucide-react";

export const Route = createFileRoute("/tags/$tag")({
  component: TagPage,
  loader: async ({ params }) => {
    const tag = decodeURIComponent(params.tag);
    const pages = getPagesByTag(tag);
    return { tag, pages };
  },
});

function TagPage() {
  const { tag, pages } = Route.useLoaderData();

  return (
    <HomeLayout {...baseOptions}>
      <main className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto">
          <Link
            to="/tags"
            className="inline-flex items-center gap-2 text-fd-muted-foreground hover:text-fd-foreground mb-6"
          >
            <ArrowLeft className="h-4 w-4" />
            All Tags
          </Link>

          <div className="mb-8">
            <h1 className="text-3xl font-bold mb-4 flex items-center gap-3">
              <Hash className="h-8 w-8" />
              {tag}
            </h1>
            <p className="text-fd-muted-foreground">
              {pages.length} {pages.length === 1 ? "note" : "notes"} tagged with "{tag}"
            </p>
          </div>

          {pages.length === 0 ? (
            <div className="text-center py-12 text-fd-muted-foreground">
              <BookOpen className="h-12 w-12 mx-auto mb-4 opacity-50" />
              <p>No notes found with this tag.</p>
            </div>
          ) : (
            <div className="grid gap-4 md:grid-cols-2">
              {pages.map((page) => (
                <NoteCard key={page.url} page={page} currentTag={tag} />
              ))}
            </div>
          )}
        </div>
      </main>
    </HomeLayout>
  );
}

function NoteCard({
  page,
  currentTag,
}: {
  page: ReturnType<typeof source.getPages>[0];
  currentTag: string;
}) {
  const data = page.data as {
    title?: string;
    description?: string;
    tags?: string[];
    date?: string;
  };

  const otherTags = (data.tags ?? []).filter((t) => t !== currentTag);

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
      <div className="flex flex-wrap items-center gap-3 text-xs text-fd-muted-foreground">
        {data.date && (
          <span className="flex items-center gap-1">
            <Calendar className="h-3 w-3" />
            {data.date}
          </span>
        )}
        {otherTags.length > 0 && (
          <span className="flex items-center gap-1">
            <Tag className="h-3 w-3" />
            {otherTags.slice(0, 2).join(", ")}
            {otherTags.length > 2 && ` +${otherTags.length - 2}`}
          </span>
        )}
      </div>
    </Link>
  );
}
