---
layout: container
name:  "quay.io/biocontainers/foldseek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/foldseek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/foldseek/container.yaml"
updated_at: "2023-09-11 03:26:48.947330"
latest: "6.29e2557--pl5321hb365157_2"
container_url: "https://biocontainers.pro/tools/foldseek"
aliases:
 - "aria2c"
 - "foldseek"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "idn2"
 - "wget"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.915ef7d--pl5321hf1761c0_1"
 - "4.645b789--pl5321hf1761c0_0"
 - "5.53465f0--pl5321hf1761c0_0"
 - "6.29e2557--pl5321hb365157_2"
description: "shpc-registry automated BioContainers addition for foldseek"
config: {"url": "https://biocontainers.pro/tools/foldseek", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for foldseek", "latest": {"6.29e2557--pl5321hb365157_2": "sha256:05fc55c67452e37c8a631a6bd35d7e7039363dffd3d36bf6e5661385599da718"}, "tags": {"3.915ef7d--pl5321hf1761c0_1": "sha256:ad8a423b260403e5f95640f0d0e66e11ad36f566b1360dbb99f481f45f2a67c8", "4.645b789--pl5321hf1761c0_0": "sha256:623c1a171af801691fb80b37ad1f1e6c3adc68df24dc18428bf5b5247879eee9", "5.53465f0--pl5321hf1761c0_0": "sha256:176ee099aff34fdb1f333e74ef0ab5a50381a6e987f9018d0a81396d891651ad", "6.29e2557--pl5321hb365157_2": "sha256:05fc55c67452e37c8a631a6bd35d7e7039363dffd3d36bf6e5661385599da718"}, "docker": "quay.io/biocontainers/foldseek", "aliases": {"aria2c": "/usr/local/bin/aria2c", "foldseek": "/usr/local/bin/foldseek", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/foldseek.
shpc-registry automated BioContainers addition for foldseek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/foldseek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/foldseek:6.29e2557--pl5321hb365157_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/foldseek/6.29e2557--pl5321hb365157_2
$ module help quay.io/biocontainers/foldseek/6.29e2557--pl5321hb365157_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### foldseek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### foldseek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### foldseek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### foldseek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### foldseek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### foldseek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### foldseek

```bash
$ singularity exec <container> /usr/local/bin/foldseek
$ podman run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
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