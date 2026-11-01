import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
import check_tokens  # noqa: E402
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



class SharedLightTest(unittest.TestCase):
    def tokens(self, pair):
        panel = {"name": "panel", "value": {"light": "#17161A", "dark": "#000000"}}
        if pair is not None:
            panel["pair"] = pair
        return {"core": {"color": [{"name": "ink", "value": {"light": "#17161A", "dark": "#F2F2F2"}}]},
                "layers": {"kit": {"themes": ["light", "dark"], "color": ["@ink", panel]}}}

    def run_check(self, t):
        check_tokens.errors.clear()
        check_tokens.check_shared_light(t)
        return list(check_tokens.errors)

    def test_collision_needs_pair(self):
        self.assertEqual(len(self.run_check(self.tokens(None))), 1)

    def test_pair_accepted(self):
        self.assertEqual(self.run_check(self.tokens(True)), [])

    def test_stale_pair_rejected(self):
        t = self.tokens(True)
        t["layers"]["kit"]["color"][1]["value"]["light"] = "#222222"
        self.assertEqual(len(self.run_check(t)), 1)



class VariantTest(unittest.TestCase):
    def tokens(self, carry_on_accent):
        colours = ["@mint", "@on-mint", "@fairy-accent"] + (["@fairy-on-accent"] if carry_on_accent else [])
        return {
            "core": {"color": [{"name": "mint", "value": {"dark": "#43F3B7"}},
                               {"name": "on-mint", "value": {"dark": "#033423"}}]},
            "layers": {"app": {"themes": ["dark"], "color": colours}},
            "variants": {"fairy": {"color": [
                {"name": "fairy-accent", "value": {"dark": "#FF8FC7"}, "replaces": "mint"},
                {"name": "fairy-on-accent", "value": {"dark": "#3D0A26"}, "replaces": "on-mint"}]}},
            "contrast": [{"fg": "on-mint", "bg": "mint", "min": 4.5, "layers": ["app"]}],
        }

    def test_half_a_variant_is_rejected(self):
        check_tokens.errors.clear()
        check_tokens.check_variants(self.tokens(False))
        self.assertEqual(len(check_tokens.errors), 1)

    def test_whole_variant_passes_and_contrast_is_checked_swapped(self):
        t = self.tokens(True)
        check_tokens.errors.clear()
        check_tokens.check_variants(t)
        self.assertEqual(check_tokens.errors, [])
        cases = list(check_tokens.contrast_cases(t, ["app"]))
        self.assertEqual([v for _, v, _ in cases], [None, "fairy"])
        self.assertEqual(cases[1][2]["mint"]["dark"], "#FF8FC7")


if __name__ == "__main__":
    unittest.main()
