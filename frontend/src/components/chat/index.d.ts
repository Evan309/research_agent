import React from "react";
import type { Message } from "../../types/index";
interface ChatProps {
    messages: Message[];
    isLoading: boolean;
    error: string | null;
    onSendMessage: (message: string) => void;
    onClearError?: () => void;
}
export declare const Chat: React.FC<ChatProps>;
export {};
