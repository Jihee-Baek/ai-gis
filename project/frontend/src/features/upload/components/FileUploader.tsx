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
    console.log('Starting upload for file:', file.name);
    mutate(file, {
      onSuccess: (data) => {
        console.log('Upload success, received data:', data);
        // 업로드 성공 시 로컬에서 파일 읽기 (지도시각화용)
        const reader = new FileReader();
        reader.onload = (e) => {
          try {
            console.log('FileReader loaded content');
            const geoJsonData = JSON.parse(e.target?.result as string);
            console.log('Parsed GeoJSON data:', geoJsonData);
            
            addLayer({
              id: String(data.id), // Ensure id is string if that's what store expects
              name: file.name,
              visible: true,
              data: geoJsonData,
              analysis: data
            });
            console.log('addLayer called successfully');
          } catch (err) {
            console.error('Error in FileReader onload:', err);
          }
        };
        reader.onerror = (err) => console.error('FileReader error:', err);
        reader.readAsText(file);
      },
      onError: (error) => {
        console.error('Upload mutation error:', error);
        alert(`업로드 실패: ${error.message}`);
      }
    });
  }, [mutate, addLayer]);

  const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      handleUpload(e.target.files[0]);
    }
  };

  return (
    <div 
      onClick={() => fileInputRef.current?.click()}
      style={{
        padding: '20px',
        border: '2px dashed #007bff',
        borderRadius: '8px',
        textAlign: 'center',
        cursor: 'pointer',
        backgroundColor: isPending ? '#f0f0f0' : 'transparent',
        transition: 'background-color 0.2s'
      }}
    >
      <input 
        type="file" 
        ref={fileInputRef} 
        onChange={onFileChange} 
        style={{ display: 'none' }} 
        accept=".json,.geojson"
      />
      <div style={{ fontSize: '16px', fontWeight: '500', color: '#007bff' }}>
        {isPending ? '파일 분석 중...' : 'GeoJSON 파일을 여기에 드래그하거나 클릭하여 업로드하세요.'}
      </div>
      <div style={{ fontSize: '12px', color: '#6c757d', marginTop: '8px' }}>
        최대 50MB까지 지원합니다.
      </div>
    </div>
  );
};

export default React.memo(FileUploader);
