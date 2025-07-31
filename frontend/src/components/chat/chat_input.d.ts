import React from "react";
interface ChatInputProps {
    onSendMessage: (message: string) => void;
    isLoading: boolean;
    placeholder?: string;
}
export declare const ChatInput: React.FC<ChatInputProps>;
export {};
