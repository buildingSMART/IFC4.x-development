"""Compatibility entry point for the canonical EXPRESS-to-XSD generator.

Keep the historical command usable while sharing the implementation and IFC
XML binding configuration used by the current publication pipeline.
"""
from generators.util.express_to_xsd import main


if __name__ == "__main__":
    main()
