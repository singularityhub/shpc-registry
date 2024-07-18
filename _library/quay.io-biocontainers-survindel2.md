---
layout: container
name:  "quay.io/biocontainers/survindel2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/survindel2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/survindel2/container.yaml"
updated_at: "2024-07-18 03:09:36.650084"
latest: "1.1.3--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/survindel2"
aliases:
 - "clip_consensus_builder"
 - "dp_clusterer"
 - "features.py"
 - "merge_identical_calls"
 - "normalise"
 - "random_pos_generator.py"
 - "reads_categorizer"
 - "survindel2.py"
 - "survindel2_run_classifier.py"
 - "survindel2_train_classifier.py"
 - "annot-tsv"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "faidx"
 - "htsfile"
 - "bgzip"
 - "tabix"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.1.3--h4ac6f70_0"
description: "singularity registry hpc automated addition for survindel2"
config: {"url": "https://biocontainers.pro/tools/survindel2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for survindel2", "latest": {"1.1.3--h4ac6f70_0": "sha256:9da3ffc0a82d4ebe8404eaf1e3f64bf261908c0e3776ebcecdc5c1527e2cec97"}, "tags": {"1.1.3--h4ac6f70_0": "sha256:9da3ffc0a82d4ebe8404eaf1e3f64bf261908c0e3776ebcecdc5c1527e2cec97"}, "docker": "quay.io/biocontainers/survindel2", "aliases": {"clip_consensus_builder": "/usr/local/bin/clip_consensus_builder", "dp_clusterer": "/usr/local/bin/dp_clusterer", "features.py": "/usr/local/bin/features.py", "merge_identical_calls": "/usr/local/bin/merge_identical_calls", "normalise": "/usr/local/bin/normalise", "random_pos_generator.py": "/usr/local/bin/random_pos_generator.py", "reads_categorizer": "/usr/local/bin/reads_categorizer", "survindel2.py": "/usr/local/bin/survindel2.py", "survindel2_run_classifier.py": "/usr/local/bin/survindel2_run_classifier.py", "survindel2_train_classifier.py": "/usr/local/bin/survindel2_train_classifier.py", "annot-tsv": "/usr/local/bin/annot-tsv", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "faidx": "/usr/local/bin/faidx", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/survindel2.
singularity registry hpc automated addition for survindel2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/survindel2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/survindel2:1.1.3--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/survindel2/1.1.3--h4ac6f70_0
$ module help quay.io/biocontainers/survindel2/1.1.3--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### survindel2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### survindel2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### survindel2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### survindel2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### survindel2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### survindel2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clip_consensus_builder

```bash
$ singularity exec <container> /usr/local/bin/clip_consensus_builder
$ podman run --it --rm --entrypoint /usr/local/bin/clip_consensus_builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clip_consensus_builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dp_clusterer

```bash
$ singularity exec <container> /usr/local/bin/dp_clusterer
$ podman run --it --rm --entrypoint /usr/local/bin/dp_clusterer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dp_clusterer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### features.py

```bash
$ singularity exec <container> /usr/local/bin/features.py
$ podman run --it --rm --entrypoint /usr/local/bin/features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_identical_calls

```bash
$ singularity exec <container> /usr/local/bin/merge_identical_calls
$ podman run --it --rm --entrypoint /usr/local/bin/merge_identical_calls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_identical_calls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalise

```bash
$ singularity exec <container> /usr/local/bin/normalise
$ podman run --it --rm --entrypoint /usr/local/bin/normalise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### random_pos_generator.py

```bash
$ singularity exec <container> /usr/local/bin/random_pos_generator.py
$ podman run --it --rm --entrypoint /usr/local/bin/random_pos_generator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/random_pos_generator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reads_categorizer

```bash
$ singularity exec <container> /usr/local/bin/reads_categorizer
$ podman run --it --rm --entrypoint /usr/local/bin/reads_categorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reads_categorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### survindel2.py

```bash
$ singularity exec <container> /usr/local/bin/survindel2.py
$ podman run --it --rm --entrypoint /usr/local/bin/survindel2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/survindel2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### survindel2_run_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/survindel2_run_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/survindel2_run_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/survindel2_run_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### survindel2_train_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/survindel2_train_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/survindel2_train_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/survindel2_train_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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