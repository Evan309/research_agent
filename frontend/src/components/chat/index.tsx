import React from "react";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Badge } from "@/components/ui/badge";
import { Sparkles } from "lucide-react";
import { MessageBubble } from "./message_bubble";
import { LoadingIndicator } from "./loading_indicator";
import { ChatInput } from "./chat_input";
import type { Message } from "../../types/index";

interface ChatProps {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
  onSendMessage: (message: string) => void;
  onClearError?: () => void;
}

export const Chat: React.FC<ChatProps> = ({
  messages,
  isLoading,
  error,
  onSendMessage,
  onClearError,
}) => {
  return (
    <div className="flex-1 flex flex-col">
      {/* Header */}
      <div className="bg-zinc-950/80 backdrop-blur-xl border-b border-zinc-800/50 p-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-gradient-to-br from-blue-500/20 to-purple-500/20 rounded-xl">
              <Sparkles className="h-6 w-6 text-blue-400" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-zinc-100">Research Assistant</h1>
              <p className="text-sm text-zinc-400">Advanced AI-powered research</p>
            </div>
          </div>
          <div className="flex items-center space-x-3">
            <Badge className="bg-emerald-500/20 text-emerald-400 border-emerald-500/30 px-3 py-1 rounded-full">
              <div className="w-2 h-2 bg-emerald-400 rounded-full mr-2 animate-pulse"></div>
              Online
            </Badge>
          </div>
        </div>
      </div>

      {/* Messages */}
      <ScrollArea className="flex-1 p-6">
        <div className="max-w-4xl mx-auto space-y-8">
          {error && (
            <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-400 text-sm">
              Error: {error}
              {onClearError && (
                <button 
                  onClick={onClearError}
                  className="ml-2 underline hover:no-underline"
                >
                  Dismiss
                </button>
              )}
            </div>
          )}
          
          {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
          ))}

          {isLoading && <LoadingIndicator />}
        </div>
      </ScrollArea>

      {/* Input Area */}
      <ChatInput onSendMessage={onSendMessage} isLoading={isLoading} />
    </div>
  );
};