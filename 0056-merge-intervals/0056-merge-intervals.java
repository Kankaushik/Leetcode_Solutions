class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new int[0][];
        }
        
       
        quickSort(intervals, 0, intervals.length - 1);
        
       
        List<int[]> merged = new ArrayList<>();
        
        
        int[] currentInterval = intervals[0];
        merged.add(currentInterval);
        
       
        for (int i = 1; i < intervals.length; i++) {
            int[] interval = intervals[i];
            
            
            if (interval[0] <= currentInterval[1]) {
                
                if (interval[1] > currentInterval[1]) {
                    currentInterval[1] = interval[1];
                }
            } else {
               
                currentInterval = interval;
                merged.add(currentInterval);
            }
        }
        
        
        return merged.toArray(new int[merged.size()][]);
    }
    
    
    private void quickSort(int[][] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }
    
   
    private int partition(int[][] arr, int low, int high) {
        int[] pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            
            if (arr[j][0] <= pivot[0]) {
                i++;
                swap(arr, i, j);
            }
        }
        
        
        swap(arr, i + 1, high);
        return i + 1;
    }
    
   
    private void swap(int[][] arr, int i, int j) {
        int[] temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}