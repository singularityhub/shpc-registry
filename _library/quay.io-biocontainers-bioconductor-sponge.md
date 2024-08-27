---
layout: container
name:  "quay.io/biocontainers/bioconductor-sponge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sponge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sponge/container.yaml"
updated_at: "2024-08-27 03:13:25.142733"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sponge"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sponge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sponge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sponge", "latest": {"1.22.0--r43hdfd78af_0": "sha256:855f5a42415faaf80e8508e2d824f54b04b4248f4a4665ab1196cb1f296904fe"}, "tags": {"1.8.0--r36_0": "sha256:4e1bdce1cef1c3a86b4aed341602eb854b8fd4cf91c0b99d7899b33303fe792d", "1.20.0--r42hdfd78af_0": "sha256:478112962ee576e576043b164e0917d7c057bbce46a0dff95c976b75838fd0cc", "1.16.0--r41hdfd78af_0": "sha256:55e0e0c3aa2bd8528ee98232534197e8bb578972b1727f380b6b56f1084d10ab", "1.14.0--r41hdfd78af_0": "sha256:2c532b9b6dc170ebf03594cb2312d51107ae54d1580dd159fd1605126694cb47", "1.12.0--r40hdfd78af_1": "sha256:0257ede206c8810fe85593de4a7dc299f45fce83561ce6c35abdf8494adc1645", "1.10.0--r40_0": "sha256:0019b3aa6f74c6cc264695b63720bc68c7501c338f84875d24700f8632a68206", "1.22.0--r43hdfd78af_0": "sha256:855f5a42415faaf80e8508e2d824f54b04b4248f4a4665ab1196cb1f296904fe"}, "docker": "quay.io/biocontainers/bioconductor-sponge", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sponge.
shpc-registry automated BioContainers addition for bioconductor-sponge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sponge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sponge:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sponge/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sponge/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sponge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sponge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sponge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sponge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sponge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sponge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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