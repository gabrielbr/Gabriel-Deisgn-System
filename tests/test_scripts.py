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

    def product(self):
        """A product layer the way a product repo keeps it (docs/products.md): every core token,
        three themes with night falling back to dark, and a partner brand that swaps mint."""
        t = tl.load()
        core = tl.core_index(t)
        layer = {g: ["@" + n for n in core[g]] for g in tl.GROUPS}
        layer.update(themes=["light", "dark", "night"], theme_fallback={"night": "dark"}, brand="p",
                     type=[{"group": "body", "styles": [{"name": "body", "fontSize": "16px", "lineHeight": "24px"}]}])
        t["layers"] = {"app": layer}
        t["brands"] = {"p": {"name": "Partner", "type": {"family": "\"Partner Sans\", sans-serif", "faces": ["p.ttf"]},
                             "color": [{"replaces": "mint", "value": {"light": "#5DC2BB", "dark": "#5DC2BB"}}]}}
        return t

    def test_compose_writes_a_product_layer(self):
        kt = gen_tokens.compose_kt(self.product(), "app", "com.example.ui.theme", "XTokens", ["Values for X."])
        self.assertIn("package com.example.ui.theme", kt)
        self.assertIn("object XTokens {", kt)
        self.assertIn(" * Values for X.", kt)
        light = kt[kt.index("val Light"):kt.index("val Dark")]
        dark = kt[kt.index("val Dark"):kt.index("val Night")]
        night = kt[kt.index("val Night"):kt.index("object Spacing")]
        # Every theme has every role; night, not spelled out, falls back to dark.
        self.assertEqual(light.count("= Color("), dark.count("= Color("))
        self.assertEqual(dark.replace("Dark", "Night"), night)
        # The brand swaps a colour role and names the family, nothing else.
        self.assertIn("mint = Color(0xFF5DC2BB)", light)
        self.assertIn('const val fontFamily = "Partner Sans"', kt)
        self.assertIn("const val bodySize = 16", kt)

    def test_generation_is_deterministic(self):
        t = tl.load()
        self.assertEqual(gen_tokens.uikit_java(t), gen_tokens.uikit_java(t))



class SharedLightTest(unittest.TestCase):
    def tokens(self, pair):
        panel = {"name": "panel", "value": {"light": "#17161A", "dark": "#000000"}}
        if pair is not None:
            panel["pair"] = pair
        return {"core": {"color": [{"name": "ink", "value": {"light": "#17161A", "dark": "#F2F2F2"}}]},
                "layers": {"uikit": {"themes": ["light", "dark"], "color": ["@ink", panel]}}}

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
        t["layers"]["uikit"]["color"][1]["value"]["light"] = "#222222"
        self.assertEqual(len(self.run_check(t)), 1)



class BrandTest(unittest.TestCase):
    def tokens(self, replaces="mint", themes=("light", "dark")):
        return {
            "core": {"color": [{"name": "mint", "value": {"light": "#43F3B7", "dark": "#43F3B7"}}]},
            "layers": {"app": {"themes": ["light", "dark"], "brand": "b",
                               "color": ["@mint", {"name": "event-nap", "value": {"light": "#1C7ED6", "dark": "#5BA8FF"}}]}},
            "brands": {"b": {"name": "B", "type": {"family": "X", "faces": ["x.ttf"]},
                             "color": [{"replaces": replaces, "value": {th: "#5DC2BB" for th in themes}}]}},
        }

    def run_check(self, t):
        check_tokens.errors.clear()
        check_tokens.check_brands(t)
        return list(check_tokens.errors)

    def test_brand_swaps_a_colour_role(self):
        t = self.tokens()
        self.assertEqual(self.run_check(t), [])
        self.assertEqual(tl.colour_map(t, "app")["mint"], {"light": "#5DC2BB", "dark": "#5DC2BB"})
        self.assertEqual(tl.colour_map(t, "app")["event-nap"]["light"], "#1C7ED6")

    def test_brand_may_not_touch_data_colours(self):
        self.assertEqual(len(self.run_check(self.tokens(replaces="event-nap"))), 1)

    def test_brand_covers_every_theme(self):
        self.assertEqual(len(self.run_check(self.tokens(themes=("light",)))), 1)

    def test_brand_swaps_nothing_but_colour_and_type(self):
        t = self.tokens()
        t["brands"]["b"]["radius"] = []
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
