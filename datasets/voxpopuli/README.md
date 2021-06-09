---
annotations_creators:
- other
language_creators:
- other
languages:
- en
- de
- fr
- es
- pl
- it
- ro
- hu
- cs
- nl
- fi
- hr
- sk
- sl
- et
- lt
- pt
- bg
- el
- lv
- mt
- sv
- da
licenses:
- cc-by-nc-4.0
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
- 100K<n<1M
source_datasets:
- original
task_categories:
- other
task_ids:
- other-other-automatic-speech-recognition
---

# Dataset Card for [Dataset Name]

## Table of Contents
- [Dataset Card for [Dataset Name]](#dataset-card-for-dataset-name)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/facebookresearch/voxpopuli
- **Repository:** https://github.com/facebookresearch/voxpopuli
- **Paper:** https://arxiv.org/abs/2101.00390
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

A large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation. The raw data is collected from 2009-2020 European Parliament plenary session recordings. In each session, members of the European Parliament give speeches in turn in different European Union languages. The speeches are interpreted into each language. The (unlabelled) dataset contains both the original source speech and the respective interpreted speech.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The unlabelled audio is in 23 languages: Bulgarian (Bg), Czech (Cs), Croatian (Hr), Danish (Da), Dutch (Nl), English (En), Estonian (Et), Finnish (Fi), French (Fr), German (De), Greek (El), Hungarian (Hu), Italian (It), Latvian (Lv), Lithuanian (Lt), Maltese (Mt), Polish (Pl), Portuguese (Pt), Romanian (Ro), Slovak (Sk), Slovene (Sl), Spanish (Es) and Swedish (Sv).

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

- id (`string`): unique id of the data sample.

- file (`string`): A path to the downloaded audio file in .ogg format.

- language (`string`): the language of the data sample.

- year (`int`): the year for the data sample.

- segments (seq. of pairs of `floats`): start and end values (in seconds) for speech segments within the data file.

### Data Splits

There is a config for each individual of the 23 languages which will download all unlabelled data for each language from the years 2009-2020.  Additionally, the unlabelled 10K config contains 10K hours of unlabelled data (train-split only) for all 23 languages from only the years 2019-2020.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The (unlabelled) data includes all source (original speech) and target (interpreted speech) for all 23 EU languages (excluding Irish because of very limited data availability). The provided segments are created by segmenting each full-session audio into short clips of 15-30 seconds using an energy-based voice activity detection (VAD) algorithm. Each audio clip has a maximum of 2 seconds of continuous silence, and silent clips were discarded. Around 13% data were dropped after silence removal, leading to a final overall duration of around 100K hours across all 23 languages.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The dataset was created by Facebook AI, specifically: Changhan Wang, Morgane Rivière, Ann Lee, Anne Wu, Chaitanya Talnikar, Daniel Haziza, Mary Williamson, Juan Pino, Emmanuel Dupoux.

The original data was created and shared by the [European Parliament](https://multimedia.europarl.europa.eu/en/home).

### Licensing Information

[CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) (see also European Parliament's [legal notice](https://www.europarl.europa.eu/legal-notice/en/) for the raw data)

### Citation Information
```
@article{wang2021voxpopuli,
  title={VoxPopuli: A Large-Scale Multilingual Speech Corpus for Representation Learning, Semi-Supervised Learning and Interpretation},
  author={Wang, Changhan and Rivi{\`e}re, Morgane and Lee, Ann and Wu, Anne and Talnikar, Chaitanya and Haziza, Daniel and Williamson, Mary and Pino, Juan and Dupoux, Emmanuel},
  journal={arXiv preprint arXiv:2101.00390},
  year={2021}
}
```

### Contributions

Thanks to [@jfainberg](https://github.com/jfainberg) for adding this dataset.
