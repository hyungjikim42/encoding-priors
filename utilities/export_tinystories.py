from datasets import load_dataset

seed = 42
num_samples = 100

ds = load_dataset("roneneldan/TinyStories")

subset = ds['train'].shuffle(seed=seed).select(range(num_samples))

filename = f"tiny_stories_subset_{num_samples}.txt"

with open(filename, 'w') as file:
    for sample in subset:
        file.write(sample['text'] + '\n\n')

print(f"Exported {num_samples} samples to {filename}")