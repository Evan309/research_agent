export interface Message {
    id: string;
    role: "user" | "assistant";
    content: string;
    timestamp: Date;
    sources?: Source[];
    researchType?: ResearchType;
  }
  
  export interface Source {
    title: string;
    url: string;
    snippet: string;
    domain: string;
  }
  
  export interface Conversation {
    id: string;
    title: string;
    lastMessage: Date;
    messageCount: number;
  }
  
  export type ResearchType = "web" | "academic" | "database";
  
  export interface ChatState {
    messages: Message[];
    isLoading: boolean;
    error: string | null;
  }