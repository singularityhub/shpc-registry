---
layout: container
name:  "quay.io/biocontainers/wgsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wgsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wgsim/container.yaml"
updated_at: "2025-11-28 03:36:19.372995"
latest: "1.0--h577a1d6_10"
container_url: "https://biocontainers.pro/tools/wgsim"
aliases:
 - "wgsim"
 - "wgsim_eval.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0--h7132678_5"
 - "1.0--h7132678_6"
 - "1.0--he4a0461_7"
 - "1.0--h577a1d6_8"
 - "1.0--h577a1d6_9"
 - "1.0--h577a1d6_10"
description: "shpc-registry automated BioContainers addition for wgsim"
config: {"url": "https://biocontainers.pro/tools/wgsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wgsim", "latest": {"1.0--h577a1d6_10": "sha256:e1a6049a6483a1fee4438c3a0bb8ea424156ed1f3e47f4b3efb793fd5b299b1c"}, "tags": {"1.0--h7132678_5": "sha256:649797d4a94d3a34605296782c44829f94ad89a25d6e679ec93a2d2ac373c30c", "1.0--h7132678_6": "sha256:2c6f858bbc2e93fc0d3a48c81511855ea6980cee871a0a26be455257ca639023", "1.0--he4a0461_7": "sha256:be81c52fe7d8e0173f64ead0a11789bf3efca49c9c4411bb307a1456f89172b4", "1.0--h577a1d6_8": "sha256:72ec63be44c0feb746f7cb7f2d3c9f1d20afad31d1425cd7c16010e5814e6b38", "1.0--h577a1d6_9": "sha256:e1abb6ad460dc1d9eb5d8bbb68d1544daf173ae05dad6226aad6c950d55b24c0", "1.0--h577a1d6_10": "sha256:e1a6049a6483a1fee4438c3a0bb8ea424156ed1f3e47f4b3efb793fd5b299b1c"}, "docker": "quay.io/biocontainers/wgsim", "aliases": {"wgsim": "/usr/local/bin/wgsim", "wgsim_eval.pl": "/usr/local/bin/wgsim_eval.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wgsim.
shpc-registry automated BioContainers addition for wgsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wgsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wgsim:1.0--h577a1d6_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wgsim/1.0--h577a1d6_10
$ module help quay.io/biocontainers/wgsim/1.0--h577a1d6_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wgsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wgsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wgsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wgsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wgsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wgsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wgsim

```bash
$ singularity exec <container> /usr/local/bin/wgsim
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim_eval.pl

```bash
$ singularity exec <container> /usr/local/bin/wgsim_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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