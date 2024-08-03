---
layout: container
name:  "quay.io/biocontainers/handyreadgenotyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/handyreadgenotyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/handyreadgenotyper/container.yaml"
updated_at: "2024-08-03 03:06:13.583102"
latest: "0.1.22--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/handyreadgenotyper"
aliases:
 - "classifier_report.py"
 - "classify"
 - "classify.py"
 - "data_classes.py"
 - "genotyper_data_classes.py"
 - "input_processing.py"
 - "inputs_validation.py"
 - "map.py"
 - "model_manager.py"
 - "read_classifier.py"
 - "train"
 - "train.py"
 - "annot-tsv"
 - "sdust"
 - "k8"
 - "paftools.js"
 - "minimap2"
 - "f2py3.8"
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
 - "plot-bamstats"
 - "psl2sam.pl"
 - "sam2vcf.pl"
 - "samtools.pl"
 - "seq_cache_populate.pl"
 - "soap2sam.pl"
versions:
 - "0.1.13--pyhdfd78af_0"
 - "0.1.18--pyhdfd78af_0"
 - "0.1.22--pyhdfd78af_0"
description: "singularity registry hpc automated addition for handyreadgenotyper"
config: {"url": "https://biocontainers.pro/tools/handyreadgenotyper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for handyreadgenotyper", "latest": {"0.1.22--pyhdfd78af_0": "sha256:48efa1acf1526c5e1a15d52afd647e7056363e21e873e58c1a55853bd765a1d2"}, "tags": {"0.1.13--pyhdfd78af_0": "sha256:98acf5eb6edb20b9befbc68eea340849db97f0482170c86d377f568c75e748c6", "0.1.18--pyhdfd78af_0": "sha256:b028d37e3aff491d52389002e9d1f1144b6d9bd0ff2293fe759b598df9c29f72", "0.1.22--pyhdfd78af_0": "sha256:48efa1acf1526c5e1a15d52afd647e7056363e21e873e58c1a55853bd765a1d2"}, "docker": "quay.io/biocontainers/handyreadgenotyper", "aliases": {"classifier_report.py": "/usr/local/bin/classifier_report.py", "classify": "/usr/local/bin/classify", "classify.py": "/usr/local/bin/classify.py", "data_classes.py": "/usr/local/bin/data_classes.py", "genotyper_data_classes.py": "/usr/local/bin/genotyper_data_classes.py", "input_processing.py": "/usr/local/bin/input_processing.py", "inputs_validation.py": "/usr/local/bin/inputs_validation.py", "map.py": "/usr/local/bin/map.py", "model_manager.py": "/usr/local/bin/model_manager.py", "read_classifier.py": "/usr/local/bin/read_classifier.py", "train": "/usr/local/bin/train", "train.py": "/usr/local/bin/train.py", "annot-tsv": "/usr/local/bin/annot-tsv", "sdust": "/usr/local/bin/sdust", "k8": "/usr/local/bin/k8", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "f2py3.8": "/usr/local/bin/f2py3.8", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite", "plot-bamstats": "/usr/local/bin/plot-bamstats", "psl2sam.pl": "/usr/local/bin/psl2sam.pl", "sam2vcf.pl": "/usr/local/bin/sam2vcf.pl", "samtools.pl": "/usr/local/bin/samtools.pl", "seq_cache_populate.pl": "/usr/local/bin/seq_cache_populate.pl", "soap2sam.pl": "/usr/local/bin/soap2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/handyreadgenotyper.
singularity registry hpc automated addition for handyreadgenotyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/handyreadgenotyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/handyreadgenotyper:0.1.22--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/handyreadgenotyper/0.1.22--pyhdfd78af_0
$ module help quay.io/biocontainers/handyreadgenotyper/0.1.22--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### handyreadgenotyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### handyreadgenotyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### handyreadgenotyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### handyreadgenotyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### handyreadgenotyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### handyreadgenotyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### genotyper_data_classes.py

```bash
$ singularity exec <container> /usr/local/bin/genotyper_data_classes.py
$ podman run --it --rm --entrypoint /usr/local/bin/genotyper_data_classes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotyper_data_classes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### plot-bamstats

```bash
$ singularity exec <container> /usr/local/bin/plot-bamstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/psl2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/sam2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools.pl

```bash
$ singularity exec <container> /usr/local/bin/samtools.pl
$ podman run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.pl

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/soap2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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