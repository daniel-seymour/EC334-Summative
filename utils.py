# utils.py
from pathlib import Path
from datetime import datetime

def timestamped_path(basename: str, outdir: str, ext: str):
    """
    Build an output path like '<outdir>/<basename>_YYYYMMDD-HHMMSS.<ext>',
    creating the directory if needed.
    """
    Path(outdir).mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    return Path(outdir) / f"{basename}_{ts}.{ext}"

def save_fig(fig, basename: str, outdir: str = "figures", **save_kwargs):
    """
    Save a matplotlib Figure object to a timestamped file.
    Returns the Path to the file.
    """
    p = timestamped_path(basename, outdir, "png")
    fig.savefig(p, **save_kwargs)
    return p

def save_df(df, basename: str, outdir: str = "tables", **to_csv_kwargs):
    """
    Save a pandas DataFrame to a timestamped CSV.
    Returns the Path to the file.
    """
    p = timestamped_path(basename, outdir, "csv")
    df.to_csv(p, **to_csv_kwargs)
    return p