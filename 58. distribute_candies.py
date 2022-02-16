class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        candies_to_eat = len(candyType)/2

        unique_candy= {}

        for i in range(0, len(candyType)):

            if candyType[i] not in unique_candy:
                unique_candy[candyType[i]] = 1

        return int(min(candies_to_eat, len(unique_candy)))
