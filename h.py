from augraphy import *
import random

import random

import numpy as np

from augraphy.base.augmentation import Augmentation
from augraphy.base.augmentationsequence import AugmentationSequence


class ONEOf(Augmentation):
    """Given a list of Augmentations, selects one to apply.

    :param augmentations: A list of Augmentations to choose from.
    :type augmentations: list
    :param p: The probability that this augmentation will be applied.
    :type p: float, optional
    """

    def __init__(self, augmentations, p=1):
        """Constructor method"""
        self.augmentations = augmentations
        self.augmentation_probabilities = self.compute_probability(self.augmentations)
        self.p = p

    # Randomly selects an Augmentation to apply to data.
    def __call__(self, image, layer=None, mask=None, keypoints=None, bounding_boxes=None, force=False):
        if force or self.should_run():

            # Select one augmentation using the max value in probability values
            augmentation = self.augmentations[np.argmax(self.augmentation_probabilities)]

            # Applies the selected Augmentation.
            image = augmentation(image, mask=mask, keypoints=keypoints, bounding_boxes=bounding_boxes, force=True)
            return image

    # Constructs a string containing the representations
    # of each augmentation
    def __repr__(self):
        r = "ONEOf([\n"

        for augmentation in self.augmentations:
            r += f"\t{repr(augmentation)}\n"

        r += f"], p={self.p})"
        return r

    def compute_probability(self, augmentations):
        """For each Augmentation in the input list, compute the probability of applying that Augmentation.

        :param augmentations: Augmentations to compute probability list for.
        :type augmentations: list
        """

        # generate random 0-1 value for each augmentation
        augmentation_probabilities = [random.uniform(0, 1.0) for augmentation in augmentations]
        probability_sum = sum(augmentation_probabilities)

        # generate weighted probability by using (probability/ sum of probabilities)
        augmentation_probabilities = [
            augmentation_probability / probability_sum for augmentation_probability in augmentation_probabilities
        ]

        return augmentation_probabilities

