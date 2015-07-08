class Solution {
    public int solution(int[] A) {
        int length = A.length;
        int[] maxSliceTillHere = new int[length];
        int[] maxSliceFromHere = new int[length];
        int maxSlice = 0;
        int doubleMax = 0;
        
        for (int i = 1; i < length-1; ++i) {
            maxSlice = Math.max(0, maxSlice + A[i]);
            maxSliceTillHere[i] = maxSlice;
        }
        
        maxSlice = 0;
        for(int i = length - 2; i > 0; --i) {
            maxSlice = Math.max(0, maxSlice + A[i]);
            maxSliceFromHere[i] = maxSlice;
        }
        
        for (int i = 0; i < length - 2; ++i) {
            doubleMax = Math.max(doubleMax, 
            maxSliceTillHere[i] + maxSliceFromHere[i+2]);
        }
        
        return doubleMax;
    }
}
