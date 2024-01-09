# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
from app import generate
from src.utils import paths, restore_dirs, make_archive
from src.client import download_zip
import shutil
import os


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""

    def predict(
        self,
        session_id: str = Input(description="Session id: "),
    ) -> Path:
        """Run a single prediction on the model"""

        restore_dirs()

        # shutil.copy(input_video, paths.input_video)
        # shutil.copy(audio, paths.audio)

        download_zip(session_id)
        shutil.copy(paths.inputs_folder / "audio.wav", paths.audio)
        generate()
        return Path("".join([str(paths.captioned_video).split(".")[0], "_with_audio.mp4"]))
