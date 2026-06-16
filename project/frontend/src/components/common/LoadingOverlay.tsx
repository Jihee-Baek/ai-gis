import React from 'react';

interface LoadingOverlayProps {
  isVisible: boolean;
  message?: string;
}

/**
 * 비동기 작업 중 사용자의 상호작용을 제어하고 진행 상태를 알리는 오버레이 컴포넌트
 */
const LoadingOverlay: React.FC<LoadingOverlayProps> = ({ isVisible, message = '데이터를 처리 중입니다...' }) => {
  if (!isVisible) return null;

  return (
    <div style={{
      position: 'fixed',
      top: 0, left: 0, right: 0, bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex', flexDirection: 'column',
      justifyContent: 'center', alignItems: 'center',
      zIndex: 9999,
      color: 'white'
    }}>
      <div className="spinner" style={{
        border: '4px solid rgba(255, 255, 255, 0.3)',
        borderTop: '4px solid #ffffff',
        borderRadius: '50%',
        width: '40px',
        height: '40px',
        animation: 'spin 1s linear infinite',
        marginBottom: '10px'
      }} />
      <p>{message}</p>
      <style>{`
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
};

export default React.memo(LoadingOverlay);
