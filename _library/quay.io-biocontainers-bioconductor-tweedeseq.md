---
layout: container
name:  "quay.io/biocontainers/bioconductor-tweedeseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tweedeseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tweedeseq/container.yaml"
updated_at: "2025-10-24 03:03:44.233800"
latest: "1.52.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-tweedeseq"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
 - "1.44.0--r42ha9d7317_1"
 - "1.45.0--r43ha9d7317_0"
 - "1.48.0--r43hf17093f_0"
 - "1.52.0--r44he5774e6_0"
 - "1.52.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-tweedeseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tweedeseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tweedeseq", "latest": {"1.52.0--r44he5774e6_1": "sha256:ddec42f82031c9a43724c16816b4bb3ba28080774cf60c5712a95e2f67bab06b"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:9aa59a4cdef737f593ece0e64dda88b085be1fc76c3a044e07bbb813e33b09ac", "1.44.0--r42hc0cfd56_0": "sha256:916c91388562e6f6b8d6affc01e1f1723d53640a7b0a17d879b5e971a54cbefc", "1.44.0--r42ha9d7317_1": "sha256:8f7a7df1156e766eadfe19fda93c6ec6e1506d1a12ee79e1c3963f399b112729", "1.45.0--r43ha9d7317_0": "sha256:f540222543593c4f72dc00751a2b545e19195a8951187a1b906557402e827e4e", "1.48.0--r43hf17093f_0": "sha256:dd8585974849a0b5bfc891105a46f8b6a8d01dfecc66b6271e447f293f845a0e", "1.52.0--r44he5774e6_0": "sha256:a83ca07f26e94b07038c85e78490dcbda69e024a9c4b64cf2f62bce9f829d1f7", "1.52.0--r44he5774e6_1": "sha256:ddec42f82031c9a43724c16816b4bb3ba28080774cf60c5712a95e2f67bab06b"}, "docker": "quay.io/biocontainers/bioconductor-tweedeseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tweedeseq.
shpc-registry automated BioContainers addition for bioconductor-tweedeseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tweedeseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tweedeseq:1.52.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tweedeseq/1.52.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-tweedeseq/1.52.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tweedeseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tweedeseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tweedeseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tweedeseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tweedeseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tweedeseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tweedeseq

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