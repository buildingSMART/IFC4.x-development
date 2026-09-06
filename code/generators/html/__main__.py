from __future__ import annotations

import argparse
import cProfile
import io
from pathlib import Path
import pstats

from .builder import StaticSiteBuilder
from .config import BuildConfig


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the IFC static HTML site.")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output directory for the generated site. Defaults to output/html under the repo root.",
    )
    parser.add_argument(
        "-j",
        "--threads",
        type=int,
        default=None,
        help="Number of worker processes used to render HTML pages. Defaults to up to 4 cores.",
    )
    parser.add_argument(
        "--sample-percent",
        type=float,
        default=None,
        help="Render only a deterministic sample of generated pages. Static pages are always included.",
    )
    parser.add_argument(
        "--include",
        nargs="+",
        default=None,
        metavar="PAGE",
        help="Only render generated pages whose paths match one of the given values. Example: --include '/'.",
    )
    parser.add_argument(
        "--profile",
        action="store_true",
        help="Run the build under cProfile. This forces in-process rendering so the profile captures real work.",
    )
    parser.add_argument(
        "--profile-output",
        type=Path,
        default=None,
        help="Optional path to write the cProfile summary report.",
    )
    parser.add_argument(
        "--no-index",
        action="store_true"
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    if args.profile:
        if args.profile_output is None:
            args.profile_output = repo_root / "output" / "profile" / "cprofile-summary.txt"

    config = BuildConfig.from_repo_root(
        repo_root,
        args.output,
        args.threads,
        args.sample_percent,
        args.profile,
        include_paths=args.include,
        no_index=args.no_index
    )
    builder = StaticSiteBuilder(config)

    if args.profile:
        profiler = cProfile.Profile()
        profiler.enable()
        summary = builder.build()
        profiler.disable()

        stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
        stats.print_stats(50)
        report = stream.getvalue()

        if args.profile_output is not None:
            args.profile_output.parent.mkdir(parents=True, exist_ok=True)
            args.profile_output.write_text(report, encoding="utf-8")

        print(report)
    else:
        summary = builder.build()

    print(f"Output: {config.output_dir}")
    print(f"Errors: {summary['errors']}")
    print(f"Written: {summary['written']}")


if __name__ == "__main__":
    main()
