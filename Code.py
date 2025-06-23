import cv2
import numpy as np
import os


def generate_frames(sentences, output_dir="frames", font_size=20, frame_size=(500, 100), fps=30):
    os.makedirs(output_dir, exist_ok=True)
    width, height = frame_size

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = font_size / 40
    font_thickness = 1
    padding = 20

    frames_per_action = fps * 5  # 5 seconds for writing or deleting
    pause_frames = fps * 10  # 10 seconds pause
    blank_image = np.ones((height, width, 3), dtype=np.uint8) * 255
    num_frames = 0

    for i, sentence in enumerate(sentences):
        total_chars = len(sentence)
        
        # Writing phase
        for frame_idx in range(frames_per_action):
            blank_image.fill(255)
            cv2.rectangle(blank_image, (padding, padding), (width - padding, height - padding), (0, 0, 0), 2)

            chars_to_show = int((frame_idx + 1) / frames_per_action * total_chars)
            text_to_show = sentence[:chars_to_show]

            cv2.putText(blank_image, text_to_show, (padding + 10, height // 2), font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

            frame_path = f"{output_dir}/frame_{num_frames:04d}.png"
            cv2.imwrite(frame_path, blank_image)
            num_frames += 1

        # Pause phase
        for _ in range(pause_frames):
            frame_path = f"{output_dir}/frame_{num_frames:04d}.png"
            cv2.imwrite(frame_path, blank_image)
            num_frames += 1

        # Deleting phase
        for frame_idx in range(frames_per_action):
            blank_image.fill(255)
            cv2.rectangle(blank_image, (padding, padding), (width - padding, height - padding), (0, 0, 0), 2)

            chars_to_show = total_chars - int((frame_idx + 1) / frames_per_action * total_chars)
            text_to_show = sentence[:chars_to_show]

            cv2.putText(blank_image, text_to_show, (padding + 10, height // 2), font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

            frame_path = f"{output_dir}/frame_{num_frames:04d}.png"
            cv2.imwrite(frame_path, blank_image)
            num_frames += 1

    return num_frames



def create_video_from_frames(output_video="output.mp4", output_dir="frames", fps=30):
    frame_files = sorted([os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".png")])
    if not frame_files:
        print("No frames found in the directory.")
        return

    first_frame = cv2.imread(frame_files[0])
    height, width, layers = first_frame.shape
    size = (width, height)

    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    for frame_file in frame_files:
        frame = cv2.imread(frame_file)
        out.write(frame)

    out.release()
    print(f"Video saved as {output_video}")

if __name__ == "__main__":
    sentences = [
        "Generate a Polycrystal RVE . . .",
        "Generate a Fiber Reinforced Concrete RVE . . .",
        "Generate a Multiscale Woven Fabric Model  . . .",
        "Generate a Ballistic Impact Model . . ."
    ]
    frame_output_dir = "frames"
    video_output_file = "writing_animation.mp4"

    fps = 30

    print("Generating frames...")
    num_frames = generate_frames(sentences, output_dir=frame_output_dir, fps=fps)

    print("Creating video...")
    create_video_from_frames(output_video=video_output_file, output_dir=frame_output_dir, fps=fps)

    print("Process completed!")

