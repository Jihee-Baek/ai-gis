import React from 'react';
import { useMapStore } from '../../../stores/mapStore';
import AnalysisCard from '../../analysis/components/AnalysisCard';

/**
 * 활성 레이어 관리 및 공간 분석 결과 요약을 보여주는 사이드바 컴포넌트
 */
const LayerSidebar: React.FC = () => {
  const { layers, toggleLayerVisibility, removeLayer } = useMapStore();

  return (
    <div style={{
      width: '320px',
      height: '100%',
      backgroundColor: 'var(--bg-sidebar)',
      borderRight: '1px solid var(--border-color)',
      padding: '24px',
      display: 'flex',
      flexDirection: 'column',
      zIndex: 1001,
      boxShadow: '2px 0 8px rgba(0,0,0,0.02)'
    }}>
      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ fontSize: '20px', fontWeight: '700', color: 'var(--primary-dark)', margin: 0 }}>데이터 레이어</h2>
        <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginTop: '4px' }}>시각화 및 분석 관리</p>
      </div>
      
      <div style={{ flex: 1, overflowY: 'auto', paddingRight: '4px' }}>
        {layers.length === 0 ? (
          <div style={{ 
            marginTop: '40px', 
            textAlign: 'center', 
            color: 'var(--text-muted)',
            padding: '20px',
            backgroundColor: 'var(--bg-main)',
            borderRadius: 'var(--radius)',
            fontSize: '14px'
          }}>
            추가된 데이터 레이어가 없습니다.
          </div>
        ) : (
          layers.map((layer) => (
            <div key={layer.id} style={{ 
              marginBottom: '16px', 
              padding: '16px', 
              backgroundColor: 'white',
              border: '1px solid var(--border-color)', 
              borderRadius: 'var(--radius)',
              boxShadow: 'var(--shadow-sm)'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
                <span style={{ fontWeight: '600', color: 'var(--text-main)', fontSize: '15px' }}>{layer.name}</span>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <input 
                    type="checkbox" 
                    checked={layer.visible} 
                    onChange={() => toggleLayerVisibility(layer.id)} 
                    style={{ cursor: 'pointer', width: '16px', height: '16px' }}
                  />
                  <button 
                    onClick={() => removeLayer(layer.id)}
                    style={{ 
                      color: '#ef4444', 
                      border: 'none', 
                      background: 'none', 
                      cursor: 'pointer',
                      fontSize: '12px',
                      padding: '4px'
                    }}
                  >
                    삭제
                  </button>
                </div>
              </div>

              {layer.analysis && layer.analysis.analysis_results && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  {layer.analysis.analysis_results.map((result: any, idx: number) => (
                    <div key={idx} style={{ 
                      padding: '12px', 
                      backgroundColor: 'var(--bg-main)', 
                      borderRadius: '6px',
                      border: '1px solid rgba(0,0,0,0.03)'
                    }}>
                      <div style={{ fontSize: '12px', fontWeight: '700', color: 'var(--primary-color)', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '5px' }}>
                         <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: 'var(--accent-color)' }}></span>
                         {result.properties.name || `객체 ${idx + 1}`}
                      </div>
                      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                        <AnalysisCard label="면적" value={result.area_sqm} unit="㎡" />
                        <AnalysisCard label="평수" value={result.area_pyung} unit="평" />
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default React.memo(LayerSidebar);
