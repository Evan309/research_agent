import { useState, useCallback } from "react";
import type { Message, ChatState } from "../types";
import { apiClient, type QueryResponse } from "../lib/api";

export const useChat = () => {
  const [state, setState] = useState<ChatState>({
    messages: [
      {
        id: "1",
        role: "assistant",
        content: "Hello! I'm your AI research assistant. I can help you find information, analyze data, and retrieve insights from various sources. What would you like to research today?",
        timestamp: new Date(),
      },
    ],
    isLoading: false,
    error: null,
  });

  const sendMessage = useCallback(async (content: string): Promise<void> => {
    if (!content.trim() || state.isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content,
      timestamp: new Date(),
    };

    setState(prev => ({
      ...prev,
      messages: [...prev.messages, userMessage],
      isLoading: true,
      error: null,
    }));

    try {
      // Call the FastAPI backend
      const response: QueryResponse = await apiClient.query({ query: content });
      
      let assistantContent = "";
      let researchType: "web" | "academic" | "database" = "web";
      let sources: any[] = [];

      if (response.intent === "chat") {
        assistantContent = response.response || "I'm here to help! What would you like to know?";
      } else if (response.intent === "research") {
        assistantContent = response.research_results?.response || "I've completed my research. Here are the findings:";
        
        // Collect sources from research results
        if (response.research_results) {
          if (response.research_results.datasets) {
            sources.push(...response.research_results.datasets.map((dataset: any) => ({
              title: dataset.title || "Dataset",
              url: dataset.url || "#",
              snippet: dataset.description || "Dataset information",
              domain: "kaggle.com"
            })));
          }
          if (response.research_results.papers) {
            sources.push(...response.research_results.papers.map((paper: any) => ({
              title: paper.title || "Research Paper",
              url: paper.url || "#",
              snippet: paper.abstract || "Academic paper",
              domain: "core.ac.uk"
            })));
          }
          if (response.research_results.news) {
            sources.push(...response.research_results.news.map((news: any) => ({
              title: news.title || "News Article",
              url: news.url || "#",
              snippet: news.description || "News information",
              domain: "gnews.io"
            })));
          }
        }
        
        researchType = "academic";
      }

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: assistantContent,
        timestamp: new Date(),
        researchType,
        sources: sources.length > 0 ? sources : undefined,
      };

      setState(prev => ({
        ...prev,
        messages: [...prev.messages, assistantMessage],
        isLoading: false,
      }));
    } catch (error) {
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: error instanceof Error ? error.message : "An error occurred while connecting to the research service",
      }));
    }
  }, [state.isLoading]);

  const clearError = useCallback(() => {
    setState(prev => ({ ...prev, error: null }));
  }, []);

  return {
    ...state,
    sendMessage,
    clearError,
  };
};