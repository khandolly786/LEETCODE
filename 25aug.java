class Solution {
public:
   int maximizeMedian(vector<int>& a, int k) {
        sort(a.begin(), a.end());
        int n = (int)a.size();
        long long K = k; // use 64-bit for safety

        if (n % 2 == 1) {
            // Odd n: raise the median and then the prefix [median..end] level by level
            int start = n / 2;
            long long L = a[start];
            long long g = 1;                 // size of the leveled group
            for (int i = start + 1; i < n; ++i) {
                long long gap = a[i] - L;    // how much level to reach next value
                long long need = g * gap;    // cost to lift the whole group to a[i]
                if (K < need) return (int)(L + K / g);
                K -= need;
                L = a[i];
                ++g;
            }
            return (int)(L + K / g);
        } else {
            // Even n: we care about the average of the two middle positions.
            // Consider S = a[n/2 - 1 .. n-1]. We "pour" K increments onto its min-heap effect.
            int start = n / 2 - 1;
            // Step 1: raise a[start] up to a[start+1] if possible (only the smallest moves first)
            long long d = (long long)a[start + 1] - a[start];
            if (K < d) {
                return (int)((a[start] + K + a[start + 1]) / 2);
            }
            K -= d;
            long long L = a[start + 1];  // current common level of the smallest group
            long long g = 2;             // we now have two equal smallest elements
            int i = start + 2;

            // Include any ties already at level L
            while (i < n && a[i] <= L) { ++g; ++i; }

            // Level the growing prefix to each next value
            while (i < n) {
                long long gap = (long long)a[i] - L;
                if (gap <= 0) { ++g; ++i; continue; }
                long long need = g * gap;
                if (K < need) return (int)(L + K / g);
                K -= need;
                L = a[i];
                ++g; ++i;
            }
            // All elements in S are equal to L; further increases raise all together.
            return (int)(L + K / g);
        }
    }
};
