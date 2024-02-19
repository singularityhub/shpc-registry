---
layout: container
name:  "quay.io/biocontainers/bioconductor-ipac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ipac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ipac/container.yaml"
updated_at: "2024-02-19 02:25:42.519180"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ipac"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ipac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ipac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ipac", "latest": {"1.46.0--r43hdfd78af_0": "sha256:4f87a6b0fa55717d838ceac45b7b8eeb0689cbf1688a1a9aa4e99e33e039ebd9"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:75c06f0dfd8a2286fac2180a514ddb55a1ee69bc8450ed5d798579b9f185c853", "1.42.0--r42hdfd78af_0": "sha256:3a5a199ed112284e011b7c7533ab4d83d2eb90018f5935a544e235685bc2f4b7", "1.44.0--r43hdfd78af_0": "sha256:4d3c8339dc9ef14ac90a7986085b4bd13128c1260b2003f5183fdc0302e94463", "1.46.0--r43hdfd78af_0": "sha256:4f87a6b0fa55717d838ceac45b7b8eeb0689cbf1688a1a9aa4e99e33e039ebd9"}, "docker": "quay.io/biocontainers/bioconductor-ipac"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ipac.
shpc-registry automated BioContainers addition for bioconductor-ipac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ipac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ipac:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ipac/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ipac/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ipac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ipac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ipac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ipac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ipac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ipac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ipac

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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