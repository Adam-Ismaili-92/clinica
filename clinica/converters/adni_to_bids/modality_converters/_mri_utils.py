from pathlib import Path

import pandas as pd

__all__ = ["load_all_images_metadata"]


def load_all_images_metadata(csv_dir: Path) -> pd.DataFrame:
    """All Images and MRIQC csv files are loaded. Columns from MRIQC file are merged into All Images.

    Parameters
    ----------
    csv_dir : PathLike
        Path to the clinical data directory.

    Returns: DataFrame containing main clinical data for PET images.
    """
    from clinica.converters._utils import load_clinical_csv

    all_images = load_clinical_csv(csv_dir, "All_Images")
    mriqc = load_clinical_csv(csv_dir, "MRIQC")

    all_images = all_images.merge(
        mriqc[["image_id", "LONISeries", "MagneticFieldStrength"]],
        on="image_id",
        how="left",
    )

    all_images = all_images.rename(columns={"LONISeries": "series_id"})

    return all_images
