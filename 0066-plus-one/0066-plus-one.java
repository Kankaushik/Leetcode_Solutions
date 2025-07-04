class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        int count = 0; 

        for (int i = n - 1; i >= 0; i--) {
            count++;
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            } else {
                digits[i] = 0;
            }
        }

        int[] result = new int[n + 1];
        result[0] = 1;
        return result;
    }
}
