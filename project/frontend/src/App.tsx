import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import MainViewerPage from "./pages/MainViewerPage";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <MainViewerPage />
    </QueryClientProvider>
  );
}

export default App;