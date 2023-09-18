---
layout: container
name:  "quay.io/biocontainers/surpyvor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/surpyvor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/surpyvor/container.yaml"
updated_at: "2023-09-18 02:50:38.197265"
latest: "0.15.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/surpyvor"
aliases:
 - "SURVIVOR"
 - "surpyvor"
 - "cyvcf2"
 - "coloredlogs"
 - "humanfriendly"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
versions:
 - "0.8.1--py_1"
 - "0.12.0--pyhdfd78af_0"
 - "0.11.0--pyhdfd78af_0"
 - "0.10.0--pyhdfd78af_0"
 - "0.13.0--pyhdfd78af_0"
 - "0.15.0--pyhdfd78af_0"
 - "0.14.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for surpyvor"
config: {"url": "https://biocontainers.pro/tools/surpyvor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for surpyvor", "latest": {"0.15.0--pyhdfd78af_0": "sha256:bde8beb467b400f2a9662a1e999f93c495561e9040cd6b87f0bef39988876e43"}, "tags": {"0.8.1--py_1": "sha256:fac270c3114ac8a77003046632ca27a2fbe0350830e8a1f229a7a639dce9154b", "0.12.0--pyhdfd78af_0": "sha256:9c9abb9c938e473bfc1c0d2724a9f72f55d4b592b3925daaed4949d691167df1", "0.11.0--pyhdfd78af_0": "sha256:e89303a071ffbda359b1559df9d975369701949df2da6c644ee38ae721b367e3", "0.10.0--pyhdfd78af_0": "sha256:22db281fa1a955eccd16771093ec7f33f6853b7163272e42fb2fb430a1a25fcc", "0.13.0--pyhdfd78af_0": "sha256:4b1bb060aff08b9ba24c3218654a64c51ce1864d718e8540d06fa2c68e40a5c5", "0.15.0--pyhdfd78af_0": "sha256:bde8beb467b400f2a9662a1e999f93c495561e9040cd6b87f0bef39988876e43", "0.14.0--pyhdfd78af_0": "sha256:ee7fb71aef0247b2f94f00d5065dc0712d595634d2dfeb4ea138d317da813350"}, "docker": "quay.io/biocontainers/surpyvor", "aliases": {"SURVIVOR": "/usr/local/bin/SURVIVOR", "surpyvor": "/usr/local/bin/surpyvor", "cyvcf2": "/usr/local/bin/cyvcf2", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/surpyvor.
shpc-registry automated BioContainers addition for surpyvor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/surpyvor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/surpyvor:0.15.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/surpyvor/0.15.0--pyhdfd78af_0
$ module help quay.io/biocontainers/surpyvor/0.15.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### surpyvor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### surpyvor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### surpyvor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### surpyvor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### surpyvor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### surpyvor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SURVIVOR

```bash
$ singularity exec <container> /usr/local/bin/SURVIVOR
$ podman run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### surpyvor

```bash
$ singularity exec <container> /usr/local/bin/surpyvor
$ podman run --it --rm --entrypoint /usr/local/bin/surpyvor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/surpyvor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
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