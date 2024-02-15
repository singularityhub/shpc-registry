---
layout: container
name:  "quay.io/biocontainers/bioconductor-gagedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gagedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gagedata/container.yaml"
updated_at: "2024-02-15 02:25:09.590398"
latest: "2.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gagedata"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
versions:
 - "2.8.0--0"
 - "2.35.0--r42hdfd78af_0"
 - "2.32.0--r41hdfd78af_1"
 - "2.30.0--r41hdfd78af_0"
 - "2.28.0--r40hdfd78af_1"
 - "2.27.0--r40_0"
 - "2.38.0--r43hdfd78af_0"
 - "2.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gagedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gagedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gagedata", "latest": {"2.40.0--r43hdfd78af_0": "sha256:1d319e4fa85ee9dc4c3bebf5950d1eea909475a57d07be138aa7003cfb4ad677"}, "tags": {"2.8.0--0": "sha256:6e15c94d5329670cf4676464a4cf33b50ce04df9536e60a1c6cc1dc28e5a7f0d", "2.35.0--r42hdfd78af_0": "sha256:308f061585483671949736e9fccfc24857f9e1a744657e3911db504ee9b6de3e", "2.32.0--r41hdfd78af_1": "sha256:f1c8463b7a3c1fe51a18ad8441fc59a10d812660b4b94421d8b9220f6ed24eae", "2.30.0--r41hdfd78af_0": "sha256:5f4cef48ea8184e2d4c08c8b5a87f863190d65bbd378e46afe408e8c330df9b1", "2.28.0--r40hdfd78af_1": "sha256:914993679a01b14a4150698872b5a6bf8dfedf7f4a29380b9dc4a1531acfb8fb", "2.27.0--r40_0": "sha256:339b43010905a63c8a9f4a8d64d8f41bc50d4ac0daa9951db7293941ef8840a9", "2.38.0--r43hdfd78af_0": "sha256:7d1dfd1b1da44c18c78a2cc2ca388260a315761816033943e3fff9f912d4948c", "2.40.0--r43hdfd78af_0": "sha256:1d319e4fa85ee9dc4c3bebf5950d1eea909475a57d07be138aa7003cfb4ad677"}, "docker": "quay.io/biocontainers/bioconductor-gagedata", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gagedata.
shpc-registry automated BioContainers addition for bioconductor-gagedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gagedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gagedata:2.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gagedata/2.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gagedata/2.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gagedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gagedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gagedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gagedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gagedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gagedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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