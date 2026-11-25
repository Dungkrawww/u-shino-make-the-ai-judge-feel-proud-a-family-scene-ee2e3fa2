# u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2: Make the AI Judge Feel Proud
# One short family scene, one or two lines and no more than 280 characters.
# The program writes the scene to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The scene: a small domestic moment — Dad's weekly call, Mum shouting the
# football score in the background, comfortable silence. Warm, specific,
# a little funny, genuinely affectionate rather than greeting-card sweet.
SCENE = (
    "Dad still calls every Sunday to ask if I've eaten, then stays on the line "
    "in comfortable silence while Mum shouts the football score in the background "
    "— and somehow that's the best conversation of my week."
)


def validate_scene(text):
    assert 1 <= len(text) <= 280, f"scene is {len(text)} chars, must be 1-280"
    assert text.strip(), "scene must not be only whitespace"
    assert text.count("\n") <= 1, "scene must be one or two lines"


def main():
    validate_scene(SCENE)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
