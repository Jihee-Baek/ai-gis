import { create } from 'zustand';
import type { GeoJSONFeature } from '../types/spatial';

interface FeatureState {
  selectedFeature: GeoJSONFeature | null;
  hoveredFeature: GeoJSONFeature | null;
}

interface FeatureActions {
  setSelectedFeature: (feature: GeoJSONFeature | null) => void;
  setHoveredFeature: (feature: GeoJSONFeature | null) => void;
  clearSelection: () => void;
}

/**
 * 선택된 지리 객체와 해당 속성을 관리하는 Zustand 스토어
 */
export const useFeatureStore = create<FeatureState & FeatureActions>((set) => ({
  selectedFeature: null,
  hoveredFeature: null,

  setSelectedFeature: (feature) => set({ selectedFeature: feature }),
  setHoveredFeature: (feature) => set({ hoveredFeature: feature }),
  clearSelection: () => set({ selectedFeature: null, hoveredFeature: null }),
}));
