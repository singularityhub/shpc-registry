---
layout: container
name:  "quay.io/biocontainers/clever-toolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clever-toolkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clever-toolkit/container.yaml"
updated_at: "2025-11-21 03:57:20.081122"
latest: "2.4--h077b44d_14"
container_url: "https://biocontainers.pro/tools/clever-toolkit"
aliases:
 - "add-score-tags-to-bam"
 - "bam-to-alignment-priors"
 - "bam2fastq"
 - "clever"
 - "clever-core"
 - "ctk-version"
 - "evaluate-sv-predictions"
 - "extract-bad-reads"
 - "filter-bam"
 - "filter-variations"
 - "genotyper"
 - "insert-length-histogram"
 - "laser"
 - "laser-core"
 - "laser-recalibrate"
 - "mateclever"
 - "mateclever-compute-rois"
 - "merge-putative-variations"
 - "merge-to-vcf"
 - "multiline-to-xa"
 - "plot-insert-size-distribution"
 - "postprocess-predictions"
 - "precompute-distributions"
 - "read-group-stats"
 - "remove-redundant-variations"
 - "split-priors-by-chromosome"
 - "split-reads"
 - "vcf-to-deletionlist"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
 - "qhelpconverter"
 - "guess-ploidy.py"
versions:
 - "2.4--py35_boost1.64_0"
 - "2.4--py38hda97c0d_10"
 - "2.4--hd03093a_12"
 - "2.4--hdcf5f25_13"
 - "2.4--h077b44d_14"
