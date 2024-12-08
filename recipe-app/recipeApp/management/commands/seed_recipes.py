from django.core.management.base import BaseCommand
from recipeApp.models import Recipe
from random import choice

class Command(BaseCommand):
    help = 'Seeds the Recipe table with sample data'

    def handle(self, *args, **kwargs):
        recipes_data = [
            {
                'name': "Delicious Pasta",
                'short_desc': "Find out how to make this mouthwatering pasta dish.",
                'ingred_html': "<ul><li>200g dried pasta (spaghetti, penne, or your choice)</li><li>1 tablespoon salt (for boiling water)</li><li>2 tablespoons olive oil</li><li>2 cloves garlic, minced</li><li>400g canned tomatoes (crushed or whole)</li><li>1 teaspoon dried basil (or a handful of fresh basil)</li><li>Salt and pepper to taste</li><li>Grated Parmesan cheese (for serving)</li></ul>",
                'desc_html': '<div class="section video-section"><h3>How to Make Pasta (Video)</h3><iframe width="560" height="315" src="https://www.youtube.com/embed/hJxnH7OKLps?si=t-Ya4mvQv0ER6qST" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>',
                'additional_html' : '<div class="section video-section"><h3>How to Make Pasta (Video)</h3><iframe width="560" height="315" src="https://www.youtube.com/embed/hJxnH7OKLps?si=t-Ya4mvQv0ER6qST" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>',
                'image' : "/static/images/pasta.jpeg",
            },
            {
                'name': "Rich Chocolate Cake",
                'short_desc': "What's the secret to a perfect chocolate cake?",
                'ingred_html': "<ul><li>1 ¾ cups all-purpose flour</li><li>2 cups granulated sugar</li><li>¾ cup unsweetened cocoa powder</li><li>1 ½ teaspoons baking powder</li><li>1 ½ teaspoons baking soda</li><li>1 teaspoon salt</li><li>2 large eggs</li><li>1 cup whole milk</li><li>½ cup vegetable oil</li><li>2 teaspoons vanilla extract</li><li>1 cup boiling water</li><li>1 cup chocolate chips (optional, for extra richness)</li></ul>",
                'desc_html' : '<div class="step"><h4>Step 1: Preheat the Oven</h4><p>Preheat your oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.</p></div><div class="step"><h4>Step 2: Mix Dry Ingredients</h4><p>In a large mixing bowl, combine the flour, sugar, cocoa powder, baking powder, baking soda, and salt. Mix until well combined.</p></div><div class="step"><h4>Step 3: Add Wet Ingredients</h4><p>Add the eggs, milk, vegetable oil, and vanilla extract to the dry ingredients. Beat on medium speed for 2 minutes. Stir in the boiling water until the batter is smooth. If using, fold in the chocolate chips.</p></div><div class="step"><h4>Step 4: Bake</h4><p>Pour the batter evenly into the prepared cake pans. Bake for 30-35 minutes or until a toothpick inserted in the center comes out clean. Let the cakes cool in the pans for 10 minutes before transferring to wire racks to cool completely.</p></div><div class="step"><h4>Step 5: Frost and Serve</h4><p>Once the cakes are completely cool, frost with your favorite chocolate frosting and serve. Enjoy your rich chocolate cake!</p></div>',
                'additional_html' : '<div class="section video-section"><h3>How to Make Rich Chocolate Cake (Video)</h3><iframe width="560" height="315" src="https://www.youtube.com/embed/0cV8C8ybZUY?si=YcUlzrPnM0BAFuAG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>',
                'image' : "/static/images/cake.jpeg"
            },
            {
                'name': "Refreshing Smoothies",
                'short_desc': "Blend up a fresh and delicious smoothie in minutes.",
                'ingred_html': "<ul><li>1 banana</li><li>1 cup spinach or kale</li><li>1 cup frozen berries (strawberries, blueberries, or mixed)</li><li>1 cup yogurt (plain or flavored)</li><li>1 cup almond milk or any milk of your choice</li><li>1 tablespoon honey or maple syrup (optional)</li><li>Ice cubes (optional)</li></ul>",
                'desc_html': '<div class="step"><h4>Step 1: Prepare Ingredients</h4><p>Gather all the ingredients. Peel the banana and wash the spinach or kale thoroughly.</p></div><div class="step"><h4>Step 2: Blend</h4><p>In a blender, combine the banana, spinach or kale, frozen berries, yogurt, and almond milk. Blend until smooth.</p></div><div class="step"><h4>Step 3: Taste and Sweeten</h4><p>Taste the smoothie. If you\'d like it sweeter, add honey or maple syrup and blend again.</p></div><div class="step"><h4>Step 4: Adjust Consistency</h4><p>If the smoothie is too thick, add more almond milk. If too thin, add a few ice cubes and blend until desired consistency is reached.</p></div><div class="step"><h4>Step 5: Serve</h4><p>Pour the smoothie into glasses and enjoy immediately!</p></div>',
                'additional_html': '<div class="section video-section"><h3>How to Make Refreshing Smoothies (Video)</h3><iframe width="560" height="315" src="https://www.youtube.com/embed/YuDhbLQtt2k?si=3b-ZwAh_uicbkJeg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>',
                'image' : "/static/images/smoothie.jpeg",
            },
            {
                'name': "Vegan Tacos",
                'short_desc': "Discover the flavors of these incredible vegan tacos.",
                'ingred_html': "<ul><li>8 small corn tortillas</li><li>1 can black beans, drained and rinsed</li><li>1 cup corn (fresh, frozen, or canned)</li><li>1 red bell pepper, diced</li><li>1 avocado, diced</li><li>1 small red onion, diced</li><li>1 teaspoon cumin</li><li>1 teaspoon chili powder</li><li>Salt and pepper to taste</li><li>Fresh cilantro, for garnish</li><li>Lime wedges, for serving</li></ul>",
                'additional_html' : '<div class="section video-section"><h3>How to Make Vegan Tacos (Video)</h3><iframe width="560" height="315" src="https://www.youtube.com/embed/7_UtpAf2Mag?si=IpQCJP68pS82sD-c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>',
                'desc_html': '<div class="step"><h4>Step 1: Prepare Ingredients</h4><p>Gather all the ingredients. Peel the banana and wash the spinach or kale thoroughly.</p></div><div class="step"><h4>Step 2: Blend</h4><p>In a blender, combine the banana, spinach or kale, frozen berries, yogurt, and almond milk. Blend until smooth.</p></div><div class="step"><h4>Step 3: Taste and Sweeten</h4><p>Taste the smoothie. If you\'d like it sweeter, add honey or maple syrup and blend again.</p></div><div class="step"><h4>Step 4: Adjust Consistency</h4><p>If the smoothie is too thick, add more almond milk. If too thin, add a few ice cubes and blend until desired consistency is reached.</p></div><div class="step"><h4>Step 5: Serve</h4><p>Pour the smoothie into glasses and enjoy immediately!</p></div>',
                'image' : "/static/images/tacos.jpeg",
            },
            {
                'name': "Spicy Chicken Curry",
                'short_desc': "Learn how to make an authentic chicken curry.",
                'ingred_html': "<ul><li>500g chicken, cut into pieces</li><li>2 tablespoons vegetable oil</li><li>1 large onion, finely chopped</li><li>3 cloves garlic, minced</li><li>1 inch ginger, grated</li><li>2 tomatoes, pureed</li><li>1 tablespoon curry powder</li><li>1 teaspoon turmeric powder</li><li>1 teaspoon red chili powder</li><li>1 teaspoon garam masala</li><li>Salt to taste</li><li>Fresh cilantro, for garnish</li><li>1 cup coconut milk</li></ul>",
                'desc_html': '<div class="step"><h4>Step 1: Heat Oil and Sauté Onions</h4><p>In a large pot, heat the vegetable oil over medium heat. Add the chopped onions and sauté until they are golden brown.</p></div><div class="step"><h4>Step 2: Add Garlic and Ginger</h4><p>Add the minced garlic and grated ginger to the pot, and sauté for another 2 minutes until fragrant.</p></div><div class="step"><h4>Step 3: Cook Chicken</h4><p>Add the chicken pieces to the pot, cooking until they are browned on all sides.</p></div><div class="step"><h4>Step 4: Add Spices and Tomato Puree</h4><p>Stir in the curry powder, turmeric powder, red chili powder, and salt. Then add the tomato puree and mix well.</p></div><div class="step"><h4>Step 5: Simmer with Coconut Milk</h4><p>Pour in the coconut milk and bring to a boil. Reduce the heat, cover, and let it simmer for about 20 minutes, or until the chicken is cooked through.</p></div><div class="step"><h4>Step 6: Finish with Garam Masala</h4><p>Stir in the garam masala and let it cook for an additional 5 minutes. Garnish with fresh cilantro before serving.</p></div>',
                'additional_html' : '<div class="section video-section"><h3>How to Make Spicy Chicken Curry (Video)</h3><iframe width="560" height="315" src="https://www.youtube.com/embed/DNOo53bfi_E?si=LVjHW1lXoeqG9yhl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>',
                'image' : "/static/images/chicken-curry.jpeg",
            },
        ]
        
        for recipe in recipes_data:
            Recipe.objects.create(
                name=recipe['name'],
                short_desc=recipe['short_desc'],
                ingred_html=recipe['ingred_html'],
                desc_html=recipe['desc_html'],
                additional_html=recipe['additional_html'],
                image=recipe['image']
            )

        self.stdout.write(self.style.SUCCESS('Successfully added recipes!'))
