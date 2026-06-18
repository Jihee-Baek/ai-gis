import React, { useCallback, useRef } from 'react';
import { useUploadGeoJson } from '../../../hooks/mutations/useUploadGeoJson';
import { useMapStore } from '../../../stores/mapStore';

/**
 * GeoJSON 파일 드래그 앤 드롭 업로드 인터페이스 컴포넌트
 */
const FileUploader: React.FC = () => {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const { mutate, isPending } = useUploadGeoJson();
  const { addLayer } = useMapStore();

  const handleUpload = useCallback((file: File) => {
    mutate(file, {
      onSuccess: (data) => {
        // 업로드 성공 시 로컬에서 파일 읽기 (지도시각화용)
        const reader = new FileReader();
        reader.onload = (e) => {
          const geoJsonData = JSON.parse(e.target?.result as string);
          addLayer({
            id: String(data.id),
            name: file.name,
            visible: true,
            data: geoJsonData,
            analysis: data
          });
        };
        reader.readAsText(file);
      },
      onError: (error) => {
        alert(`업로드 실패: ${error.message}`);
      }
    });
  }, [mutate, addLayer]);

  const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      handleUpload(e.target.files[0]);
    }
  };

  const onDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (!isPending) {
      e.currentTarget.style.borderColor = 'var(--accent-color)';
      e.currentTarget.style.backgroundColor = 'var(--bg-main)';
    }
  };

  const onDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (!isPending) {
      e.currentTarget.style.borderColor = 'var(--primary-light)';
      e.currentTarget.style.backgroundColor = 'rgba(255,255,255,0.9)';
    }
  };

  const onDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (isPending) return;
    
    e.currentTarget.style.borderColor = 'var(--primary-light)';
    e.currentTarget.style.backgroundColor = 'rgba(255,255,255,0.9)';

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleUpload(e.dataTransfer.files[0]);
    }
  };

  return (
    <div 
      onClick={() => !isPending && fileInputRef.current?.click()}
      onDragOver={onDragOver}
      onDragLeave={onDragLeave}
      onDrop={onDrop}
      style={{
        padding: '24px',
        border: '2px dashed var(--primary-light)',
        borderRadius: 'var(--radius)',
        textAlign: 'center',
        cursor: isPending ? 'not-allowed' : 'pointer',
        backgroundColor: isPending ? 'var(--bg-main)' : 'rgba(255,255,255,0.9)',
        boxShadow: 'var(--shadow-md)',
        backdropFilter: 'blur(4px)',
        transition: 'all 0.2s ease',
        borderWidth: isPending ? '2px' : '2px'
      }}
      onMouseOver={(e) => !isPending && (e.currentTarget.style.borderColor = 'var(--accent-color)')}
      onMouseOut={(e) => !isPending && (e.currentTarget.style.borderColor = 'var(--primary-light)')}
    >
      <input 
        type="file" 
        ref={fileInputRef} 
        onChange={onFileChange} 
        style={{ display: 'none' }} 
        accept=".json,.geojson"
      />
      <div style={{ fontSize: '15px', fontWeight: '600', color: 'var(--primary-dark)', marginBottom: '4px' }}>
        {isPending ? '분석 중...' : 'GeoJSON 데이터 업로드'}
      </div>
      <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
        {isPending ? '잠시만 기다려주세요.' : '클릭하거나 파일을 드래그하세요.'}
      </div>
    </div>
  );
};

export default React.memo(FileUploader);
