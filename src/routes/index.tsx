import { createFileRoute, Link } from "@tanstack/react-router";
import { HomeLayout } from "fumadocs-ui/layouts/home";
import { baseOptions } from "@/lib/layout";
import { BookOpen, Tags, Search, ArrowRight, Calendar } from "lucide-react";

export const Route = createFileRoute("/")({
  component: HomePage,
});

function HomePage() {
  return (
    <HomeLayout {...baseOptions}>
      <main className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl font-bold tracking-tight sm:text-6xl mb-6">
            Scripture Study
          </h1>
          <p className="text-xl text-fd-muted-foreground mb-12">
            Personal notes and insights from studying the scriptures.
            Old Testament, Book of Mormon, General Conference, and more.
          </p>

          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3 mb-12">
            <FeatureCard
              icon={<BookOpen className="h-8 w-8" />}
              title="Study Notes"
              description="Browse all scripture study notes organized by topic and source."
              href="/docs"
            />
            <FeatureCard
              icon={<Tags className="h-8 w-8" />}
              title="Browse Tags"
              description="Explore notes by tags like themes, books, and topics."
              href="/tags"
            />
            <FeatureCard
              icon={<Search className="h-8 w-8" />}
              title="Search"
              description="Search across all notes to find specific topics or scriptures."
              href="/docs"
            />
          </div>

          <div className="bg-fd-card border border-fd-border rounded-lg p-8 text-left">
            <h2 className="text-2xl font-semibold mb-4 flex items-center gap-2">
              <Calendar className="h-6 w-6" />
              Come Follow Me 2025
            </h2>
            <p className="text-fd-muted-foreground mb-4">
              This year's study focuses on the Old Testament. Discover
              insights from Genesis through Malachi, exploring themes of
              creation, covenant, prophecy, and the coming Messiah.
            </p>
            <Link
              to="/docs"
              className="inline-flex items-center text-fd-primary hover:underline"
            >
              Start Reading <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </main>
    </HomeLayout>
  );
}

function FeatureCard({
  icon,
  title,
  description,
  href,
}: {
  icon: React.ReactNode;
  title: string;
  description: string;
  href: string;
}) {
  return (
    <Link
      to={href}
      className="block p-6 bg-fd-card border border-fd-border rounded-lg hover:border-fd-primary transition-colors"
    >
      <div className="text-fd-primary mb-4">{icon}</div>
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <p className="text-fd-muted-foreground text-sm">{description}</p>
    </Link>
  );
}
