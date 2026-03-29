import { defineDocs, frontmatterSchema } from "fumadocs-mdx/config";
import { z } from "zod";

// Define collections for each notes directory
export const { docs, meta } = defineDocs({
  dir: "content/docs",
  docs: {
    schema: frontmatterSchema.extend({
      // Custom frontmatter fields for scripture study notes
      tags: z.array(z.string()).optional().default([]),
      date: z.string().optional(),
      scripture: z.string().optional(),
      category: z.enum([
        "old-testament",
        "new-testament",
        "book-of-mormon",
        "conference",
        "parallels",
        "personal",
      ]).optional(),
    }),
  },
});
