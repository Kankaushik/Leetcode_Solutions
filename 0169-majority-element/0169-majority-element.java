class Solution {
    public int majorityElement(int[] nums) {    
        HashMap<Integer,Integer> fre = new HashMap<>();
         int mejEl = nums.length/2;
         for(int num:nums){
            fre.put(num, fre.getOrDefault(num,0)+1);
            if(fre.get(num)>mejEl){
                return num;
            }
		}
        
        return- 1;
}}