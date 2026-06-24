/**
 * @param {number} n
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var zigZagArrays = function(n, l, r) {
    const MOD = 1000000007n;
    const m = r - l + 1;

    if (n === 1) return m % Number(MOD);
    if (n === 2) return Number((BigInt(m) * BigInt(m - 1)) % MOD);

    let up = Array(m).fill(0n);
    let down = Array(m).fill(0n);

    // length = 2
    for (let v = 0; v < m; v++) {
        up[v] = BigInt(v);              // smaller values
        down[v] = BigInt(m - 1 - v);   // larger values
    }

    for (let len = 3; len <= n; len++) {
        let prefixDown = Array(m).fill(0n);
        let suffixUp = Array(m).fill(0n);

        prefixDown[0] = down[0];
        for (let i = 1; i < m; i++) {
            prefixDown[i] = (prefixDown[i - 1] + down[i]) % MOD;
        }

        suffixUp[m - 1] = up[m - 1];
        for (let i = m - 2; i >= 0; i--) {
            suffixUp[i] = (suffixUp[i + 1] + up[i]) % MOD;
        }

        let newUp = Array(m).fill(0n);
        let newDown = Array(m).fill(0n);

        for (let x = 0; x < m; x++) {
            newUp[x] = x > 0 ? prefixDown[x - 1] : 0n;
            newDown[x] = x < m - 1 ? suffixUp[x + 1] : 0n;
        }

        up = newUp;
        down = newDown;
    }

    let ans = 0n;

    for (let i = 0; i < m; i++) {
        ans = (ans + up[i] + down[i]) % MOD;
    }

    return Number(ans);
};