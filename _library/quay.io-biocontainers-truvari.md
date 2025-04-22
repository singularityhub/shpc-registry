---
layout: container
name:  "quay.io/biocontainers/truvari"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/truvari/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/truvari/container.yaml"
updated_at: "2025-04-22 03:32:29.832708"
latest: "5.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/truvari"
aliases:
 - "bwamempy"
 - "truvari"
 - "cmark"
 - "pygmentize"
 - "futurize"
 - "pasteurize"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
versions:
 - "3.5.0--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
 - "4.1.0--pyhdfd78af_0"
 - "4.1.0--pyhdfd78af_1"
 - "4.2.2--pyhdfd78af_0"
 - "4.3.0--pyhdfd78af_0"
 - "4.3.1--pyhdfd78af_0"
 - "5.0.0--pyhdfd78af_0"
 - "5.1.1--pyhdfd78af_0"
 - "5.2.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for truvari"
config: {"url": "https://biocontainers.pro/tools/truvari", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for truvari", "latest": {"5.2.0--pyhdfd78af_0": "sha256:b3a47cda0bedd7782b427d1686f00b68d14a3260a5ba95b25c2a12625230469c"}, "tags": {"3.5.0--pyhdfd78af_0": "sha256:53513ea33dfdd6f7c0c37cfcc0af804202cdf6ec7a17a318b19d1014df761bd3", "4.0.0--pyhdfd78af_0": "sha256:ae370f515fe240679b2bc151f7e2c2db5a9e704ee811acd85a1c882f2170b808", "4.1.0--pyhdfd78af_0": "sha256:f60bd45e790c3b7feb6c343c60d4ac16a97f3185548fb0bd2b8a64a86907793e", "4.1.0--pyhdfd78af_1": "sha256:db78b97fd5a1221aedeb4530f24c1a2d15ce65fffaa4ee973e7a2e9e6d7a0299", "4.2.2--pyhdfd78af_0": "sha256:4f99c6d8738549467a8caf0b89df019f10d73fbd30cb9b89661b9cf82a322313", "4.3.0--pyhdfd78af_0": "sha256:31e29dd2d82d2146c4960648c30cc0bcead44763dbaa7b867bf006a101b721b3", "4.3.1--pyhdfd78af_0": "sha256:e4ecb26232ca0a7b6811da29f57c42ccdbaf99fefe291c5728c3c347bd895c8f", "5.0.0--pyhdfd78af_0": "sha256:25b446537d1bc96725b4042a4fc1f6a688e8381825ee6635bc1e45cb3c5777e4", "5.1.1--pyhdfd78af_0": "sha256:287844ffd531f9e04c1bcb48acc003238cd86e35e2d715c049cafb3b3cd91976", "5.2.0--pyhdfd78af_0": "sha256:b3a47cda0bedd7782b427d1686f00b68d14a3260a5ba95b25c2a12625230469c"}, "docker": "quay.io/biocontainers/truvari", "aliases": {"bwamempy": "/usr/local/bin/bwamempy", "truvari": "/usr/local/bin/truvari", "cmark": "/usr/local/bin/cmark", "pygmentize": "/usr/local/bin/pygmentize", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/truvari.
shpc-registry automated BioContainers addition for truvari
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/truvari
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/truvari:5.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/truvari/5.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/truvari/5.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### truvari-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### truvari-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### truvari-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### truvari-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### truvari-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### truvari-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwamempy

```bash
$ singularity exec <container> /usr/local/bin/bwamempy
$ podman run --it --rm --entrypoint /usr/local/bin/bwamempy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwamempy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### truvari

```bash
$ singularity exec <container> /usr/local/bin/truvari
$ podman run --it --rm --entrypoint /usr/local/bin/truvari   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/truvari   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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