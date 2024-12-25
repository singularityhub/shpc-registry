---
layout: container
name:  "quay.io/biocontainers/bwa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bwa/container.yaml"
updated_at: "2024-12-25 03:05:51.381301"
latest: "0.7.18--h577a1d6_2"
container_url: "https://biocontainers.pro/tools/bwa"
aliases:
 - "bwa"
versions:
 - "0.7.17--h7132678_9"
 - "0.7.17--h7132678_10"
 - "0.7.17--he4a0461_11"
 - "0.7.18--he4a0461_0"
 - "0.7.18--he4a0461_1"
 - "0.7.18--h577a1d6_2"
description: "shpc-registry automated BioContainers addition for bwa"
config: {"url": "https://biocontainers.pro/tools/bwa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bwa", "latest": {"0.7.18--h577a1d6_2": "sha256:c5d0c7ca366aa58f479e01f50cc99c35b6707c7e6d87fb919e7cd03a21ff4e89"}, "tags": {"0.7.17--h7132678_9": "sha256:07822e4293a8c59755b295c448b9541db6c9bdbfdedb010bdbdcc1e1e935370f", "0.7.17--h7132678_10": "sha256:f9063141d8c5da87da76392b3a152b927b2913d47373f1874d76f14634b3f684", "0.7.17--he4a0461_11": "sha256:652ca694adcb54ca799c22b843c086d570875ef14334a90ffeab0e1beb5f5741", "0.7.18--he4a0461_0": "sha256:a8ea7d74457b55395e35f1e4200e3ac4a44e3f7c4b361d7628da86cec2133e03", "0.7.18--he4a0461_1": "sha256:239581ff47177f05f40d82709cf4bb9f0b391a729e1e299b82c6516f04cb69a4", "0.7.18--h577a1d6_2": "sha256:c5d0c7ca366aa58f479e01f50cc99c35b6707c7e6d87fb919e7cd03a21ff4e89"}, "docker": "quay.io/biocontainers/bwa", "aliases": {"bwa": "/usr/local/bin/bwa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwa.
shpc-registry automated BioContainers addition for bwa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwa:0.7.18--h577a1d6_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwa/0.7.18--h577a1d6_2
$ module help quay.io/biocontainers/bwa/0.7.18--h577a1d6_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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