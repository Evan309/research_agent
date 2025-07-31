import React from "react";
import { Card } from "../ui/card";
import { Button } from "../ui/button";
import { Badge } from "../ui/badge";
import { Separator } from "../ui/separator";
import { FileText, ExternalLink, Zap } from "lucide-react";
import { getResearchIcon } from "../../utils/icons";
import type { Message } from "../../types/index";

interface MessageBubbleProps {
  message: Message;
}

export const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const isUser = message.role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[85%] ${
          isUser
            ? "bg-gradient-to-br from-blue-600 to-blue-700 text-white shadow-lg shadow-blue-500/25"
            : "bg-zinc-900/50 border border-zinc-800/50 text-zinc-100 backdrop-blur-sm"
        } rounded-2xl p-6 transition-all duration-200`}
      >
        {!isUser && message.researchType && (
          <div className="flex items-center space-x-2 mb-4 text-sm text-zinc-400">
            <div className="p-1.5 bg-zinc-800/50 rounded-lg">
              {getResearchIcon(message.researchType)}
            </div>
            <span className="font-medium">Research completed</span>
            <Zap className="h-3 w-3 text-yellow-400" />
          </div>
        )}

        <p className={`text-sm leading-relaxed ${isUser ? "text-white" : "text-zinc-100"}`}>
          {message.content}
        </p>

        {message.sources && (
          <div className="mt-6 space-y-3">
            <Separator className="bg-zinc-700/50" />
            <p className="text-xs font-bold text-zinc-400 uppercase tracking-wider flex items-center">
              <FileText className="h-3 w-3 mr-2" />
              Research Sources
            </p>
            {message.sources.map((source, index) => (
              <Card
                key={index}
                className="p-4 bg-zinc-800/30 border-zinc-700/30 rounded-xl backdrop-blur-sm hover:bg-zinc-800/50 transition-all duration-200"
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <h4 className="text-sm font-semibold text-zinc-100 mb-2">
                      {source.title}
                    </h4>
                    <p className="text-xs text-zinc-300 mb-3 leading-relaxed">
                      {source.snippet}
                    </p>
                    <div className="flex items-center space-x-2">
                      <Badge className="text-xs bg-zinc-700/50 text-zinc-300 border-zinc-600/50 rounded-lg px-2 py-1">
                        {source.domain}
                      </Badge>
                    </div>
                  </div>
                  <Button
                    size="sm"
                    variant="ghost"
                    className="ml-3 hover:bg-zinc-700/50 text-zinc-400 hover:text-zinc-200 rounded-lg"
                    onClick={() => window.open(source.url, '_blank')}
                  >
                    <ExternalLink className="h-4 w-4" />
                  </Button>
                </div>
              </Card>
            ))}
          </div>
        )}

        <p className={`text-xs mt-4 ${isUser ? "text-blue-100" : "text-zinc-500"}`}>
          {message.timestamp.toLocaleTimeString()}
        </p>
      </div>
    </div>
  );
};