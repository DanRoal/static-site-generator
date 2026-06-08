from page_generator import extract_title
from functions import markdown_to_blocks
import unittest


class TestExtractTitle(unittest.TestCase):
    def test_extract_single_title(self):
        md = "# Hello World"
        result = extract_title(md)
        self.assertEqual(result, "Hello World")

    def test_extract_title_with_content(self):
        md = """# Main Title

This is some paragraph content"""
        result = extract_title(md)
        self.assertEqual(result, "Main Title")

    def test_extract_title_first_among_blocks(self):
        md = """# First Title

Some paragraph here

Another paragraph"""
        result = extract_title(md)
        self.assertEqual(result, "First Title")

    def test_extract_title_middle_blocks(self):
        md = """Some paragraph

# Middle Title

Another paragraph"""
        result = extract_title(md)
        self.assertEqual(result, "Middle Title")

    def test_extract_title_with_extra_whitespace(self):
        md = "#   Title with spaces   "
        result = extract_title(md)
        self.assertEqual(result, "Title with spaces")

    def test_extract_multiple_titles_returns_first(self):
        md = """# First Title

# Second Title"""
        result = extract_title(md)
        self.assertEqual(result, "First Title")

    def test_extract_title_not_found(self):
        md = """## Heading 2

Some paragraph content"""
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "There was no title in provided markdown")

    def test_extract_title_no_heading(self):
        md = """This is just a paragraph

And another paragraph"""
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_only_code_block(self):
        md = """```
print("hello")
```"""
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
