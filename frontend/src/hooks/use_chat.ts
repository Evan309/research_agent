import { useState, useCallback } from "react";
import type { Message, ChatState } from "../types";
import { generateMockSources } from "../utils/mock_data";

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
      // Simulate API call - replace with actual research service
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: `I've found several relevant sources about "${content}". Based on my research, here are the key findings and insights from multiple databases and academic sources.`,
        timestamp: new Date(),
        researchType: "web",
        sources: generateMockSources(content),
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
        error: error instanceof Error ? error.message : "An error occurred",
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