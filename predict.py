# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
from app import generate
from src.utils import paths, restore_dirs, make_archive
import shutil
import os


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""

    def predict(
        self,
        input_video: Path = Input(description="Input video"),
        audio: Path = Input(
            description="Input audio for lipsync"),
    ) -> Path:
        """Run a single prediction on the model"""

        restore_dirs()

        shutil.copy(input_video, paths.input_video)
        shutil.copy(audio, paths.audio)

        generate()
        return Path("".join([str(paths.captioned_video).split(".")[0], "_with_audio.mp4"]))
