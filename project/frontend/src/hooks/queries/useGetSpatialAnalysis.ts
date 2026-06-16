import { useQuery } from '@tanstack/react-query';
import type { SpatialAnalysisResult } from '../../types/spatial';

/**
 * 특정 파일의 공간 분석 상세 정보를 조회하는 커스텀 훅
 */
export const useGetSpatialAnalysis = (fileId: string | null) => {
  return useQuery<SpatialAnalysisResult, Error>({
    queryKey: ['spatialAnalysis', fileId],
    queryFn: async () => {
      if (!fileId) throw new Error('파일 ID가 필요합니다.');
      
      const response = await fetch(`/api/v1/geojson/${fileId}`);
      
      if (!response.ok) {
        throw new Error('분석 데이터를 불러오는데 실패했습니다.');
      }

      return response.json();
    },
    enabled: !!fileId,
  });
};
