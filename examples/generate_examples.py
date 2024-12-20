 #examples/generate_examples.py
import os
import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from islamic_fractals import IslamicFractalGenerator, save_figure

def generate_examples():
    generator = IslamicFractalGenerator()
    
    # Generate fractals with different depths
    for depth in [3, 4, 5]:
        print(f"Generating fractal with depth {depth}...")
        fig, _ = generator.generate_fractal(depth)
        save_figure(fig, f'islamic_fractal_depth_{depth}.png')
        print(f"Saved fractal with depth {depth}")

if __name__ == "__main__":
    generate_examples()