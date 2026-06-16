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
      padding: '8px',
      backgroundColor: 'white',
      borderRadius: '4px',
      border: '1px solid var(--border-color)',
      display: 'flex',
      flexDirection: 'column',
      gap: '2px'
    }}>
      <div style={{ fontSize: '10px', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
        {label}
      </div>
      <div style={{ fontSize: '14px', fontWeight: '700', color: 'var(--text-main)' }}>
        {value.toLocaleString()} <span style={{ fontSize: '11px', fontWeight: '400', color: 'var(--text-muted)' }}>{unit}</span>
      </div>
    </div>
  );
};

export default React.memo(AnalysisCard);
