---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgsa/container.yaml"
updated_at: "2025-01-26 03:24:03.337159"
latest: "1.54.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mgsa"

versions:
 - "1.42.0--r41hc0cfd56_2"
 - "1.46.0--r42hc0cfd56_0"
 - "1.46.0--r42ha9d7317_2"
 - "1.48.0--r43ha9d7317_0"
 - "1.50.0--r43ha9d7317_1"
 - "1.50.0--r43ha9d7317_2"
 - "1.54.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mgsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgsa", "latest": {"1.54.0--r44h3df3fcb_0": "sha256:53f85a8888cb053bc275bfa2b20d380e03a286fbadc7b69fb864ceb3c15dfdcb"}, "tags": {"1.42.0--r41hc0cfd56_2": "sha256:77ee7abff41fe0c7248ea33a0f763b94ad2216a02a0767286a6753ababcc5445", "1.46.0--r42hc0cfd56_0": "sha256:d5f373c1c999a4ebecdb895c87e3d9dd5468e8f4d3f59b8c19eb97740ab6f0fd", "1.46.0--r42ha9d7317_2": "sha256:336933aca6099029f80d3c57057214efa42ba14b06b19147deb64a85ae9a64fa", "1.48.0--r43ha9d7317_0": "sha256:f85b970d65826b4f7b4a8715ae006ad0808858581b329281ca3485d063caf066", "1.50.0--r43ha9d7317_1": "sha256:c2c5e6ddcb95c04e8ba20d1a1d9099346d2b0439119b82b1701cb24f542f4290", "1.50.0--r43ha9d7317_2": "sha256:0950e9dfa4da9b5f177acceb6113803436229efb0ecd30839c392bc1fd117e2b", "1.54.0--r44h3df3fcb_0": "sha256:53f85a8888cb053bc275bfa2b20d380e03a286fbadc7b69fb864ceb3c15dfdcb"}, "docker": "quay.io/biocontainers/bioconductor-mgsa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgsa.
shpc-registry automated BioContainers addition for bioconductor-mgsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgsa:1.54.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgsa/1.54.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-mgsa/1.54.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgsa

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