import json
import pandas as pd

def convert_pokedex_to_excel():
    # Read data from pokedex.json file
    with open('pokedex.json', 'r') as file:
        pokedex_data = json.load(file)

    # Create lists to store the structured data
    ids = []
    nums = []
    names = []
    imgs = []
    types = []
    heights = []
    weights = []
    candies = []
    candy_counts = []
    eggs = []
    spawn_chances = []
    avg_spawns = []
    spawn_times = []
    weaknesses = []
    next_evolutions = []
    prev_evolutions = []

    # Extract data attributes from pokedex_data and populate the lists
    for entry in pokedex_data['pokemon']:
        ids.append(entry['id'])
        nums.append(entry['num'])
        names.append(entry['name'])
        imgs.append(entry['img'])
        types.append(', '.join(entry['type']))
        heights.append(entry['height'])
        weights.append(entry['weight'])
        candies.append(entry.get('candy', ''))
        candy_counts.append(entry.get('candy_count', ''))
        eggs.append(entry.get('egg', ''))
        spawn_chances.append(entry.get('spawn_chance', ''))
        avg_spawns.append(entry.get('avg_spawns', ''))
        spawn_times.append(entry.get('spawn_time', ''))
        weaknesses.append(', '.join(entry.get('weaknesses', [])))
        next_evolution_list = entry.get('next_evolution', [])
        next_evolutions.append(', '.join([f"{evolution['num']} - {evolution['name']}" for evolution in next_evolution_list]))
        prev_evolution_list = entry.get('prev_evolution', [])
        prev_evolutions.append(', '.join([f"{evolution['num']} - {evolution['name']}" for evolution in prev_evolution_list]))

    # Create a DataFrame using the structured data
    df = pd.DataFrame({
        'ID': ids,
        'Num': nums,
        'Name': names,
        'Image': imgs,
        'Type': types,
        'Height': heights,
        'Weight': weights,
        'Candy': candies,
        'Candy Count': candy_counts,
        'Egg': eggs,
        'Spawn Chance': spawn_chances,
        'Avg Spawns': avg_spawns,
        'Spawn Time': spawn_times,
        'Weaknesses': weaknesses,
        'Next Evolution': next_evolutions,
        'Previous Evolution': prev_evolutions
    })

    # Export DataFrame to Excel file
    df.to_excel('pokedex.xlsx', index=False)

    print("Json File Converted To Excel Successfully!")


# Call the function to convert pokedex.json to Excel format
convert_pokedex_to_excel()
