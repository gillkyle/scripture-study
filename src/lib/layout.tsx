import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";
import { BookOpen, Tags, Home, Search } from "lucide-react";

export const baseOptions: BaseLayoutProps = {
  nav: {
    title: (
      <span className="flex items-center gap-2 font-semibold">
        <BookOpen className="h-5 w-5" />
        Scripture Study
      </span>
    ),
  },
  links: [
    {
      text: "Home",
      url: "/",
      icon: <Home className="h-4 w-4" />,
    },
    {
      text: "Notes",
      url: "/docs",
      icon: <BookOpen className="h-4 w-4" />,
    },
    {
      text: "Tags",
      url: "/tags",
      icon: <Tags className="h-4 w-4" />,
    },
  ],
  githubUrl: "https://github.com/gillkyle/scripture-study",
};
