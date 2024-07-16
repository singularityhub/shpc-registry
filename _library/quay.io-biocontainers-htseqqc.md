---
layout: container
name:  "quay.io/biocontainers/htseqqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/htseqqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/htseqqc/container.yaml"
updated_at: "2024-07-16 02:43:31.181643"
latest: "v1.0--pyh5bfb8f1_0"
container_url: "https://biocontainers.pro/tools/htseqqc"
aliases:
 - "Filter_Pair.py"
 - "Filter_Single.py"
 - "StatisticPair.py"
 - "StatisticSingle.py"
 - "common_functions.py"
 - "filter.py"
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
 - "v1.0--pyh5bfb8f1_0"
description: "shpc-registry automated BioContainers addition for htseqqc"
config: {"url": "https://biocontainers.pro/tools/htseqqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for htseqqc", "latest": {"v1.0--pyh5bfb8f1_0": "sha256:e60fe4f2f8c47c7d1a196403410becf5a6bae4378df3a06ac2118cec89766831"}, "tags": {"v1.0--pyh5bfb8f1_0": "sha256:e60fe4f2f8c47c7d1a196403410becf5a6bae4378df3a06ac2118cec89766831"}, "docker": "quay.io/biocontainers/htseqqc", "aliases": {"Filter_Pair.py": "/usr/local/bin/Filter_Pair.py", "Filter_Single.py": "/usr/local/bin/Filter_Single.py", "StatisticPair.py": "/usr/local/bin/StatisticPair.py", "StatisticSingle.py": "/usr/local/bin/StatisticSingle.py", "common_functions.py": "/usr/local/bin/common_functions.py", "filter.py": "/usr/local/bin/filter.py", "f2py3.6": "/usr/local/bin/f2py3.6", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/htseqqc.
shpc-registry automated BioContainers addition for htseqqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/htseqqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/htseqqc:v1.0--pyh5bfb8f1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/htseqqc/v1.0--pyh5bfb8f1_0
$ module help quay.io/biocontainers/htseqqc/v1.0--pyh5bfb8f1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htseqqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htseqqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htseqqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htseqqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htseqqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htseqqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Filter_Pair.py

```bash
$ singularity exec <container> /usr/local/bin/Filter_Pair.py
$ podman run --it --rm --entrypoint /usr/local/bin/Filter_Pair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Filter_Pair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Filter_Single.py

```bash
$ singularity exec <container> /usr/local/bin/Filter_Single.py
$ podman run --it --rm --entrypoint /usr/local/bin/Filter_Single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Filter_Single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StatisticPair.py

```bash
$ singularity exec <container> /usr/local/bin/StatisticPair.py
$ podman run --it --rm --entrypoint /usr/local/bin/StatisticPair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StatisticPair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StatisticSingle.py

```bash
$ singularity exec <container> /usr/local/bin/StatisticSingle.py
$ podman run --it --rm --entrypoint /usr/local/bin/StatisticSingle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StatisticSingle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### common_functions.py

```bash
$ singularity exec <container> /usr/local/bin/common_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/common_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/common_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter.py

```bash
$ singularity exec <container> /usr/local/bin/filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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