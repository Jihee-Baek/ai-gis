import { create } from 'zustand';
import type { LayerInfo } from '../types/spatial';

interface MapState {
  zoom: number;
  center: [number, number];
  layers: LayerInfo[];
}

interface MapActions {
  setZoom: (zoom: number) => void;
  setCenter: (center: [number, number]) => void;
  addLayer: (layer: LayerInfo) => void;
  removeLayer: (id: string) => void;
  toggleLayerVisibility: (id: string) => void;
}

/**
 * 지도 관련 전역 상태를 관리하는 Zustand 스토어
 */
export const useMapStore = create<MapState & MapActions>((set) => ({
  zoom: 13,
  center: [37.5665, 126.9780], // 서울 중심좌표
  layers: [],

  setZoom: (zoom) => set({ zoom }),
  setCenter: (center) => set({ center }),
  
  addLayer: (layer) => set((state) => {
    const id = layer.id || `layer-${Date.now()}`;
    // 이미 동일한 ID가 있다면 추가하지 않거나 덮어쓰지 않음 (필요시 로직 조정 가능)
    if (state.layers.some((l) => l.id === id)) {
      return state;
    }
    return {
      layers: [...state.layers, { ...layer, id }]
    };
  }),

  removeLayer: (id) => set((state) => ({
    layers: state.layers.filter((l) => l.id !== id)
  })),

  toggleLayerVisibility: (id) => set((state) => ({
    layers: state.layers.map((l) => 
      l.id === id ? { ...l, visible: !l.visible } : l
    )
  })),
}));
