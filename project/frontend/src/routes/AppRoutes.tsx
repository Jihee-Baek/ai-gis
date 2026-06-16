import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainViewerPage from '../pages/MainViewerPage';

/**
 * React Router를 사용하여 경로와 페이지를 매핑하는 컴포넌트
 */
const AppRoutes: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainViewerPage />} />
        {/* 향후 추가 경로 정의 가능 */}
      </Routes>
    </Router>
  );
};

export default AppRoutes;
