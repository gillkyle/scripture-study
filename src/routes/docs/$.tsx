import { createFileRoute, notFound } from "@tanstack/react-router";
import { source } from "@/lib/source";
import { DocsPage, DocsBody, DocsTitle, DocsDescription } from "fumadocs-ui/page";
import { Tag, Calendar, BookOpen } from "lucide-react";

export const Route = createFileRoute("/docs/$")({
  component: DocsPageComponent,
  loader: async ({ params }) => {
    const slug = params._ ?? "";
    const slugs = slug.split("/").filter(Boolean);
    const page = source.getPage(slugs);

    if (!page) {
      throw notFound();
    }

    return { page, slugs };
  },
});

function DocsPageComponent() {
  const { page } = Route.useLoaderData();

  const data = page.data as {
    title?: string;
    description?: string;
    tags?: string[];
    date?: string;
    scripture?: string;
    category?: string;
  };

  const MDXContent = page.data.body;

  return (
    <DocsPage
      toc={page.data.toc}
      lastUpdate={data.date ? new Date(data.date) : undefined}
      tableOfContent={{
        style: "clerk",
        single: false,
      }}
    >
      <DocsTitle>{data.title}</DocsTitle>
      {data.description && <DocsDescription>{data.description}</DocsDescription>}

      {/* Metadata bar */}
      <div className="flex flex-wrap gap-4 text-sm text-fd-muted-foreground mb-6 pb-4 border-b border-fd-border">
        {data.date && (
          <span className="flex items-center gap-1">
            <Calendar className="h-4 w-4" />
            {data.date}
          </span>
        )}
        {data.scripture && (
          <span className="flex items-center gap-1">
            <BookOpen className="h-4 w-4" />
            {data.scripture}
          </span>
        )}
      </div>

      {/* Tags */}
      {data.tags && data.tags.length > 0 && (
        <div className="flex flex-wrap gap-2 mb-6">
          {data.tags.map((tag) => (
            <a
              key={tag}
              href={`/tags/${encodeURIComponent(tag)}`}
              className="inline-flex items-center gap-1 px-2 py-1 text-xs bg-fd-muted text-fd-muted-foreground rounded-md hover:bg-fd-accent transition-colors"
            >
              <Tag className="h-3 w-3" />
              {tag}
            </a>
          ))}
        </div>
      )}

      <DocsBody>
        <MDXContent />
      </DocsBody>
    </DocsPage>
  );
}
