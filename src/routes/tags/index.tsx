import { createFileRoute, Link } from "@tanstack/react-router";
import { HomeLayout } from "fumadocs-ui/layouts/home";
import { baseOptions } from "@/lib/layout";
import { getAllTags } from "@/lib/source";
import { Tags as TagsIcon, Hash } from "lucide-react";

export const Route = createFileRoute("/tags/")({
  component: TagsPage,
});

function TagsPage() {
  const tags = getAllTags();

  return (
    <HomeLayout {...baseOptions}>
      <main className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto">
          <div className="mb-8">
            <h1 className="text-3xl font-bold mb-4 flex items-center gap-3">
              <TagsIcon className="h-8 w-8" />
              Browse Tags
            </h1>
            <p className="text-fd-muted-foreground">
              Explore scripture study notes by topic. Click a tag to see all related notes.
            </p>
          </div>

          {tags.length === 0 ? (
            <div className="text-center py-12 text-fd-muted-foreground">
              <Hash className="h-12 w-12 mx-auto mb-4 opacity-50" />
              <p>No tags yet. Add tags to your notes to see them here!</p>
            </div>
          ) : (
            <div className="flex flex-wrap gap-3">
              {tags.map(({ tag, count }) => (
                <Link
                  key={tag}
                  to={`/tags/${encodeURIComponent(tag)}`}
                  className="inline-flex items-center gap-2 px-4 py-2 bg-fd-card border border-fd-border rounded-lg hover:border-fd-primary transition-colors"
                >
                  <Hash className="h-4 w-4 text-fd-muted-foreground" />
                  <span className="font-medium">{tag}</span>
                  <span className="text-xs text-fd-muted-foreground bg-fd-muted px-2 py-0.5 rounded-full">
                    {count}
                  </span>
                </Link>
              ))}
            </div>
          )}
        </div>
      </main>
    </HomeLayout>
  );
}
