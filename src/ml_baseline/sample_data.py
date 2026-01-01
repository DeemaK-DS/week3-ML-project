from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .config import Paths
from .io import best_effort_ext, write_tabular


def make_sample_feature_table(*, root: Path | None = None, n_users: int = 1000, seed: int = 42) -> Path:
    """Write a small, deterministic feature table for local demos."""
    
    paths = Paths.from_repo_root() if root is None else Paths(root=root)
    paths.data_processed_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(seed)
    
    user_id = [f"u{i:03d}" for i in range(1, n_users + 1)]
    study_hours = rng.integers(0, 40, size=n_users)
    gender = rng.choice(["Male", "Female"], size=n_users)
    Fedu = rng.choice([ "HighSchool", "Bachelor", "Master"],size=n_users,p=[ 0.35, 0.4, 0.25],)
    Medu = rng.choice([ "HighSchool", "Bachelor", "Master"],size=n_users,p=[ 0.4, 0.35, 0.25],)

    marks = (study_hours * 2 + rng.normal(50, 10, size=n_users)).clip(0, 100)

    def to_grade(score):
        if score >= 70:
            return 1   # pass
        else:
            return 0   # fail


    grade = [to_grade(m) for m in marks]
    
     
    df = pd.DataFrame({
        "student_id": user_id,
        "study_hours": study_hours,
        "gender": gender,
        "marks": marks.round(1),
        "father_edu": Fedu,
        "mother_edu": Medu,
        "grade": grade,
    })
    
    
    ext = best_effort_ext()
    out_path = paths.data_processed_dir / f"features{ext}"
    write_tabular(df, out_path)
    return out_path
