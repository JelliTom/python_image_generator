# Python Image Generator using API

**ALL IMAGES IN THIS REPOSITORY ARE GENERATED USING AI**

This repository provides a Command Line Tool using `click` to allow basic image generation directly from the command line. Images will be saved locally as a png in a specified directory, defaults to `images`, along with the prompt used to generate each image in a separate text file. 

To generate a new image use the following command:
```
python -m image_generate "<your prompt>" <options>
```

You can specify the prompt as a string in your input command, or you can specify a file path to a file containing your full text prompt. To make use of this options ensure you add the `pf` option to your command line to specify you are passing a prompt file, instead of a string. An example is provided as part of this repository in the `example-prompt.txt` file. See command below:

```
python -m image_generate example-prompt.txt -pf
```

Some additional command line options are also available.
- `--force-new-img`, `-f`: Tells the script to generate a new image, rather than returning one that was previously generated for that prompt
- `--prompt-file`, `-pf`: Tells the script that you are passing in a file path to the file containing your prompt, rather than passing the prompt in as a command line string
- `--open-on-done`, `-o` : Tells the script to open the image in a new window once the image has been generated
- `--api-url`: Tells the application which URL to make requests to when generating your prompts, defaults to "https://image.pollinations.ai/prompt/"
- `--dir-out`: Tells the application which directory to save your generated images to, defaults to `images`
- `--timeout`: Tells the application how long to keep retrying your request for before timing out, defaults to 60 seconds


The most useful prompt is expected to be:
```
python -m image_generate "<your prompt>" -f -o
```
As this ensures a brand new image is generated and it will be opened once the generation is complete. We suggested you leave the other inputs as defaults.


### Corner Cases
Note, images are usually saved with the prompt included in the name, for example `mouse-wearing-a-suite.png` and will also be appended with the uuid string if `-f` is specified in your command, `mouse-wearing-a-suite-mouse-wearing-a-suite-f47ac10b-58cc-4372-a567-0e02b2c3d479.png`. However, if this string is too long to be a filename, the file will instead be named using the date and time of the generation, for example `2025-08-04-T14-45-06.png`.
