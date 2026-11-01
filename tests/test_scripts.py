import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
import gen_tokens  # noqa: E402
import tokens_lib as tl  # noqa: E402


class TokensLibTest(unittest.TestCase):
    def test_contrast_extremes(self):
        self.assertAlmostEqual(tl.contrast("#FFFFFF", "#000000"), 21.0, places=1)
        self.assertAlmostEqual(tl.contrast("#777777", "#777777"), 1.0)

    def test_argb_and_num(self):
        self.assertEqual(tl.argb("#43F3B7"), "0xFF43F3B7")
        self.assertEqual(tl.argb("#2E43F3B7"), "0x2E43F3B7")
        self.assertEqual(tl.num("16px"), 16)
        self.assertEqual(tl.num("1.3em"), 1.3)

    def test_every_layer_carries_core(self):
        t = tl.load()
        for layer in t["layers"]:
            names = {tok["name"] for tok in tl.resolve(t, layer)["color"]}
            self.assertTrue({tok["name"] for tok in t["core"]["color"]} <= names, layer)

    def test_alias_followed(self):
        c = tl.colour_map(tl.load(), "uikit")
        self.assertEqual(c["snackbar"], c["ink"])

    def test_css_moves_alpha_last(self):
        self.assertEqual(gen_tokens.css_hex("#2E43F3B7"), "#43F3B72E")

    def test_generation_is_deterministic(self):
        t = tl.load()
        self.assertEqual(gen_tokens.uikit_java(t), gen_tokens.uikit_java(t))


if __name__ == "__main__":
    unittest.main()
