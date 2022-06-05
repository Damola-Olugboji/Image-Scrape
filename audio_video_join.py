from moviepy.editor import *
import os


def main():
    # UKULELE CLIP, OBTAINED BY CUTTING AND CROPPING
    # RAW FOOTAGE

    ukulele = VideoFileClip("clip 37.mp4", audio=False).crop(486, 180, 900, 570)

    w, h = ukulele.size

    # THE PIANO FOOTAGE IS DOWNSIZED, HAS A WHITE MARGIN, IS
    # IN THE BOTTOM RIGHT CORNER

    piano = (
        VideoFileClip("clip 36.mp4", audio=False)
        .resize((w / 3, h / 3))
        .margin(6, color=(255, 255, 255))  # one third of the total screen
        .margin(bottom=20, right=20, opacity=0)  # white margin
        .set_pos(("right", "bottom"))  # transparent
    )

    # FINAL ASSEMBLY
    final = CompositeVideoClip([ukulele, piano])
    final.subclip(0, 5).write_videofile("output.mp4", fps=24, codec="libx264")


if __name__ == "__main__":
    main()
