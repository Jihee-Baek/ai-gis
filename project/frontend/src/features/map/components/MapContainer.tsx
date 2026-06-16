import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { useMapStore } from '../../../stores/mapStore';
import { useFeatureStore } from '../../../stores/featureStore';

/**
 * Leaflet 기반의 핵심 지도 컴포넌트
 */
const MapContainer: React.FC = () => {
  const mapRef = useRef<HTMLDivElement>(null);
  const leafletMap = useRef<L.Map | null>(null);
  const layersGroup = useRef<L.FeatureGroup>(L.featureGroup());

  const { zoom, center, layers, setZoom, setCenter } = useMapStore();
  const { setSelectedFeature } = useFeatureStore();

  // 지도 초기화
  useEffect(() => {
    if (!mapRef.current || leafletMap.current) return;

    leafletMap.current = L.map(mapRef.current).setView(center, zoom);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(leafletMap.current);

    layersGroup.current.addTo(leafletMap.current);

    leafletMap.current.on('zoomend', () => {
      setZoom(leafletMap.current!.getZoom());
    });

    leafletMap.current.on('moveend', () => {
      const c = leafletMap.current!.getCenter();
      setCenter([c.lat, c.lng]);
    });

    return () => {
      leafletMap.current?.remove();
      leafletMap.current = null;
    };
  }, []);

  // 레이어 렌더링
  useEffect(() => {
    if (!leafletMap.current) return;

    layersGroup.current.clearLayers();

    layers.forEach((layer) => {
      if (!layer.visible) return;

      const geoJsonLayer = L.geoJSON(layer.data, {
        onEachFeature: (feature, leafletLayer) => {
          leafletLayer.on('click', (e) => {
            L.DomEvent.stopPropagation(e);
            setSelectedFeature(feature as any);
          });
        },
        style: {
          color: '#007bff',
          weight: 2,
          fillOpacity: 0.3
        }
      });

      layersGroup.current.addLayer(geoJsonLayer);
      
      // 새 레이어 추가 시 영역 자동 조정
      if (layers.length > 0 && layer === layers[layers.length - 1]) {
        leafletMap.current?.fitBounds(layersGroup.current.getBounds());
      }
    });
  }, [layers, setSelectedFeature]);

  return (
    <div 
      ref={mapRef} 
      style={{ width: '100%', height: '100%', position: 'relative', zIndex: 1 }}
    />
  );
};

export default React.memo(MapContainer);