description: "shpc-registry automated BioContainers addition for clever-toolkit"
config: {"url": "https://biocontainers.pro/tools/clever-toolkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clever-toolkit", "latest": {"2.4--h077b44d_14": "sha256:63ba9a1af0e110ef1adbb0678a3fdd0331a334d2e8dbf5ec784301db01e8b6b7"}, "tags": {"2.4--py35_boost1.64_0": "sha256:c64a8ee7dc263bbf489ed21aa07a4a7d479fcd27b15d1eaa569c1b258e880bc3", "2.4--py38hda97c0d_10": "sha256:8c0ce2e1ee301a2d63cc027fae790c7470bee22f129b1703d6600680e75b8f71", "2.4--hd03093a_12": "sha256:dc9e2fdcffda925af46102818c65ce6cbaecca80f313927f98bb23a7de5ccf65", "2.4--hdcf5f25_13": "sha256:28d73d87e699344f573c60403e8b34537004dc70545e40cfa935cf4b0f1471de", "2.4--h077b44d_14": "sha256:63ba9a1af0e110ef1adbb0678a3fdd0331a334d2e8dbf5ec784301db01e8b6b7"}, "docker": "quay.io/biocontainers/clever-toolkit", "aliases": {"add-score-tags-to-bam": "/usr/local/bin/add-score-tags-to-bam", "bam-to-alignment-priors": "/usr/local/bin/bam-to-alignment-priors", "bam2fastq": "/usr/local/bin/bam2fastq", "clever": "/usr/local/bin/clever", "clever-core": "/usr/local/bin/clever-core", "ctk-version": "/usr/local/bin/ctk-version", "evaluate-sv-predictions": "/usr/local/bin/evaluate-sv-predictions", "extract-bad-reads": "/usr/local/bin/extract-bad-reads", "filter-bam": "/usr/local/bin/filter-bam", "filter-variations": "/usr/local/bin/filter-variations", "genotyper": "/usr/local/bin/genotyper", "insert-length-histogram": "/usr/local/bin/insert-length-histogram", "laser": "/usr/local/bin/laser", "laser-core": "/usr/local/bin/laser-core", "laser-recalibrate": "/usr/local/bin/laser-recalibrate", "mateclever": "/usr/local/bin/mateclever", "mateclever-compute-rois": "/usr/local/bin/mateclever-compute-rois", "merge-putative-variations": "/usr/local/bin/merge-putative-variations", "merge-to-vcf": "/usr/local/bin/merge-to-vcf", "multiline-to-xa": "/usr/local/bin/multiline-to-xa", "plot-insert-size-distribution": "/usr/local/bin/plot-insert-size-distribution", "postprocess-predictions": "/usr/local/bin/postprocess-predictions", "precompute-distributions": "/usr/local/bin/precompute-distributions", "read-group-stats": "/usr/local/bin/read-group-stats", "remove-redundant-variations": "/usr/local/bin/remove-redundant-variations", "split-priors-by-chromosome": "/usr/local/bin/split-priors-by-chromosome", "split-reads": "/usr/local/bin/split-reads", "vcf-to-deletionlist": "/usr/local/bin/vcf-to-deletionlist", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5", "qhelpconverter": "/usr/local/bin/qhelpconverter", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clever-toolkit.
shpc-registry automated BioContainers addition for clever-toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clever-toolkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clever-toolkit:2.4--h077b44d_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clever-toolkit/2.4--h077b44d_14
$ module help quay.io/biocontainers/clever-toolkit/2.4--h077b44d_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clever-toolkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clever-toolkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clever-toolkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clever-toolkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clever-toolkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clever-toolkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add-score-tags-to-bam

```bash
$ singularity exec <container> /usr/local/bin/add-score-tags-to-bam
$ podman run --it --rm --entrypoint /usr/local/bin/add-score-tags-to-bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add-score-tags-to-bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam-to-alignment-priors

```bash
$ singularity exec <container> /usr/local/bin/bam-to-alignment-priors
$ podman run --it --rm --entrypoint /usr/local/bin/bam-to-alignment-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam-to-alignment-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2fastq

```bash
$ singularity exec <container> /usr/local/bin/bam2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clever

```bash
$ singularity exec <container> /usr/local/bin/clever
$ podman run --it --rm --entrypoint /usr/local/bin/clever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clever   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clever-core

```bash
$ singularity exec <container> /usr/local/bin/clever-core
$ podman run --it --rm --entrypoint /usr/local/bin/clever-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clever-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctk-version

```bash
$ singularity exec <container> /usr/local/bin/ctk-version
$ podman run --it --rm --entrypoint /usr/local/bin/ctk-version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctk-version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evaluate-sv-predictions

```bash
$ singularity exec <container> /usr/local/bin/evaluate-sv-predictions
$ podman run --it --rm --entrypoint /usr/local/bin/evaluate-sv-predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluate-sv-predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-bad-reads

```bash
$ singularity exec <container> /usr/local/bin/extract-bad-reads
$ podman run --it --rm --entrypoint /usr/local/bin/extract-bad-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-bad-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-bam

```bash
$ singularity exec <container> /usr/local/bin/filter-bam
$ podman run --it --rm --entrypoint /usr/local/bin/filter-bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-variations

```bash
$ singularity exec <container> /usr/local/bin/filter-variations
$ podman run --it --rm --entrypoint /usr/local/bin/filter-variations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-variations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotyper

```bash
$ singularity exec <container> /usr/local/bin/genotyper
$ podman run --it --rm --entrypoint /usr/local/bin/genotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### insert-length-histogram

```bash
$ singularity exec <container> /usr/local/bin/insert-length-histogram
$ podman run --it --rm --entrypoint /usr/local/bin/insert-length-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/insert-length-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### laser

```bash
$ singularity exec <container> /usr/local/bin/laser
$ podman run --it --rm --entrypoint /usr/local/bin/laser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/laser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### laser-core

```bash
$ singularity exec <container> /usr/local/bin/laser-core
$ podman run --it --rm --entrypoint /usr/local/bin/laser-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/laser-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### laser-recalibrate

```bash
$ singularity exec <container> /usr/local/bin/laser-recalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/laser-recalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/laser-recalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mateclever

```bash
$ singularity exec <container> /usr/local/bin/mateclever
$ podman run --it --rm --entrypoint /usr/local/bin/mateclever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mateclever   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mateclever-compute-rois

```bash
$ singularity exec <container> /usr/local/bin/mateclever-compute-rois
$ podman run --it --rm --entrypoint /usr/local/bin/mateclever-compute-rois   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mateclever-compute-rois   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-putative-variations

```bash
$ singularity exec <container> /usr/local/bin/merge-putative-variations
$ podman run --it --rm --entrypoint /usr/local/bin/merge-putative-variations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-putative-variations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-to-vcf

```bash
$ singularity exec <container> /usr/local/bin/merge-to-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/merge-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiline-to-xa

```bash
$ singularity exec <container> /usr/local/bin/multiline-to-xa
$ podman run --it --rm --entrypoint /usr/local/bin/multiline-to-xa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiline-to-xa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-insert-size-distribution

```bash
$ singularity exec <container> /usr/local/bin/plot-insert-size-distribution
$ podman run --it --rm --entrypoint /usr/local/bin/plot-insert-size-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-insert-size-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### postprocess-predictions

```bash
$ singularity exec <container> /usr/local/bin/postprocess-predictions
$ podman run --it --rm --entrypoint /usr/local/bin/postprocess-predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/postprocess-predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### precompute-distributions

```bash
$ singularity exec <container> /usr/local/bin/precompute-distributions
$ podman run --it --rm --entrypoint /usr/local/bin/precompute-distributions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/precompute-distributions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read-group-stats

```bash
$ singularity exec <container> /usr/local/bin/read-group-stats
$ podman run --it --rm --entrypoint /usr/local/bin/read-group-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read-group-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove-redundant-variations

```bash
$ singularity exec <container> /usr/local/bin/remove-redundant-variations
$ podman run --it --rm --entrypoint /usr/local/bin/remove-redundant-variations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove-redundant-variations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-priors-by-chromosome

```bash
$ singularity exec <container> /usr/local/bin/split-priors-by-chromosome
$ podman run --it --rm --entrypoint /usr/local/bin/split-priors-by-chromosome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-priors-by-chromosome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-reads

```bash
$ singularity exec <container> /usr/local/bin/split-reads
$ podman run --it --rm --entrypoint /usr/local/bin/split-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-to-deletionlist

```bash
$ singularity exec <container> /usr/local/bin/vcf-to-deletionlist
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-to-deletionlist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-to-deletionlist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m

```bash
$ singularity exec <container> /usr/local/bin/python3.5m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.5

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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