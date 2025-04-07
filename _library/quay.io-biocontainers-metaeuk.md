---
layout: container
name:  "quay.io/biocontainers/metaeuk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaeuk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaeuk/container.yaml"
updated_at: "2025-04-07 03:10:18.925445"
latest: "7.bba0d80--pl5321hd6d6fdc_2"
container_url: "https://biocontainers.pro/tools/metaeuk"
aliases:
 - "metaeuk"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "idn2"
 - "wget"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "6.a5d39d9--pl5321hf1761c0_1"
 - "6.a5d39d9--pl5321h6a68c12_3"
 - "6.a5d39d9--pl5321h6a68c12_4"
 - "7.bba0d80--pl5321h6a68c12_0"
 - "7.bba0d80--pl5321h6a68c12_1"
 - "7.bba0d80--pl5321hd6d6fdc_2"
description: "shpc-registry automated BioContainers addition for metaeuk"
config: {"url": "https://biocontainers.pro/tools/metaeuk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaeuk", "latest": {"7.bba0d80--pl5321hd6d6fdc_2": "sha256:cb600386d864b6e1c8bd34d6c8f274d96088c47c3e7389e805bb16964ac855d0"}, "tags": {"6.a5d39d9--pl5321hf1761c0_1": "sha256:2b31f6eb87329e0b6bb738af94aa7bc12e75ca2a4451904596abbb1d0bf935d6", "6.a5d39d9--pl5321h6a68c12_3": "sha256:747073d0d621f9994db023426d4837779d4d42152b292d92fc1eafe2c9ad5a96", "6.a5d39d9--pl5321h6a68c12_4": "sha256:43f9a970450d4299e440226b30cafb42a5038244a8cf72c2b30114f774750ded", "7.bba0d80--pl5321h6a68c12_0": "sha256:4c8a1d734eab07da34b1564f1a30fe731b679c9af0f0180d5166b1e6a278b9c7", "7.bba0d80--pl5321h6a68c12_1": "sha256:b8bee285b855f553b29cae5d082bf3ce0ce81d3ad54c1cace9ced0dcfb9c4b88", "7.bba0d80--pl5321hd6d6fdc_2": "sha256:cb600386d864b6e1c8bd34d6c8f274d96088c47c3e7389e805bb16964ac855d0"}, "docker": "quay.io/biocontainers/metaeuk", "aliases": {"metaeuk": "/usr/local/bin/metaeuk", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaeuk.
shpc-registry automated BioContainers addition for metaeuk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaeuk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaeuk:7.bba0d80--pl5321hd6d6fdc_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaeuk/7.bba0d80--pl5321hd6d6fdc_2
$ module help quay.io/biocontainers/metaeuk/7.bba0d80--pl5321hd6d6fdc_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaeuk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaeuk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaeuk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaeuk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaeuk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaeuk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metaeuk

```bash
$ singularity exec <container> /usr/local/bin/metaeuk
$ podman run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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