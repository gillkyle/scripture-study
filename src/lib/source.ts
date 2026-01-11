import { docs, meta } from "@/.source";
import { createMDXSource } from "fumadocs-mdx/runtime/vite";
import { loader } from "fumadocs-core/source";

export const source = loader({
  baseUrl: "/docs",
  source: createMDXSource(docs, meta),
});

// Helper function to get all unique tags from all docs
export function getAllTags(): { tag: string; count: number }[] {
  const pages = source.getPages();
  const tagCounts = new Map<string, number>();

  for (const page of pages) {
    const tags = (page.data as { tags?: string[] }).tags ?? [];
    for (const tag of tags) {
      tagCounts.set(tag, (tagCounts.get(tag) ?? 0) + 1);
    }
  }

  return Array.from(tagCounts.entries())
    .map(([tag, count]) => ({ tag, count }))
    .sort((a, b) => b.count - a.count);
}

// Helper function to get pages by tag
export function getPagesByTag(tag: string) {
  const pages = source.getPages();
  return pages.filter((page) => {
    const tags = (page.data as { tags?: string[] }).tags ?? [];
    return tags.includes(tag);
  });
}

// Helper function to search pages by text
export function searchPages(query: string) {
  const pages = source.getPages();
  const lowerQuery = query.toLowerCase();

  return pages.filter((page) => {
    const title = page.data.title?.toLowerCase() ?? "";
    const description = page.data.description?.toLowerCase() ?? "";
    const tags = ((page.data as { tags?: string[] }).tags ?? []).join(" ").toLowerCase();

    return (
      title.includes(lowerQuery) ||
      description.includes(lowerQuery) ||
      tags.includes(lowerQuery)
    );
  });
}
