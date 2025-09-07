products = [
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]},
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]},
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]},
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]},
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
    {"name": "LED Desk Lamp", "tags": ["energy-efficient", "adjustable", "stylish"]},
    {"name": "Running Shoes", "tags": ["lightweight", "durable", "comfortable"]},
    {"name": "Bluetooth Speaker", "tags": ["portable", "tech", "wireless"]},
    {"name": "Portable Charger", "tags": ["tech", "travel-friendly", "reliable"]},
    {"name": "Noise-Cancelling Headphones", "tags": ["tech", "quiet", "comfortable"]},
    {"name": "Compost Bin", "tags": ["eco-friendly", "kitchen", "odor-resistant"]},
    {"name": "Yoga Mat", "tags": ["fitness", "non-slip", "lightweight"]},
    {"name": "Reusable Grocery Bags", "tags": ["eco-friendly", "reusable", "foldable"]},
    {"name": "Ergonomic Office Chair", "tags": ["comfortable", "adjustable", "supportive"]},
    {"name": "Air Purifier", "tags": ["tech", "health", "quiet"]},
    {"name": "Gaming Mouse", "tags": ["tech", "responsive", "ergonomic"]},
    {"name": "Fitness Tracker", "tags": ["tech", "fitness", "wearable"]},
    {"name": "Standing Desk", "tags": ["adjustable", "ergonomic", "modern"]},
    {"name": "Mini Projector", "tags": ["portable", "tech", "entertainment"]},
    {"name": "Cast Iron Skillet", "tags": ["durable", "kitchen", "versatile"]},
    {"name": "Electric Kettle", "tags": ["kitchen", "tech", "energy-efficient"]},
    {"name": "Foldable Bike", "tags": ["eco-friendly", "portable", "fitness"]},
    {"name": "Smart Thermostat", "tags": ["tech", "energy-efficient", "smart-home"]},
    {"name": "Wool Blanket", "tags": ["warm", "natural", "cozy"]},
    {"name": "Digital Notebook", "tags": ["tech", "reusable", "stylish"]},
    {"name": "Bamboo Cutlery Set", "tags": ["eco-friendly", "reusable", "compact"]},
    {"name": "Compact Air Fryer", "tags": ["kitchen", "tech", "compact"]},
    {"name": "Solar Phone Charger", "tags": ["eco-friendly", "tech", "travel-friendly"]},
    {"name": "Insulated Lunch Box", "tags": ["kitchen", "portable", "durable"]},
    {"name": "Smart Light Bulbs", "tags": ["tech", "energy-efficient", "smart-home"]},
    {"name": "Laptop Stand", "tags": ["tech", "ergonomic", "portable"]},
    {"name": "Electric Bike", "tags": ["eco-friendly", "tech", "fitness"]},
    {"name": "Digital Pen", "tags": ["tech", "writing", "portable"]},
    {"name": "Silicone Food Storage Bags", "tags": ["kitchen", "reusable", "eco-friendly"]},
    {"name": "UV Sanitizer Box", "tags": ["tech", "health", "compact"]},
    {"name": "Virtual Reality Headset", "tags": ["tech", "entertainment", "immersive"]},
    {"name": "Hydroponic Indoor Garden", "tags": ["eco-friendly", "tech", "kitchen"]},
    {"name": "Wireless Charging Pad", "tags": ["tech", "convenient", "modern"]},
    {"name": "Magnetic Whiteboard", "tags": ["office", "reusable", "functional"]},
    {"name": "LED String Lights", "tags": ["decor", "energy-efficient", "stylish"]},
    {"name": "Adjustable Dumbbells", "tags": ["fitness", "compact", "durable"]},
    {"name": "Weighted Blanket", "tags": ["cozy", "health", "comfortable"]},
    {"name": "Camping Stove", "tags": ["portable", "outdoors", "reliable"]},
    {"name": "Touchless Trash Can", "tags": ["kitchen", "tech", "convenient"]},
    {"name": "Electric Toothbrush", "tags": ["tech", "health", "rechargeable"]},
    {"name": "Noise Machine", "tags": ["health", "sleep", "portable"]},
    {"name": "Pet Water Fountain", "tags": ["tech", "pet", "eco-friendly"]},
    {"name": "Motion Sensor Light", "tags": ["tech", "smart-home", "safety"]},
    {"name": "Smart Door Lock", "tags": ["tech", "security", "smart-home"]},
    {"name": "Cold Brew Coffee Maker", "tags": ["kitchen", "compact", "durable"]}
] 

for product in products[:3]:
    print(product)

customer_preferences = []
response = "Y"

while response != "N":
    print("Input a preference:")
    preference = input().strip().lower()
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").strip().upper()

customer_tags = set(customer_preferences)

converted_products = []
for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }
    converted_products.append(converted_product)

def count_matches(product_tags, customer_tags):
    return len(product_tags & customer_tags)

def recommend_products(products, customer_tags):
    recommendations = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        if match_count > 0:
            recommendations.append((product["name"], match_count))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

print("\nRecommended Products:")
results = recommend_products(converted_products, customer_tags)
for name, count in results:
    print(f"- {name} ({count} match(es))")

# 1. What core operations did you use (e.g., intersections, loops)? Why?
#The core operations that I chose to use for this project was intersections, 
#loops, and converted the list into a set. Even though the product list wasn't long, 
#converting it into a set helped with any duplicates to clean it up a bit and make it 
#easier to work with. When it comes to code like this where there's a larger list of 
#options, or in this case products, duplicates make things harder to read and identify 
#when someone like a consumer is looking for something specific. Sorting was also 
#helpful in this sense because it would give the products by relevance to the search. 

# 2. How might this code change if you had 1000+ products?
#If there were 1000+ products to sort through, a database would be a better idea for the larger 
#amount. Having it as is would be much too complicated and a database would make the work 
#exponentially easier when it comes to such a long list of products. A set would help with any 
#duplicates, as with such a long list duplicates would only make it that much harder to read. 
#Adding filters for a more streamlined experience also wouldn't be a bad idea. Working in a 
#field like data structures, it's important that organization and efficiency are given 
#priority. Not only for the customers, but for your own sake. 