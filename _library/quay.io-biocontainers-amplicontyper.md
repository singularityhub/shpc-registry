---
layout: container
name:  "quay.io/biocontainers/amplicontyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amplicontyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/amplicontyper/container.yaml"
updated_at: "2025-11-08 03:16:20.824940"
latest: "0.1.29--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/amplicontyper"
aliases:
 - "check_for_update.py"
 - "classifier_report.py"
 - "classify"
 - "classify.py"
 - "data_classes.py"
 - "genotyper_utilities"
 - "genotyper_utilities.py"
 - "hierarchy_utils.py"
 - "html_head.txt"
 - "input_processing.py"
 - "inputs_validation.py"
 - "map.py"
 - "model_manager.py"
 - "read_classifier.py"
 - "reporting_classes.py"
 - "train"
 - "train.py"
 - "x86_64-conda-linux-gnu.cfg"
 - "annot-tsv"
 - "numpy-config"
 - "sdust"
 - "paftools.js"
 - "k8"
 - "minimap2"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "tqdm"
 - "normalizer"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
 - "md5sum-lite"
versions:
 - "0.1.28--pyhdfd78af_0"
 - "0.1.29--pyhdfd78af_0"
description: "singularity registry hpc automated addition for amplicontyper"
config: {"url": "https://biocontainers.pro/tools/amplicontyper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for amplicontyper", "latest": {"0.1.29--pyhdfd78af_0": "sha256:b5e1f69d5fc6acb6638f5143e3650fecbb07155178409c2f971c202714730cae"}, "tags": {"0.1.28--pyhdfd78af_0": "sha256:4304d9f7f95e01fd265f132b57ce0ae46f63ba1c16adb32f83d54cd6565eb4fb", "0.1.29--pyhdfd78af_0": "sha256:b5e1f69d5fc6acb6638f5143e3650fecbb07155178409c2f971c202714730cae"}, "docker": "quay.io/biocontainers/amplicontyper", "aliases": {"check_for_update.py": "/usr/local/bin/check_for_update.py", "classifier_report.py": "/usr/local/bin/classifier_report.py", "classify": "/usr/local/bin/classify", "classify.py": "/usr/local/bin/classify.py", "data_classes.py": "/usr/local/bin/data_classes.py", "genotyper_utilities": "/usr/local/bin/genotyper_utilities", "genotyper_utilities.py": "/usr/local/bin/genotyper_utilities.py", "hierarchy_utils.py": "/usr/local/bin/hierarchy_utils.py", "html_head.txt": "/usr/local/bin/html_head.txt", "input_processing.py": "/usr/local/bin/input_processing.py", "inputs_validation.py": "/usr/local/bin/inputs_validation.py", "map.py": "/usr/local/bin/map.py", "model_manager.py": "/usr/local/bin/model_manager.py", "read_classifier.py": "/usr/local/bin/read_classifier.py", "reporting_classes.py": "/usr/local/bin/reporting_classes.py", "train": "/usr/local/bin/train", "train.py": "/usr/local/bin/train.py", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "annot-tsv": "/usr/local/bin/annot-tsv", "numpy-config": "/usr/local/bin/numpy-config", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "k8": "/usr/local/bin/k8", "minimap2": "/usr/local/bin/minimap2", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amplicontyper.
singularity registry hpc automated addition for amplicontyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amplicontyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amplicontyper:0.1.29--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amplicontyper/0.1.29--pyhdfd78af_0
$ module help quay.io/biocontainers/amplicontyper/0.1.29--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amplicontyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amplicontyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amplicontyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amplicontyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amplicontyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amplicontyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check_for_update.py

```bash
$ singularity exec <container> /usr/local/bin/check_for_update.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_for_update.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_for_update.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classifier_report.py

```bash
$ singularity exec <container> /usr/local/bin/classifier_report.py
$ podman run --it --rm --entrypoint /usr/local/bin/classifier_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classifier_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classify

```bash
$ singularity exec <container> /usr/local/bin/classify
$ podman run --it --rm --entrypoint /usr/local/bin/classify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classify.py

```bash
$ singularity exec <container> /usr/local/bin/classify.py
$ podman run --it --rm --entrypoint /usr/local/bin/classify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### data_classes.py

```bash
$ singularity exec <container> /usr/local/bin/data_classes.py
$ podman run --it --rm --entrypoint /usr/local/bin/data_classes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/data_classes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotyper_utilities

```bash
$ singularity exec <container> /usr/local/bin/genotyper_utilities
$ podman run --it --rm --entrypoint /usr/local/bin/genotyper_utilities   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotyper_utilities   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotyper_utilities.py

```bash
$ singularity exec <container> /usr/local/bin/genotyper_utilities.py
$ podman run --it --rm --entrypoint /usr/local/bin/genotyper_utilities.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotyper_utilities.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hierarchy_utils.py

```bash
$ singularity exec <container> /usr/local/bin/hierarchy_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/hierarchy_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hierarchy_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### html_head.txt

```bash
$ singularity exec <container> /usr/local/bin/html_head.txt
$ podman run --it --rm --entrypoint /usr/local/bin/html_head.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/html_head.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### input_processing.py

```bash
$ singularity exec <container> /usr/local/bin/input_processing.py
$ podman run --it --rm --entrypoint /usr/local/bin/input_processing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/input_processing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inputs_validation.py

```bash
$ singularity exec <container> /usr/local/bin/inputs_validation.py
$ podman run --it --rm --entrypoint /usr/local/bin/inputs_validation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inputs_validation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map.py

```bash
$ singularity exec <container> /usr/local/bin/map.py
$ podman run --it --rm --entrypoint /usr/local/bin/map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### model_manager.py

```bash
$ singularity exec <container> /usr/local/bin/model_manager.py
$ podman run --it --rm --entrypoint /usr/local/bin/model_manager.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/model_manager.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/read_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reporting_classes.py

```bash
$ singularity exec <container> /usr/local/bin/reporting_classes.py
$ podman run --it --rm --entrypoint /usr/local/bin/reporting_classes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reporting_classes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train

```bash
$ singularity exec <container> /usr/local/bin/train
$ podman run --it --rm --entrypoint /usr/local/bin/train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train.py

```bash
$ singularity exec <container> /usr/local/bin/train.py
$ podman run --it --rm --entrypoint /usr/local/bin/train.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-short

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa

```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5sum-lite

```bash
$ singularity exec <container> /usr/local/bin/md5sum-lite
$ podman run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)