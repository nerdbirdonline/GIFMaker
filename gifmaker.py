import imageio
import os

print("Enter Clip name and extension e.g; bball.mp4")
clip_name = input()

clip = os.path.abspath(clip_name)


def gifmaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame{frames}')
    print('Done!')
    writer.close()


gifmaker(clip, '.gif')
