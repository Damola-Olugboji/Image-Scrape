import moviepy.video.io.ImageSequenceClip
import os
import glob
import random
import cv2


def main():

    cwd = "/Users/damolaolugboji/Desktop/code/Image Scrape/Frames"
    image_list = []
    for iterator in range(50):
        for i in range(4):
            random_folder = random.choice(list(os.listdir(cwd)))
            while (random_folder == ".DS_Store") or (random_folder == "erotic"):
                random_folder = random.choice(list(os.listdir(cwd)))

            random_file = random.choice(
                list(os.listdir(os.path.join(cwd, random_folder)))
            )
            print(os.path.join(cwd, random_folder, random_file))
            try:
                image = cv2.imread(os.path.join(cwd, random_folder, random_file))
                resized_image = cv2.resize(image, (1080, 1920))
                RGB_img = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
                image_list.append(RGB_img)
            except:
                continue

        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_list, fps=0.5)
        clip.write_videofile("clips/output{}.mp4".format(iterator))
        print("complete")
        image_list.clear()

    rename()


def rename():
    cwd = "/Users/damolaolugboji/Desktop/code/Image Scrape/clips/final"
    for counter, dir in enumerate(os.listdir(cwd)):
        new_name = os.path.join(cwd, "clip {}.mp4".format(counter))
        os.rename(os.path.join(cwd, dir), new_name)

    return


def test():
    dict = {"yes": 0, "no": 1, "asd": 8, "asdaisod": 10}
    temp = random.choice(list(dict.keys()))
    cwd = "/Users/damolaolugboji/Desktop/code/Image Scrape/Frames"
    path = os.path.join(cwd, "erotic")
    files = os.listdir(path)
    print(len(files))


if __name__ == "__main__":
    main()
