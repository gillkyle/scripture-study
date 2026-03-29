import { createFileRoute, Outlet } from "@tanstack/react-router";
import { DocsLayout } from "fumadocs-ui/layouts/docs";
import { baseOptions } from "@/lib/layout";
import { source } from "@/lib/source";

export const Route = createFileRoute("/docs")({
  component: DocsLayoutComponent,
});

function DocsLayoutComponent() {
  return (
    <DocsLayout
      {...baseOptions}
      tree={source.pageTree}
      sidebar={{
        banner: (
          <div className="p-3 bg-fd-muted rounded-lg text-sm">
            <p className="font-medium mb-1">Scripture Study Notes</p>
            <p className="text-fd-muted-foreground text-xs">
              Personal insights and study materials
            </p>
          </div>
        ),
      }}
    >
      <Outlet />
    </DocsLayout>
  );
}
