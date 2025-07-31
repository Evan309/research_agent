import type { Source, Conversation } from "../types";

export const generateMockSources = (query: string): Source[] => [
  {
    title: `Research Paper on ${query}`,
    url: "https://example.com/research",
    snippet: "This comprehensive study examines the latest developments and provides detailed analysis...",
    domain: "academic.edu",
  },
  {
    title: `Industry Report: ${query}`,
    url: "https://example.com/report",
    snippet: "Market analysis and trends showing significant growth in this sector...",
    domain: "industry.com",
  },
];

export const mockConversations: Conversation[] = [
  { 
    id: "1", 
    title: "Climate Change Research", 
    lastMessage: new Date(), 
    messageCount: 12 
  },
  { 
    id: "2", 
    title: "AI Ethics Analysis", 
    lastMessage: new Date(Date.now() - 86400000), 
    messageCount: 8 
  },
  { 
    id: "3", 
    title: "Market Trends 2024", 
    lastMessage: new Date(Date.now() - 172800000), 
    messageCount: 15 
  },
];