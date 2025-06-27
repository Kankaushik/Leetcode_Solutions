class Solution {
    public boolean isHappy(int n) {
        if (n < 0) return false;

        HashMap<Integer, Boolean> seen = new HashMap<>();

        while (n != 1) {
            if (seen.containsKey(n)) {
                return false; // loop detected
            }

            seen.put(n, true);
            n = getSumOfSquares(n);
        }

        return true;
    }

    private int getSumOfSquares(int n) {
        int sum = 0;
        while (n != 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}