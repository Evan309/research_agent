import React from "react";
import type { Conversation } from "../../types/index";
interface SidebarProps {
    conversations?: Conversation[];
    onNewSession?: () => void;
    onConversationSelect?: (id: string) => void;
    activeConversationId?: string;
}
export declare const Sidebar: React.FC<SidebarProps>;
export {};
