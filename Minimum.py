class Solution:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by their positions.
        robot.sort()
        factory.sort()

        # Initialize DP table, where dp[i][j] represents minimum distance
        # for fixing the first i robots with the first j factories.
        n = len(robot)
        m = len(factory)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: no robots, no distance.

        for j in range(1, m + 1):  # Loop over each factory
            pos, limit = factory[j - 1]  # Position and capacity of the j-th factory

            dp[0][j] = 0  # No robots to repair with j factories, cost is 0.

            for i in range(1, n + 1):  # Loop over each robot
                dp[i][j] = dp[i][j - 1]  # Option to skip current factory

                # Try repairing k robots with the j-th factory
                total_distance = 0
                for k in range(1, min(i, limit) + 1):
                    total_distance += abs(robot[i - k] - pos)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_distance)

        return dp[n][m]
