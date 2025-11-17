---
layout: container
name:  "quay.io/biocontainers/bioconductor-xenopuslaevisprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xenopuslaevisprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xenopuslaevisprobe/container.yaml"
updated_at: "2025-11-17 05:00:55.551552"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-xenopuslaevisprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-xenopuslaevisprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xenopuslaevisprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xenopuslaevisprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:923dae5e4d59bf82b11f2f7020b8729db500b6d0dfae8cdc8d6adea7aefd1962"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f9faa56d8cbe16832e6da8c3e0d98982984685e61f1cb395e779eadac66c355f", "2.18.0--r42hdfd78af_10": "sha256:6c1e92c8b2f14785bcf23039b0be889d93fa36dd939fac3c2aec0863493bf568", "2.18.0--r43hdfd78af_11": "sha256:40a91c9d0824258cc70a65a9a123b56b89fb73100a3a65061748e5fc7c18cc95", "2.18.0--r43hdfd78af_12": "sha256:b86610994213746843c986257fb495194fdca434b1b8ca879e1b43b4377afe5b", "2.18.0--r44hdfd78af_13": "sha256:923dae5e4d59bf82b11f2f7020b8729db500b6d0dfae8cdc8d6adea7aefd1962"}, "docker": "quay.io/biocontainers/bioconductor-xenopuslaevisprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xenopuslaevisprobe.
shpc-registry automated BioContainers addition for bioconductor-xenopuslaevisprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xenopuslaevisprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xenopuslaevisprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xenopuslaevisprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-xenopuslaevisprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xenopuslaevisprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xenopuslaevisprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xenopuslaevisprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xenopuslaevisprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xenopuslaevisprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xenopuslaevisprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xenopuslaevisprobe

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