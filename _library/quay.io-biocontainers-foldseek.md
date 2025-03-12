---
layout: container
name:  "quay.io/biocontainers/foldseek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/foldseek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/foldseek/container.yaml"
updated_at: "2025-03-12 04:35:19.667997"
latest: "10.941cd33--h5021889_1"
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
 - "8.ef4e960--pl5321hb365157_0"
 - "7.04e0ec8--pl5321hb365157_0"
 - "8.ef4e960--pl5321hb365157_1"
 - "9.427df8a--pl5321hb365157_0"
 - "9.427df8a--pl5321hb365157_1"
 - "9.427df8a--pl5321h5021889_2"
 - "10.941cd33--h5021889_1"
description: "shpc-registry automated BioContainers addition for foldseek"
config: {"url": "https://biocontainers.pro/tools/foldseek", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for foldseek", "latest": {"10.941cd33--h5021889_1": "sha256:1156a052f31b2afb85257c02e83a962f559c9752273fe1064ab735f90ac29d1a"}, "tags": {"3.915ef7d--pl5321hf1761c0_1": "sha256:ad8a423b260403e5f95640f0d0e66e11ad36f566b1360dbb99f481f45f2a67c8", "4.645b789--pl5321hf1761c0_0": "sha256:623c1a171af801691fb80b37ad1f1e6c3adc68df24dc18428bf5b5247879eee9", "5.53465f0--pl5321hf1761c0_0": "sha256:176ee099aff34fdb1f333e74ef0ab5a50381a6e987f9018d0a81396d891651ad", "6.29e2557--pl5321hb365157_2": "sha256:05fc55c67452e37c8a631a6bd35d7e7039363dffd3d36bf6e5661385599da718", "8.ef4e960--pl5321hb365157_0": "sha256:56ce158f3250af68a1b5d69d93b0515d2ffb1e80321c6649fd87ae0010db3107", "7.04e0ec8--pl5321hb365157_0": "sha256:4aa710ded9127d0969a67acace515fe8337d1352700c3d889868433491eb72e9", "8.ef4e960--pl5321hb365157_1": "sha256:f194c34439f5110fa12d5fffdd8947a8d7c6f1a0b4761bb67ecd87e13656dcaa", "9.427df8a--pl5321hb365157_0": "sha256:3881cfb43da2a57fb6d9d5572962723e07c35060c6e63e83cba83de814e9d54d", "9.427df8a--pl5321hb365157_1": "sha256:c46d6fb854099780597e3adfa48e93c991f4b4d542391c144b9cae4de1ed22f9", "9.427df8a--pl5321h5021889_2": "sha256:a9ade9eacd4911cd13a0f4636d2ef70d5e5860d1707dc96f67dc5dffebcfaf64", "10.941cd33--h5021889_1": "sha256:1156a052f31b2afb85257c02e83a962f559c9752273fe1064ab735f90ac29d1a"}, "docker": "quay.io/biocontainers/foldseek", "aliases": {"aria2c": "/usr/local/bin/aria2c", "foldseek": "/usr/local/bin/foldseek", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/foldseek.
shpc-registry automated BioContainers addition for foldseek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/foldseek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/foldseek:10.941cd33--h5021889_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/foldseek/10.941cd33--h5021889_1
$ module help quay.io/biocontainers/foldseek/10.941cd33--h5021889_1
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