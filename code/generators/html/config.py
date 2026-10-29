from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class BuildConfig:
    repo_root: Path
    code_dir: Path
    output_dir: Path
    threads: int = 1
    sample_percent: float = 100.0
    profile: bool = False
    include_paths: tuple[str, ...] | None = None
    no_index: bool = False

    @classmethod
    def from_repo_root(
        cls,
        repo_root: Path,
        output_dir: Path | None = None,
        threads: int | None = None,
        sample_percent: float | None = None,
        profile: bool = False,
        include_paths: tuple[str, ...] | None = None,
        no_index: bool = False
    ) -> "BuildConfig":
        repo_root = repo_root.resolve()
        code_dir = (repo_root / "code").resolve()
        if output_dir is None:
            output_dir = repo_root / "output" / "html"
        if threads is None:
            threads = max(1, min(4, os.cpu_count() or 1))
        if sample_percent is None:
            sample_percent = 100.0
        return cls(
            repo_root=repo_root,
            code_dir=code_dir,
            output_dir=Path(output_dir).resolve(),
            threads=max(1, threads),
            sample_percent=max(0.1, min(100.0, sample_percent)),
            profile=profile,
            include_paths=include_paths,
            no_index=no_index
        )
