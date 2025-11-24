---
layout: container
name:  "quay.io/biocontainers/fast5seek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fast5seek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fast5seek/container.yaml"
updated_at: "2025-11-24 04:01:24.734800"
latest: "0.1.1--py_1"
container_url: "https://biocontainers.pro/tools/fast5seek"
aliases:
 - "fast5_subset"
 - "fast5seek"
 - "multi_to_single_fast5"
 - "single_to_multi_fast5"
 - "f2py3.6"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "2to3-3.6"
 - "idle3.6"
versions:
 - "0.1.1--py_1"
description: "shpc-registry automated BioContainers addition for fast5seek"
config: {"url": "https://biocontainers.pro/tools/fast5seek", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fast5seek", "latest": {"0.1.1--py_1": "sha256:20d41b26239f2347a138b95ef351e7c3063e35a4f568e7a9c2f4796a01430e0e"}, "tags": {"0.1.1--py_1": "sha256:20d41b26239f2347a138b95ef351e7c3063e35a4f568e7a9c2f4796a01430e0e"}, "docker": "quay.io/biocontainers/fast5seek", "aliases": {"fast5_subset": "/usr/local/bin/fast5_subset", "fast5seek": "/usr/local/bin/fast5seek", "multi_to_single_fast5": "/usr/local/bin/multi_to_single_fast5", "single_to_multi_fast5": "/usr/local/bin/single_to_multi_fast5", "f2py3.6": "/usr/local/bin/f2py3.6", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fast5seek.
shpc-registry automated BioContainers addition for fast5seek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fast5seek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fast5seek:0.1.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fast5seek/0.1.1--py_1
$ module help quay.io/biocontainers/fast5seek/0.1.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fast5seek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fast5seek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fast5seek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fast5seek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fast5seek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fast5seek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fast5_subset

```bash
$ singularity exec <container> /usr/local/bin/fast5_subset
$ podman run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast5seek

```bash
$ singularity exec <container> /usr/local/bin/fast5seek
$ podman run --it --rm --entrypoint /usr/local/bin/fast5seek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5seek   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi_to_single_fast5

```bash
$ singularity exec <container> /usr/local/bin/multi_to_single_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_to_multi_fast5

```bash
$ singularity exec <container> /usr/local/bin/single_to_multi_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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