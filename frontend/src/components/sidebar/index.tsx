import React from "react";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Plus, Brain } from "lucide-react";
import { ConversationItem } from "./conversation_item";
import { mockConversations } from "../../utils/mock_data";
import type { Conversation } from "../../types/index";

interface SidebarProps {
  conversations?: Conversation[];
  onNewSession?: () => void;
  onConversationSelect?: (id: string) => void;
  activeConversationId?: string;
}

export const Sidebar: React.FC<SidebarProps> = ({
  conversations = mockConversations,
  onNewSession,
  onConversationSelect,
  activeConversationId,
}) => {
  return (
    <div className="w-72 bg-zinc-950 border-r border-zinc-800/50 flex flex-col backdrop-blur-xl">
      <div className="p-6 border-b border-zinc-800/50">
        <Button
          onClick={onNewSession}
          className="w-full justify-start bg-gradient-to-r from-zinc-800 to-zinc-900 hover:from-zinc-700 hover:to-zinc-800 text-zinc-100 border-zinc-700/50 rounded-xl h-12 font-medium transition-all duration-200 shadow-lg"
          variant="outline"
        >
          <Plus className="h-5 w-5 mr-3" />
          New Research Session
        </Button>
      </div>

      <ScrollArea className="flex-1 p-6">
        <div className="space-y-3">
          <h3 className="text-sm font-semibold text-zinc-400 mb-4 uppercase tracking-wider">
            Recent Sessions
          </h3>
          {conversations.map((conversation) => (
            <ConversationItem
              key={conversation.id}
              conversation={conversation}
              onClick={onConversationSelect}
              isActive={activeConversationId === conversation.id}
            />
          ))}
        </div>
      </ScrollArea>

      <div className="p-6 border-t border-zinc-800/50">
        <div className="flex items-center space-x-3 text-sm text-zinc-400">
          <div className="p-2 bg-gradient-to-br from-purple-500/20 to-blue-500/20 rounded-lg">
            <Brain className="h-4 w-4 text-purple-400" />
          </div>
          <div>
            <p className="font-medium text-zinc-300">AI Research Agent</p>
            <p className="text-xs text-zinc-500">Powered by advanced AI</p>
          </div>
        </div>
      </div>
    </div>
  );
};