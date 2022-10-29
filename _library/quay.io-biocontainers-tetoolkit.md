---
layout: container
name:  "quay.io/biocontainers/tetoolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tetoolkit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tetoolkit/container.yaml"
updated_at: "2022-10-29 05:55:27.693867"
latest: "2.0.3--py_1"
container_url: "https://biocontainers.pro/tools/tetoolkit"
aliases:
 - "TEcount"
 - "TEtranscripts"
 - "ace2sam"
 - "bcftools"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "color-chrs.pl"
 - "export2sam.pl"
 - "guess-ploidy.py"
 - "idle"
 - "interpolate_sam.pl"
 - "maq2sam-long"
versions:
 - "2.0.3--py_1"
description: "shpc-registry automated BioContainers addition for tetoolkit"
config: {"url": "https://biocontainers.pro/tools/tetoolkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tetoolkit", "latest": {"2.0.3--py_1": "sha256:13035591e530c3b924bc8e83b979ca519140be38b6b904ffc42a4eb560a8f74a"}, "tags": {"2.0.3--py_1": "sha256:13035591e530c3b924bc8e83b979ca519140be38b6b904ffc42a4eb560a8f74a"}, "docker": "quay.io/biocontainers/tetoolkit", "aliases": {"TEcount": "/usr/local/bin/TEcount", "TEtranscripts": "/usr/local/bin/TEtranscripts", "ace2sam": "/usr/local/bin/ace2sam", "bcftools": "/usr/local/bin/bcftools", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "idle": "/usr/local/bin/idle", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tetoolkit.
shpc-registry automated BioContainers addition for tetoolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tetoolkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tetoolkit:2.0.3--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tetoolkit/2.0.3--py_1
$ module help quay.io/biocontainers/tetoolkit/2.0.3--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tetoolkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tetoolkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tetoolkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tetoolkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tetoolkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tetoolkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TEcount

```bash
$ singularity exec <container> /usr/local/bin/TEcount
$ podman run --it --rm --entrypoint /usr/local/bin/TEcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TEcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TEtranscripts

```bash
$ singularity exec <container> /usr/local/bin/TEtranscripts
$ podman run --it --rm --entrypoint /usr/local/bin/TEtranscripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TEtranscripts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
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