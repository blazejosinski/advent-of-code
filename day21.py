import re

from helpers import solve_line_task 
from collections import Counter

def parse_food(line):
  # ingredients, allergens
  parts = line.split("(contains ")
  ingredients = parts[0].split()
  allergens = parts[1][:-1].split(", ")
  return ingredients, allergens


def assemle_food(data):
  all_allergens = set()
  all_ingredients = set()
  ingredients_counter = Counter()
  for ingredients, allergens in data:
    all_allergens.update(allergens)
    all_ingredients.update(ingredients)
    ingredients_counter.update(ingredients)

  safe_ingredients = all_ingredients.copy()
  aLlergens_to_ingredients = {}
  for allergen in all_allergens:
    ingredients_of_this_allergen = None
    for ingredients, allergens in data:
      if allergen in allergens:
        if ingredients_of_this_allergen is None:
          ingredients_of_this_allergen = set(ingredients)
        else:
          ingredients_of_this_allergen.intersection_update(ingredients)
    safe_ingredients.difference_update(ingredients_of_this_allergen)
    aLlergens_to_ingredients[allergen] = ingredients_of_this_allergen
  
  return sum([ingredients_counter[ingredient] for ingredient in safe_ingredients]), aLlergens_to_ingredients
  

def find_alergens(data):
  _, allergens_to_ingredients = assemle_food(data)
  res = []
  while allergens_to_ingredients:
    for allergen, ingredients in allergens_to_ingredients.items():
      if len(ingredients) == 1:
        ingredient = ingredients.pop()
        res.append((allergen, ingredient))
        allergens_to_ingredients.pop(allergen)
        for _, ingredients_to_update in allergens_to_ingredients.items():
          ingredients_to_update.difference_update([ingredient])
  return ",".join([x[1] for x in sorted(res)])


def main():
  print(solve_line_task("in", parse_food, lambda x: assemle_food(x)[0]))
  print(solve_line_task("in", parse_food, find_alergens))


if __name__ == "__main__":
    main()
