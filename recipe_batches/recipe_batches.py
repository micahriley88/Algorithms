#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  smallest = 9000
  for item in recipe.keys():
    if item not in ingredients.keys():                       # If a recipe item is not in ingredients, you automatically cant make the recipe!
      return 0
    else:
      print(recipe[item])
      print(ingredients[item])
      compare = ingredients[item] // recipe[item]
      if smallest > compare:
        smallest = compare
  return smallest


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))