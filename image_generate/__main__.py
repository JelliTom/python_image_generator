import click
from .image_generator import ImageGenerator

@click.command()
@click.argument('prompt')
@click.option('--prompt-file', '-pf', is_flag=True, help='Prompt is specific in a separate file instead')
@click.option('--force-new-img', "-f", is_flag=True, help='Force generation of a new image')
@click.option('--open-on-done', "-o", is_flag=True, help='Open image on download')
@click.option('--api-url', default='https://image.pollinations.ai/prompt/', help='API URL for image generation')
@click.option('--dir-out', default='images', help='Directory to save generated images')
@click.option('--timeout', default=60, help='Timeout for image generation in seconds')
def main(prompt, prompt_file, force_new_img, open_on_done, api_url, dir_out, timeout):
    image_generator = ImageGenerator(api_url, dir_out, timeout)
    image_path = image_generator.generate_image(prompt, prompt_file, force_new_img, open_on_done)
    if image_path:
        print(f"Image saved to: {image_path}")
    else:
        print("Image generation failed.")

if __name__ == "__main__":
    main()
