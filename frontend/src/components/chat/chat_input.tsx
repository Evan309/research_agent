import React, { useState } from "react";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { Search, Send } from "lucide-react";

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  isLoading: boolean;
  placeholder?: string;
}

export const ChatInput: React.FC<ChatInputProps> = ({
  onSendMessage,
  isLoading,
  placeholder = "Ask me to research anything...",
}) => {
  const [input, setInput] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;
    
    onSendMessage(input);
    setInput("");
  };

  return (
    <div className="bg-zinc-950/80 backdrop-blur-xl border-t border-zinc-800/50 p-6">
      <div className="max-w-4xl mx-auto">
        <form onSubmit={handleSubmit} className="flex space-x-4">
          <div className="flex-1 relative">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder={placeholder}
              className="pr-12 bg-zinc-900/50 border-zinc-800/50 text-zinc-100 placeholder-zinc-500 focus:border-blue-500/50 focus:ring-blue-500/25 rounded-xl h-14 text-base backdrop-blur-sm transition-all duration-200"
              disabled={isLoading}
            />
            <Search className="absolute right-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-zinc-400" />
          </div>
          <Button
            type="submit"
            disabled={isLoading || !input.trim()}
            className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 h-14 px-6 rounded-xl font-medium shadow-lg shadow-blue-500/25 transition-all duration-200 disabled:opacity-50"
          >
            <Send className="h-5 w-5" />
          </Button>
        </form>
        <p className="text-xs text-zinc-500 mt-4 text-center">
          Advanced AI research across academic papers, databases, and web sources
        </p>
      </div>
    </div>
  );
};