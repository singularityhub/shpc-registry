---
layout: container
name:  "quay.io/biocontainers/fba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fba/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fba/container.yaml"
updated_at: "2022-10-29 05:38:13.291784"
latest: "0.0.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/fba"
aliases:
 - "fba"
 - "umi_tools"
 - "brotli"
 - "cwebp"
 - "dwebp"
 - "f2py3.8"
 - "fonttools"
 - "futurize"
 - "gif2rgb"
 - "gif2webp"
 - "gifbuild"
 - "gifclrmp"
versions:
 - "0.0.12--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for fba"
config: {"url": "https://biocontainers.pro/tools/fba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fba", "latest": {"0.0.12--pyhdfd78af_0": "sha256:8cd46b212dcb9bdb51509917b1257d8db3392ed38da858478f2bc0dac5c5f901"}, "tags": {"0.0.12--pyhdfd78af_0": "sha256:8cd46b212dcb9bdb51509917b1257d8db3392ed38da858478f2bc0dac5c5f901"}, "docker": "quay.io/biocontainers/fba", "aliases": {"fba": "/usr/local/bin/fba", "umi_tools": "/usr/local/bin/umi_tools", "brotli": "/usr/local/bin/brotli", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "f2py3.8": "/usr/local/bin/f2py3.8", "fonttools": "/usr/local/bin/fonttools", "futurize": "/usr/local/bin/futurize", "gif2rgb": "/usr/local/bin/gif2rgb", "gif2webp": "/usr/local/bin/gif2webp", "gifbuild": "/usr/local/bin/gifbuild", "gifclrmp": "/usr/local/bin/gifclrmp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fba.
shpc-registry automated BioContainers addition for fba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fba:0.0.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fba/0.0.12--pyhdfd78af_0
$ module help quay.io/biocontainers/fba/0.0.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fba

```bash
$ singularity exec <container> /usr/local/bin/fba
$ podman run --it --rm --entrypoint /usr/local/bin/fba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### umi_tools

```bash
$ singularity exec <container> /usr/local/bin/umi_tools
$ podman run --it --rm --entrypoint /usr/local/bin/umi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/umi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2webp

```bash
$ singularity exec <container> /usr/local/bin/gif2webp
$ podman run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifclrmp

```bash
$ singularity exec <container> /usr/local/bin/gifclrmp
$ podman run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
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