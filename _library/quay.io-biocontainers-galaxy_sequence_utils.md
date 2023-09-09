---
layout: container
name:  "quay.io/biocontainers/galaxy_sequence_utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/galaxy_sequence_utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/galaxy_sequence_utils/container.yaml"
updated_at: "2023-09-09 03:05:15.759114"
latest: "1.1.5--py_0"
container_url: "https://biocontainers.pro/tools/galaxy_sequence_utils"
aliases:
 - "gx-fastq-combiner"
 - "gx-fastq-filter"
 - "gx-fastq-groomer"
 - "gx-fastq-manipulation"
 - "gx-fastq-masker-by-quality"
 - "gx-fastq-paired-end-deinterlacer"
 - "gx-fastq-paired-end-interlacer"
 - "gx-fastq-paired-end-joiner"
 - "gx-fastq-paired-end-splitter"
 - "gx-fastq-stats"
 - "gx-fastq-to-fasta"
 - "gx-fastq-to-tabular"
 - "gx-fastq-trimmer"
 - "gx-fastq-trimmer-by-quality"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.1.5--py_0"
description: "shpc-registry automated BioContainers addition for galaxy_sequence_utils"
config: {"url": "https://biocontainers.pro/tools/galaxy_sequence_utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for galaxy_sequence_utils", "latest": {"1.1.5--py_0": "sha256:4efad4ef94ed27fd0149780b0f9ee7d1c03e8f375fda17613a9c793bfc4e4510"}, "tags": {"1.1.5--py_0": "sha256:4efad4ef94ed27fd0149780b0f9ee7d1c03e8f375fda17613a9c793bfc4e4510"}, "docker": "quay.io/biocontainers/galaxy_sequence_utils", "aliases": {"gx-fastq-combiner": "/usr/local/bin/gx-fastq-combiner", "gx-fastq-filter": "/usr/local/bin/gx-fastq-filter", "gx-fastq-groomer": "/usr/local/bin/gx-fastq-groomer", "gx-fastq-manipulation": "/usr/local/bin/gx-fastq-manipulation", "gx-fastq-masker-by-quality": "/usr/local/bin/gx-fastq-masker-by-quality", "gx-fastq-paired-end-deinterlacer": "/usr/local/bin/gx-fastq-paired-end-deinterlacer", "gx-fastq-paired-end-interlacer": "/usr/local/bin/gx-fastq-paired-end-interlacer", "gx-fastq-paired-end-joiner": "/usr/local/bin/gx-fastq-paired-end-joiner", "gx-fastq-paired-end-splitter": "/usr/local/bin/gx-fastq-paired-end-splitter", "gx-fastq-stats": "/usr/local/bin/gx-fastq-stats", "gx-fastq-to-fasta": "/usr/local/bin/gx-fastq-to-fasta", "gx-fastq-to-tabular": "/usr/local/bin/gx-fastq-to-tabular", "gx-fastq-trimmer": "/usr/local/bin/gx-fastq-trimmer", "gx-fastq-trimmer-by-quality": "/usr/local/bin/gx-fastq-trimmer-by-quality", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/galaxy_sequence_utils.
shpc-registry automated BioContainers addition for galaxy_sequence_utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/galaxy_sequence_utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/galaxy_sequence_utils:1.1.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/galaxy_sequence_utils/1.1.5--py_0
$ module help quay.io/biocontainers/galaxy_sequence_utils/1.1.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### galaxy_sequence_utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### galaxy_sequence_utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### galaxy_sequence_utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### galaxy_sequence_utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### galaxy_sequence_utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### galaxy_sequence_utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gx-fastq-combiner

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-combiner
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-filter

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-filter
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-groomer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-groomer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-groomer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-groomer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-manipulation

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-manipulation
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-manipulation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-manipulation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-masker-by-quality

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-masker-by-quality
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-masker-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-masker-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-deinterlacer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-deinterlacer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-deinterlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-deinterlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-interlacer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-interlacer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-interlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-interlacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-joiner

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-joiner
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-joiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-joiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-paired-end-splitter

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-paired-end-splitter
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-paired-end-splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-stats

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-stats
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-to-tabular

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-to-tabular
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-to-tabular   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-trimmer

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-trimmer
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx-fastq-trimmer-by-quality

```bash
$ singularity exec <container> /usr/local/bin/gx-fastq-trimmer-by-quality
$ podman run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx-fastq-trimmer-by-quality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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