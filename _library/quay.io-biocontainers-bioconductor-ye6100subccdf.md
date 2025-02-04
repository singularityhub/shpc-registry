---
layout: container
name:  "quay.io/biocontainers/bioconductor-ye6100subccdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ye6100subccdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ye6100subccdf/container.yaml"
updated_at: "2025-02-04 03:15:07.018479"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-ye6100subccdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-ye6100subccdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ye6100subccdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ye6100subccdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:920cf50844f775ec53e48909eb3703df270d0eb559854bd330becfb508791297"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:b2877bf2b0223d6313952c615c71d2286a1c033c3d3212dac71e94f7d9e02246", "2.18.0--r42hdfd78af_10": "sha256:6eee67b2699b6325abffff588acfc3a8c38a68ee54a456c071087d7a5f8d24b6", "2.18.0--r43hdfd78af_11": "sha256:9211aff6327522476f9400dc26692316261a92454baa04a9df0bf7f991370f1d", "2.18.0--r43hdfd78af_12": "sha256:3778039d2e7adc7402f65dbae768f40935dcce09198e4a6500803ba3cc34a592", "2.18.0--r44hdfd78af_13": "sha256:920cf50844f775ec53e48909eb3703df270d0eb559854bd330becfb508791297"}, "docker": "quay.io/biocontainers/bioconductor-ye6100subccdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ye6100subccdf.
shpc-registry automated BioContainers addition for bioconductor-ye6100subccdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ye6100subccdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ye6100subccdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ye6100subccdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-ye6100subccdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ye6100subccdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ye6100subccdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ye6100subccdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ye6100subccdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ye6100subccdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ye6100subccdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ye6100subccdf

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