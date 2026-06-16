import { useMutation } from '@tanstack/react-query';
import type { SpatialAnalysisResult } from '../../types/spatial';

/**
 * GeoJSON 파일 업로드 및 분석 결과 수신을 위한 커스텀 훅
 */
export const useUploadGeoJson = () => {
  return useMutation<SpatialAnalysisResult, Error, File>({
    mutationFn: async (file: File) => {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('/api/v1/geojson/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('파일 업로드에 실패했습니다.');
      }

      return response.json();
    },
  });
};
