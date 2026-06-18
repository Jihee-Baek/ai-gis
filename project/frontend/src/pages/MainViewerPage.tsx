import React from 'react';
import MapContainer from '../features/map/components/MapContainer';
import FileUploader from '../features/upload/components/FileUploader';
import LayerSidebar from '../features/sidebar/components/LayerSidebar';
import PropertyInspector from '../features/inspector/components/PropertyInspector';
import LoadingOverlay from '../components/common/LoadingOverlay';
import { useUploadGeoJson } from '../hooks/mutations/useUploadGeoJson';

/**
 * 애플리케이션의 메인 뷰어 레이아웃을 구성하고 상태를 조율하는 페이지 컴포넌트
 */
const MainViewerPage: React.FC = () => {
  const { isPending: isUploading } = useUploadGeoJson();

  return (
    <div style={{
      display: 'flex',
      width: '100vw',
      height: '100vh',
      overflow: 'hidden',
      fontFamily: 'sans-serif'
    }}>
      <LayerSidebar />
      
      <main style={{ flex: 1, position: 'relative' }}>
        <div style={{
          position: 'absolute',
          top: '20px',
          left: '20px',
          zIndex: 1000,
          width: '400px'
        }}>
          <FileUploader />
        </div>

        <MapContainer />
        <PropertyInspector />
      </main>

      <LoadingOverlay isVisible={isUploading} message="GeoJSON 파일을 분석 중입니다..." />
    </div>
  );
};

export default MainViewerPage;
