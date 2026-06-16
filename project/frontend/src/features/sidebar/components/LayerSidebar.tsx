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
      width: '300px',
      height: '100%',
      backgroundColor: 'white',
      borderRight: '1px solid #ddd',
      padding: '20px',
      display: 'flex',
      flexDirection: 'column',
      zIndex: 1001
    }}>
      <h2 style={{ fontSize: '20px', marginBottom: '20px' }}>레이어 목록</h2>
      
      <div style={{ flex: 1, overflowY: 'auto' }}>
        {layers.length === 0 ? (
          <p style={{ color: '#999', textAlign: 'center' }}>업로드된 레이어가 없습니다.</p>
        ) : (
          layers.map((layer) => (
            <div key={layer.id} style={{ 
              marginBottom: '20px', 
              padding: '12px', 
              border: '1px solid #eee', 
              borderRadius: '8px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                <span style={{ fontWeight: '600' }}>{layer.name}</span>
                <div>
                  <input 
                    type="checkbox" 
                    checked={layer.visible} 
                    onChange={() => toggleLayerVisibility(layer.id)} 
                  />
                  <button 
                    onClick={() => removeLayer(layer.id)}
                    style={{ marginLeft: '8px', color: 'red', border: 'none', background: 'none', cursor: 'pointer' }}
                  >
                    삭제
                  </button>
                </div>
              </div>

              {layer.analysis && layer.analysis.analysis_results && (
                <div style={{ marginTop: '10px' }}>
                  {layer.analysis.analysis_results.map((result: any, idx: number) => (
                    <div key={idx} style={{ marginBottom: '8px', padding: '8px', backgroundColor: '#f9f9f9', borderRadius: '4px' }}>
                      <div style={{ fontSize: '12px', fontWeight: 'bold' }}>{result.properties.name || `피처 ${idx + 1}`}</div>
                      <AnalysisCard label="면적" value={result.area_sqm} unit="㎡" />
                      <AnalysisCard label="면적 (평)" value={result.area_pyung} unit="평" />
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
