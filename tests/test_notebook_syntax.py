import ast
import json
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = REPOSITORY_ROOT / "cardiac-surgery-and-percutaneous (1).ipynb"


class NotebookSyntaxTests(unittest.TestCase):
    def test_notebook_is_valid_json_and_code_cells_parse(self):
        notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
        self.assertIn("cells", notebook)
        code_cells = [
            (index, cell)
            for index, cell in enumerate(notebook["cells"])
            if cell.get("cell_type") == "code"
        ]
        self.assertTrue(code_cells, "Notebook should contain code cells")
        for index, cell in code_cells:
            source = "".join(cell.get("source", []))
            with self.subTest(cell=index):
                ast.parse(source, filename=f"notebook cell {index}")


if __name__ == "__main__":
    unittest.main()
