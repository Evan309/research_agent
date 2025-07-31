import { Search, FileText, Database } from "lucide-react";
import type { ResearchType } from "../types";

export const getResearchIcon = (type?: ResearchType) => {
  const iconMap = {
    academic: FileText,
    database: Database,
    web: Search,
  } as const;

  const IconComponent = iconMap[type || "web"];
  return <IconComponent className="h-4 w-4" />;
};