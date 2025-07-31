import React from "react";
import { Card } from "@/components/ui/card";
import { MessageSquare } from "lucide-react";
import type { Conversation } from "../../types/index";

interface ConversationItemProps {
  conversation: Conversation;
  onClick?: (id: string) => void;
  isActive?: boolean;
}

export const ConversationItem: React.FC<ConversationItemProps> = ({
  conversation,
  onClick,
  isActive = false,
}) => {
  return (
    <Card
      className={`p-4 hover:bg-zinc-900/50 cursor-pointer transition-all duration-200 bg-zinc-950/50 border-zinc-800/30 rounded-xl backdrop-blur-sm hover:border-zinc-700/50 group ${
        isActive ? 'border-blue-500/50 bg-blue-500/10' : ''
      }`}
      onClick={() => onClick?.(conversation.id)}
    >
      <div className="flex items-start space-x-3">
        <div className="p-2 bg-zinc-800/50 rounded-lg group-hover:bg-zinc-700/50 transition-colors">
          <MessageSquare className="h-4 w-4 text-zinc-400" />
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-sm font-medium text-zinc-100 truncate mb-1">
            {conversation.title}
          </p>
          <p className="text-xs text-zinc-500">
            {conversation.messageCount} messages
          </p>
        </div>
      </div>
    </Card>
  );
};