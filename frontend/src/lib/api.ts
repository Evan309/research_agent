const API_BASE_URL = 'http://localhost:8000';

export interface QueryRequest {
  query: string;
}

export interface ResearchResults {
  datasets?: any[];
  papers?: any[];
  news?: any[];
  response?: string;
}

export interface QueryResponse {
  topic: string | null;
  intent: string | null;
  response: string | null;
  research_results: ResearchResults | null;
}

class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
  }

  async query(request: QueryRequest): Promise<QueryResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }
}

export const apiClient = new ApiClient(); 