def last(bounding_boxes):

    pre_phase = [
        # Rescale(scale="optimal", target_dpi = 300,  p = 1.0),
    ]

    ink_phase = [
        InkColorSwap(
            ink_swap_color="random",
            ink_swap_sequence_number_range=(5, 10),
            ink_swap_min_width_range=(2, 3),
            ink_swap_max_width_range=(100, 120),
            ink_swap_min_height_range=(2, 3),
            ink_swap_max_height_range=(100, 120),
            ink_swap_min_area_range=(10, 20),
            ink_swap_max_area_range=(400, 500),
            p=0.2,
        ),
        LinesDegradation(
            line_roi=(0.0, 0.0, 1.0, 1.0),
            line_gradient_range=(32, 255),
            line_gradient_direction=(0, 2),
            line_split_probability=(0.2, 0.4),
            line_replacement_value=(250, 255),
            line_min_length=(30, 40),
            line_long_to_short_ratio=(5, 7),
            line_replacement_probability=(0.4, 0.5),
            line_replacement_thickness=(1, 3),
            p=0.2,
        ),
        ONEOf(
            [
                Dithering(
                    dither=random.choice(["ordered", "floyd-steinberg"]),
                    order=(3, 5),
                ),
            ],
            p=0.2,
        ),
        ONEOf(
            [
                Letterpress(
                    n_samples=(100, 400),
                    n_clusters=(200, 400),
                    std_range=(500, 3000),
                    value_range=(150, 224),
                    value_threshold_range=(96, 128),
                    blur=1,
                ),
            ],
            p=0.2,
        ),
        ONEOf(
            [
                LowInkRandomLines(
                    count_range=(5, 10),
                    use_consistent_lines=random.choice([True, False]),
                    noise_probability=0.1,
                ),
                LowInkPeriodicLines(
                    count_range=(2, 5),
                    period_range=(16, 32),
                    use_consistent_lines=random.choice([True, False]),
                    noise_probability=0.1,
                ),
            ],
            p=0.2,
        ),
    ]

    paper_phase = [
        PaperFactory(p=0.2),
        ColorPaper(
            hue_range=(0, 255),
            saturation_range=(10, 40),
            p=0.2,
        ),
        ONEOf(
            [
                PatternGenerator(
                    imgx=random.randint(256, 512),
                    imgy=random.randint(256, 512),
                    n_rotation_range=(10, 15),
                    color="random",
                    alpha_range=(0.25, 0.5),
                ),
                VoronoiTessellation(
                    mult_range=(50, 80),
                    seed=19829813472,
                    num_cells_range=(500, 1000),
                    noise_type="random",
                    background_value=(200, 255),
                ),
            ],
            p=0.2,
        ),
        WaterMark(
            watermark_word="random",
            watermark_font_size=(10, 15),
            watermark_font_thickness=(20, 25),
            watermark_rotation=(0, 360),
            watermark_location="random",
            watermark_color="random",
            watermark_method="darken",
            p=0.2,
        ),
        ONEOf(
            [
                AugmentationSequence(
                    [
                        NoiseTexturize(
                            sigma_range=(3, 10),
                            turbulence_range=(2, 5),
                            texture_width_range=(300, 500),
                            texture_height_range=(300, 500),
                        ),
                        BrightnessTexturize(
                            texturize_range=(0.9, 0.99),
                            deviation=0.03,
                        ),
                    ],
                ),
                AugmentationSequence(
                    [
                        BrightnessTexturize(
                            texturize_range=(0.9, 0.99),
                            deviation=0.03,
                        ),
                        NoiseTexturize(
                            sigma_range=(3, 10),
                            turbulence_range=(2, 5),
                            texture_width_range=(300, 500),
                            texture_height_range=(300, 500),
                        ),
                    ],
                ),
            ],
            p=0.2,
        ),
    ]

    post_phase = [
        ONEOf(
            [
                Folding(
                    fold_x=None,
                    fold_deviation=(0, 0),
                    fold_count=random.randint(2, 8),
                    fold_noise=0.001,
                    fold_angle_range=(-360, 360),
                    gradient_width=(0.1, 0.2),
                    gradient_height=(0.005, 0.01),
                    backdrop_color=(0, 0, 0),
                ),
                DirtyDrum(
                    line_width_range=(1, 6),
                    line_concentration=random.uniform(0.05, 0.15),
                    direction=random.randint(0, 2),
                    noise_intensity=random.uniform(0.1, 0.3),
                    noise_value=(64, 224),
                    ksize=random.choice([(3, 3), (5, 5), (7, 7)]),
                    sigmaX=0,
                    p=0.2,
                ),
                DirtyRollers(
                    line_width_range=(16,32),
                    scanline_type=0,
                ),
            ],
            p=0.2,
        ),
        ONEOf(
            [
                LightingGradient(
                    light_position=None,
                    direction=None,
                    max_brightness=255,
                    min_brightness=0,
                    mode="gaussian",
                    linear_decay_rate=None,
                    transparency=None,
                ),
                Brightness(
                    brightness_range=(0.9, 1.1),
                    min_brightness=0,
                    min_brightness_value=(120, 150),
                ),
                Gamma(
                    gamma_range=(0.9, 1.1),
                ),
            ],
            p=0.2,
        ),
        ONEOf(
            [
                Markup(
                    num_lines_range=(2, 7),
                    markup_length_range=(0.5, 1),
                    markup_thickness_range=(1, 2),
                    markup_type=random.choice(["strikethrough", "crossed", "highlight", "underline"]),
                    markup_color="random",
                    single_word_mode=False,
                    repetitions=1,
                ),
            ],
            p=0.2,
        ),
        ONEOf(
            [
                ShadowCast(
                    shadow_side="random",
                    shadow_vertices_range=(1, 20),
                    shadow_width_range=(0.3, 0.8),
                    shadow_height_range=(0.3, 0.8),
                    shadow_color=(0.1, 0.1, 0.1),
                    shadow_opacity_range=(0.2, 0.9),
                    shadow_iterations_range=(1, 2),
                    shadow_blur_kernel_range=(101, 301),
                ),
            ],
            p=0.2,
        ),    
        ONEOf(
            [
                InkMottling(
                    ink_mottling_alpha_range=(0.2, 0.3),
                    ink_mottling_noise_scale_range=(2, 2),
                    ink_mottling_gaussian_kernel_range=(3, 5),
                ),
            ],
            p=0.2,
        ),
    ]

    pipeline = AugraphyPipeline(
        ink_phase=ink_phase,
        # paper_phase=paper_phase,
        post_phase=post_phase,
        pre_phase=[],
        bounding_boxes=bounding_boxes,
        mask = None,
        keypoints=None,
        log=False,
    )

    return pipeline

