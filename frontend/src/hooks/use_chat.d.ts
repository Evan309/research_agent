import type { Message } from "../types";
export declare const useChat: () => {
    sendMessage: (content: string) => Promise<void>;
    clearError: () => void;
    messages: Message[];
    isLoading: boolean;
    error: string | null;
};
