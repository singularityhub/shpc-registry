---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotationfilter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotationfilter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotationfilter/container.yaml"
updated_at: "2024-01-22 02:54:53.413974"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotationfilter"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotationfilter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotationfilter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotationfilter", "latest": {"1.26.0--r43hdfd78af_0": "sha256:412d55e1074340cb5dc8dafd237e4b64e4683d882673586410543290432b7cf3"}, "tags": {"1.8.0--r36_1": "sha256:60902f3ca3ca936238033978957d4c579fc4a2d1ee7669752efab9bf6c3e8c5b", "1.22.0--r42hdfd78af_0": "sha256:99aa0f2334803c8ee3f8a459560817c3d15c096d2314529954e736d00ae09be3", "1.18.0--r41hdfd78af_0": "sha256:c0bf5695a813999e61488594616dee63357c4759301a4b0603fa105ca37b759c", "1.16.0--r41hdfd78af_0": "sha256:692f331601b69c8ba09e7def0f8bbc68f6c0d5b825539c49a95736d3093e31a3", "1.14.0--r40hdfd78af_1": "sha256:bb9b0eb36882a787c410b4a13ba9736fe74356bc2e1c049d4d45231ad2269b7c", "1.12.0--r40_0": "sha256:28add3b1bef84f99278a91494ead6beb5a0b37dde973474db8ac2f2eba78e454", "1.24.0--r43hdfd78af_0": "sha256:bc00c3478eac233ae21c60240974eea52ccc06d7fe6d1445c925588b94c4411b", "1.26.0--r43hdfd78af_0": "sha256:412d55e1074340cb5dc8dafd237e4b64e4683d882673586410543290432b7cf3"}, "docker": "quay.io/biocontainers/bioconductor-annotationfilter", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotationfilter.
shpc-registry automated BioContainers addition for bioconductor-annotationfilter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationfilter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationfilter:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotationfilter/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotationfilter/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotationfilter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationfilter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationfilter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotationfilter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotationfilter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotationfilter-inspect-deffile:

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