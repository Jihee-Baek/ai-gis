import React from 'react';
import { useFeatureStore } from '../../../stores/featureStore';

/**
 * 선택된 지리 객체의 속성 정보를 표 형식으로 시각화하는 패널
 */
const PropertyInspector: React.FC = () => {
  const { selectedFeature, clearSelection } = useFeatureStore();

  if (!selectedFeature) return null;

  const properties = selectedFeature.properties || {};

  return (
    <div style={{
      position: 'absolute',
      right: '20px',
      bottom: '20px',
      width: '320px',
      maxHeight: '400px',
      backgroundColor: 'white',
      boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
      borderRadius: '8px',
      overflow: 'hidden',
      display: 'flex',
      flexDirection: 'column',
      zIndex: 1000
    }}>
      <div style={{
        padding: '12px 16px',
        borderBottom: '1px solid #eee',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        backgroundColor: '#f8f9fa'
      }}>
        <h3 style={{ margin: 0, fontSize: '16px' }}>객체 속성 정보</h3>
        <button 
          onClick={clearSelection}
          style={{ border: 'none', background: 'none', cursor: 'pointer', fontSize: '18px' }}
        >
          &times;
        </button>
      </div>
      <div style={{ overflowY: 'auto', padding: '0 16px' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
          <tbody>
            {Object.entries(properties).map(([key, value]) => (
              <tr key={key} style={{ borderBottom: '1px solid #f0f0f0' }}>
                <td style={{ padding: '8px 0', fontWeight: '600', color: '#666', width: '40%' }}>{key}</td>
                <td style={{ padding: '8px 0', color: '#333', wordBreak: 'break-all' }}>{String(value)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default React.memo(PropertyInspector);
