import React from "react";

export const LoadingIndicator: React.FC = () => (
  <div className="flex justify-start">
    <div className="bg-zinc-900/50 border border-zinc-800/50 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center space-x-3">
        <div className="relative">
          <div className="animate-spin rounded-full h-5 w-5 border-2 border-zinc-600 border-t-blue-400"></div>
          <div className="absolute inset-0 rounded-full bg-blue-400/20 animate-pulse"></div>
        </div>
        <span className="text-sm text-zinc-300 font-medium">
          Researching and analyzing...
        </span>
      </div>
    </div>
  </div>
);