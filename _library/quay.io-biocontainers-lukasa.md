---
layout: container
name:  "quay.io/biocontainers/lukasa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lukasa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/lukasa/container.yaml"
updated_at: "2022-10-27 00:55:33.583120"
latest: "0.0.8--py310hdfd78af_1"
container_url: "https://biocontainers.pro/tools/lukasa"
aliases:
 - "catchr.pl"
 - "corepack"
 - "cwl-cite-extract"
 - "cwl-docker-extract"
 - "cwl-explode"
 - "cwl-expression-refactor"
 - "cwl-format"
 - "cwl-graph-split"
 - "cwl-normalizer"
 - "cwl-upgrader"
 - "lukasa.py"
 - "makblk.pl"
 - "makdbs"
 - "makeidx.pl"
 - "makmdm"
 - "metaeuk"
 - "node"
 - "npm"
 - "npx"
 - "sortgrcd"
 - "spaln"
 - "spspaln.pl"
versions:
 - "0.0.8--py310hdfd78af_1"
description: "shpc-registry automated BioContainers addition for lukasa"
config: {"url": "https://biocontainers.pro/tools/lukasa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lukasa", "latest": {"0.0.8--py310hdfd78af_1": "sha256:e55304725d85cb9cc8859c82f3ecdf95d0b2cada7e792bb18ff4ff6321567737"}, "tags": {"0.0.8--py310hdfd78af_1": "sha256:e55304725d85cb9cc8859c82f3ecdf95d0b2cada7e792bb18ff4ff6321567737"}, "docker": "quay.io/biocontainers/lukasa", "aliases": {"catchr.pl": "/usr/local/bin/catchr.pl", "corepack": "/usr/local/bin/corepack", "cwl-cite-extract": "/usr/local/bin/cwl-cite-extract", "cwl-docker-extract": "/usr/local/bin/cwl-docker-extract", "cwl-explode": "/usr/local/bin/cwl-explode", "cwl-expression-refactor": "/usr/local/bin/cwl-expression-refactor", "cwl-format": "/usr/local/bin/cwl-format", "cwl-graph-split": "/usr/local/bin/cwl-graph-split", "cwl-normalizer": "/usr/local/bin/cwl-normalizer", "cwl-upgrader": "/usr/local/bin/cwl-upgrader", "lukasa.py": "/usr/local/bin/lukasa.py", "makblk.pl": "/usr/local/bin/makblk.pl", "makdbs": "/usr/local/bin/makdbs", "makeidx.pl": "/usr/local/bin/makeidx.pl", "makmdm": "/usr/local/bin/makmdm", "metaeuk": "/usr/local/bin/metaeuk", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "npx": "/usr/local/bin/npx", "sortgrcd": "/usr/local/bin/sortgrcd", "spaln": "/usr/local/bin/spaln", "spspaln.pl": "/usr/local/bin/spspaln.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lukasa.
shpc-registry automated BioContainers addition for lukasa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lukasa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lukasa:0.0.8--py310hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lukasa/0.0.8--py310hdfd78af_1
$ module help quay.io/biocontainers/lukasa/0.0.8--py310hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lukasa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lukasa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lukasa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lukasa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lukasa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lukasa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### catchr.pl

```bash
$ singularity exec <container> /usr/local/bin/catchr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/catchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-cite-extract

```bash
$ singularity exec <container> /usr/local/bin/cwl-cite-extract
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-cite-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-cite-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-docker-extract

```bash
$ singularity exec <container> /usr/local/bin/cwl-docker-extract
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-docker-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-docker-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-explode

```bash
$ singularity exec <container> /usr/local/bin/cwl-explode
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-explode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-explode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-expression-refactor

```bash
$ singularity exec <container> /usr/local/bin/cwl-expression-refactor
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-expression-refactor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-expression-refactor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-format

```bash
$ singularity exec <container> /usr/local/bin/cwl-format
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-graph-split

```bash
$ singularity exec <container> /usr/local/bin/cwl-graph-split
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-graph-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-graph-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-normalizer

```bash
$ singularity exec <container> /usr/local/bin/cwl-normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-upgrader

```bash
$ singularity exec <container> /usr/local/bin/cwl-upgrader
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-upgrader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-upgrader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lukasa.py

```bash
$ singularity exec <container> /usr/local/bin/lukasa.py
$ podman run --it --rm --entrypoint /usr/local/bin/lukasa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lukasa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makblk.pl

```bash
$ singularity exec <container> /usr/local/bin/makblk.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makblk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makblk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makdbs

```bash
$ singularity exec <container> /usr/local/bin/makdbs
$ podman run --it --rm --entrypoint /usr/local/bin/makdbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makdbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeidx.pl

```bash
$ singularity exec <container> /usr/local/bin/makeidx.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makeidx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeidx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makmdm

```bash
$ singularity exec <container> /usr/local/bin/makmdm
$ podman run --it --rm --entrypoint /usr/local/bin/makmdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makmdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaeuk

```bash
$ singularity exec <container> /usr/local/bin/metaeuk
$ podman run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortgrcd

```bash
$ singularity exec <container> /usr/local/bin/sortgrcd
$ podman run --it --rm --entrypoint /usr/local/bin/sortgrcd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortgrcd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaln

```bash
$ singularity exec <container> /usr/local/bin/spaln
$ podman run --it --rm --entrypoint /usr/local/bin/spaln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaln   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spspaln.pl

```bash
$ singularity exec <container> /usr/local/bin/spspaln.pl
$ podman run --it --rm --entrypoint /usr/local/bin/spspaln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spspaln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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