import os
from PIL import Image

def compress_gif(input_path, output_path, max_width=480):
    try:
        with Image.open(input_path) as im:
            # Calculate new size
            width, height = im.size
            if width > max_width:
                new_width = max_width
                new_height = int(height * (max_width / width))
            else:
                new_width, new_height = width, height
                
            print(f"Original size: {width}x{height}, New size: {new_width}x{new_height}")

            frames = []
            try:
                while True:
                    # Resize frame
                    frame = im.copy()
                    frame = frame.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    # Reduce colors to 128
                    frame = frame.quantize(colors=128)
                    frames.append(frame)
                    im.seek(im.tell() + 1)
            except EOFError:
                pass

            # Save optimized GIF
            frames[0].save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                optimize=True,
                duration=im.info.get('duration', 100),
                loop=0
            )
            
            original_size = os.path.getsize(input_path) / (1024 * 1024)
            new_size = os.path.getsize(output_path) / (1024 * 1024)
            print(f"Compressed GIF saved to {output_path}")
            print(f"Original size: {original_size:.2f} MB")
            print(f"New size: {new_size:.2f} MB")
            
    except Exception as e:
        print(f"Error compressing GIF: {e}")

if __name__ == "__main__":
    compress_gif("demo.gif", "demo_optimized_v2.gif")
