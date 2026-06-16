import React from 'react';

interface AnalysisCardProps {
  label: string;
  value: number;
  unit?: string;
}

/**
 * 특정 폴리곤의 면적 정보 등 분석 수치를 시각적으로 강조하는 카드 컴포넌트
 */
const AnalysisCard: React.FC<AnalysisCardProps> = ({ label, value, unit = '㎡' }) => {
  return (
    <div style={{
      padding: '16px',
      backgroundColor: '#f8f9fa',
      borderRadius: '8px',
      border: '1px solid #dee2e6',
      marginBottom: '12px'
    }}>
      <div style={{ fontSize: '14px', color: '#6c757d', marginBottom: '4px' }}>
        {label}
      </div>
      <div style={{ fontSize: '20px', fontWeight: 'bold', color: '#212529' }}>
        {value.toLocaleString()} <span style={{ fontSize: '14px', fontWeight: 'normal' }}>{unit}</span>
      </div>
    </div>
  );
};

export default React.memo(AnalysisCard);
