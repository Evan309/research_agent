import { useState } from "react";
import { Sidebar } from "./components/sidebar";
import { Chat } from "./components/chat";
import { useChat } from "./hooks/use_chat";

export default function App() {
  const [activeConversationId, setActiveConversationId] = useState<string>("1");
  const { messages, isLoading, error, sendMessage, clearError } = useChat();

  const handleNewSession = () => {
    // In a real app, this would create a new conversation
    console.log("Starting new research session");
  };

  const handleConversationSelect = (id: string) => {
    setActiveConversationId(id);
    // In a real app, this would load the selected conversation
    console.log(`Loading conversation: ${id}`);
  };

  return (
    <div className="flex h-screen bg-black">
      <Sidebar
        onNewSession={handleNewSession}
        onConversationSelect={handleConversationSelect}
        activeConversationId={activeConversationId}
      />
      <Chat
        messages={messages}
        isLoading={isLoading}
        error={error}
        onSendMessage={sendMessage}
        onClearError={clearError}
      />
    </div>
  );
} 