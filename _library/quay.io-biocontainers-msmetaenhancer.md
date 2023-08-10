---
layout: container
name:  "quay.io/biocontainers/msmetaenhancer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msmetaenhancer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msmetaenhancer/container.yaml"
updated_at: "2023-08-10 03:14:05.823859"
latest: "0.3.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/msmetaenhancer"
aliases:
 - "xml2-config.bak"
 - "tabulate"
 - "numba"
 - "pycc"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "normalizer"
 - "brotli"
versions:
 - "0.2.5--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for msmetaenhancer"
config: {"url": "https://biocontainers.pro/tools/msmetaenhancer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msmetaenhancer", "latest": {"0.3.0--pyhdfd78af_1": "sha256:ad0f66a8843b27e2fe027006ad7b23972857fceb26d47a1d5699fdecb2cb0ff2"}, "tags": {"0.2.5--pyhdfd78af_0": "sha256:ff09e6c18c69be623dae7a7063d3bf031ba0e7eea721be8eae918e282e74d48d", "0.3.0--pyhdfd78af_1": "sha256:ad0f66a8843b27e2fe027006ad7b23972857fceb26d47a1d5699fdecb2cb0ff2"}, "docker": "quay.io/biocontainers/msmetaenhancer", "aliases": {"xml2-config.bak": "/usr/local/bin/xml2-config.bak", "tabulate": "/usr/local/bin/tabulate", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "normalizer": "/usr/local/bin/normalizer", "brotli": "/usr/local/bin/brotli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msmetaenhancer.
shpc-registry automated BioContainers addition for msmetaenhancer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msmetaenhancer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msmetaenhancer:0.3.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msmetaenhancer/0.3.0--pyhdfd78af_1
$ module help quay.io/biocontainers/msmetaenhancer/0.3.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msmetaenhancer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msmetaenhancer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msmetaenhancer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msmetaenhancer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msmetaenhancer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msmetaenhancer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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