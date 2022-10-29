---
layout: container
name:  "quay.io/biocontainers/bakdrive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bakdrive/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bakdrive/container.yaml"
updated_at: "2022-10-29 05:56:49.483950"
latest: "1.0.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bakdrive"
aliases:
 - "bakdrive"
 - "httpx"
 - "2to3-3.9"
 - "cbc"
 - "clp"
 - "cmark"
 - "f2py3.9"
 - "futurize"
 - "glpsol"
 - "idle3.9"
 - "isympy"
 - "normalizer"
versions:
 - "1.0.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bakdrive"
config: {"url": "https://biocontainers.pro/tools/bakdrive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bakdrive", "latest": {"1.0.4--hdfd78af_0": "sha256:248fdd478912ae707d9acf27b9ff2f704ef87a0ecd2f95fb5ee5dd306724b736"}, "tags": {"1.0.4--hdfd78af_0": "sha256:248fdd478912ae707d9acf27b9ff2f704ef87a0ecd2f95fb5ee5dd306724b736"}, "docker": "quay.io/biocontainers/bakdrive", "aliases": {"bakdrive": "/usr/local/bin/bakdrive", "httpx": "/usr/local/bin/httpx", "2to3-3.9": "/usr/local/bin/2to3-3.9", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "cmark": "/usr/local/bin/cmark", "f2py3.9": "/usr/local/bin/f2py3.9", "futurize": "/usr/local/bin/futurize", "glpsol": "/usr/local/bin/glpsol", "idle3.9": "/usr/local/bin/idle3.9", "isympy": "/usr/local/bin/isympy", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bakdrive.
shpc-registry automated BioContainers addition for bakdrive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bakdrive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bakdrive:1.0.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bakdrive/1.0.4--hdfd78af_0
$ module help quay.io/biocontainers/bakdrive/1.0.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bakdrive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bakdrive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bakdrive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bakdrive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bakdrive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bakdrive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bakdrive

```bash
$ singularity exec <container> /usr/local/bin/bakdrive
$ podman run --it --rm --entrypoint /usr/local/bin/bakdrive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bakdrive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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