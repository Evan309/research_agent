import React from "react";
import type { Conversation } from "../../types/index";
interface ConversationItemProps {
    conversation: Conversation;
    onClick?: (id: string) => void;
    isActive?: boolean;
}
export declare const ConversationItem: React.FC<ConversationItemProps>;
export {};
