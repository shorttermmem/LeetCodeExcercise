#https://leetcode.com/problems/design-a-food-rating-system/description/
# Input
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]

from typing import List
from collections import defaultdict
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine_map = {}
        self.food_rating_map = {}
        self.cuisine_ratings_map = defaultdict(list)

        for food, rating, cuisine in zip(foods, ratings, cuisines):
            self.food_cuisine_map[food] = cuisine
            self.food_rating_map[food] = rating
            heapq.heappush(self.cuisine_ratings_map[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating_map[food] = newRating 
        cuisine = self.food_cuisine_map[food]
        heapq.heappush(self.cuisine_ratings_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        if not self.cuisine_ratings_map[cuisine]:
            return None

        while self.cuisine_ratings_map[cuisine]:
            rating, food = self.cuisine_ratings_map[cuisine][0]
            
            if self.food_rating_map[food] == -rating:
                return food
            
            heapq.heappop(self.cuisine_ratings_map[cuisine])   

        return None



class FoodRatings_opt:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self._cuisines = cuisines
        self._ratings = ratings
        self._heaps = collections.defaultdict(list)
        for i in range(len(foods)):
            heappush(self._heaps[cuisines[i]], (-ratings[i], foods[i], i))
        self._food_idxs = {f: i for i, f in enumerate(foods)}

    def changeRating(self, food: str, newRating: int) -> None:
        idx = self._food_idxs[food]
        self._ratings[idx] = newRating
        cuisine = self._cuisines[idx]
        heappush(self._heaps[cuisine], (-newRating, food, idx))

    def highestRated(self, cuisine: str) -> str:
        neg_rating, food, idx = self._heaps[cuisine][0]
        while -neg_rating != self._ratings[idx]:
            heappop(self._heaps[cuisine])
            neg_rating, food, idx = self._heaps[cuisine][0]

        return food
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)