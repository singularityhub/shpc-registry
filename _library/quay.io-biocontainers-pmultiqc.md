---
layout: container
name:  "quay.io/biocontainers/pmultiqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pmultiqc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pmultiqc/container.yaml"
updated_at: "2022-10-29 05:42:34.205637"
latest: "0.0.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pmultiqc"
aliases:
 - "parse_sdrf"
 - "2to3-3.10"
 - "brotli"
 - "chardetect"
 - "cmark"
 - "coloredlogs"
 - "f2py3.10"
 - "fonttools"
 - "futurize"
 - "humanfriendly"
 - "idle3.10"
versions:
 - "0.0.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pmultiqc"
config: {"url": "https://biocontainers.pro/tools/pmultiqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pmultiqc", "latest": {"0.0.9--pyhdfd78af_0": "sha256:5a090cd18ad36694211f29ff1102d887b5404596ae3009e39a8b8cec8b4bde4a"}, "tags": {"0.0.9--pyhdfd78af_0": "sha256:5a090cd18ad36694211f29ff1102d887b5404596ae3009e39a8b8cec8b4bde4a"}, "docker": "quay.io/biocontainers/pmultiqc", "aliases": {"parse_sdrf": "/usr/local/bin/parse_sdrf", "2to3-3.10": "/usr/local/bin/2to3-3.10", "brotli": "/usr/local/bin/brotli", "chardetect": "/usr/local/bin/chardetect", "cmark": "/usr/local/bin/cmark", "coloredlogs": "/usr/local/bin/coloredlogs", "f2py3.10": "/usr/local/bin/f2py3.10", "fonttools": "/usr/local/bin/fonttools", "futurize": "/usr/local/bin/futurize", "humanfriendly": "/usr/local/bin/humanfriendly", "idle3.10": "/usr/local/bin/idle3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pmultiqc.
shpc-registry automated BioContainers addition for pmultiqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pmultiqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pmultiqc:0.0.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pmultiqc/0.0.9--pyhdfd78af_0
$ module help quay.io/biocontainers/pmultiqc/0.0.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pmultiqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pmultiqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pmultiqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pmultiqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pmultiqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pmultiqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### parse_sdrf

```bash
$ singularity exec <container> /usr/local/bin/parse_sdrf
$ podman run --it --rm --entrypoint /usr/local/bin/parse_sdrf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_sdrf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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