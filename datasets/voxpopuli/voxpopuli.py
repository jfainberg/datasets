# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""VoxPopuli dataset"""


import csv
import os
from collections import defaultdict

import datasets


_CITATION = """\
@article{wang2021voxpopuli,
  title={VoxPopuli: A Large-Scale Multilingual Speech Corpus for Representation Learning, Semi-Supervised Learning and Interpretation},
  author={Wang, Changhan and Rivi{\\`e}re, Morgane and Lee, Ann and Wu, Anne and Talnikar, Chaitanya and Haziza, Daniel and Williamson, Mary and Pino, Juan and Dupoux, Emmanuel},
  journal={arXiv preprint arXiv:2101.00390},
  year={2021}
}
"""

_DESCRIPTION = """\
A large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .ogg format and is not converted to a float32 array. To convert the audio
file to a float32 array, please make use of the `.map()` function as follows:


```python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```
"""

_HOMEPAGE = "https://github.com/facebookresearch/voxpopuli"

_LICENSE = "https://creativecommons.org/share-your-work/public-domain/cc0/"

_AUDIO_URL = "https://dl.fbaipublicfiles.com/voxpopuli/audios/{lang}_{year}.tar"
_ANNOTATIONS_URL = "https://dl.fbaipublicfiles.com/voxpopuli/annotations/unlabelled.tsv.gz"

_LANGUAGES = [
    "en",
    "de",
    "fr",
    "es",
    "pl",
    "it",
    "ro",
    "hu",
    "cs",
    "nl",
    "fi",
    "hr",
    "sk",
    "sl",
    "et",
    "lt",
    "pt",
    "bg",
    "el",
    "lv",
    "mt",
    "sv",
    "da",
]


class VoxPopuliConfig(datasets.BuilderConfig):
    """BuilderConfig for VoxPopuli."""

    def __init__(self, name, **kwargs):
        """
        Args:
          data_dir: `string`, the path to the folder containing the files in the
            downloaded .tar
          citation: `string`, citation for the data set
          url: `string`, url for information about the data set
          **kwargs: keyword arguments forwarded to super.
        """
        self.languages = kwargs.pop("languages", None)
        self.years = kwargs.pop("years", None)
        super(VoxPopuliConfig, self).__init__(name=name, version=datasets.Version("1.0.0", ""), **kwargs)


class VoxPopuli(datasets.GeneratorBasedBuilder):
    """VoxPopuli dataset."""

    VERSION = datasets.Version("1.0.0")

    # Subsets by individual language
    BUILDER_CONFIGS = [
        VoxPopuliConfig(
            name=lang,
            description=f"All data for {lang} across the years 2009-2020.",
            languages=[lang],
            years=range(2009, 2021),
        )
        for lang in _LANGUAGES
    ]

    # Subsets by size
    BUILDER_CONFIGS.append(
        VoxPopuliConfig(
            name="10K",
            description="10K hours of unlabelled audio across 23 languages from the years 2019-202.",
            languages=_LANGUAGES,
            years=[2019, 2020],
        )
    )

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "file": datasets.Value("string"),
                    "language": datasets.Value("string"),
                    "year": datasets.Value("uint16"),
                    "segments": datasets.features.Sequence(
                        {
                            "start": datasets.Value("float32"),
                            "end": datasets.Value("float32"),
                        }
                    ),
                }
            ),
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        urls = [
            _AUDIO_URL.format(lang=lang, year=year) for lang in self.config.languages for year in self.config.years
        ]
        dir_paths = dl_manager.download_and_extract(urls)
        annotations_path = dl_manager.download_and_extract(_ANNOTATIONS_URL)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN, gen_kwargs={"dir_paths": dir_paths, "annotations_path": annotations_path}
            )
        ]

    def _generate_examples(self, dir_paths, annotations_path):
        """Yields examples as (key, example) tuples."""
        # Get segment start/ends

        file_to_starts = defaultdict(list)
        file_to_ends = defaultdict(list)
        with open(annotations_path, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
            for row in reader:
                file_to_starts[row["event_id"]].append(row["start"])
                file_to_ends[row["event_id"]].append(row["end"])

        for dir_path in dir_paths:
            for lang in os.listdir(dir_path):
                for year in os.listdir(os.path.join(dir_path, lang)):
                    for audio_file in os.listdir(os.path.join(dir_path, lang, year)):
                        key, _ = os.path.splitext(audio_file)
                        example = {
                            "id": key,
                            "file": os.path.join(dir_path, lang, year, audio_file),
                            "language": lang,
                            "year": year,
                            "segments": {"start": file_to_starts[key], "end": file_to_ends[key]},
                        }
                        yield key, example
