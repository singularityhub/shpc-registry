---
layout: container
name:  "quay.io/biocontainers/bioconductor-medips"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-medips/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-medips/container.yaml"
updated_at: "2024-07-18 03:17:37.248547"
latest: "1.54.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-medips"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-medips"
config: {"url": "https://biocontainers.pro/tools/bioconductor-medips", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-medips", "latest": {"1.54.0--r43hdfd78af_0": "sha256:ba1a76b35f81cf56e0285d3a44329ac36103f6acc3e3736ee9fa044c7e8ccc0c"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:1cd519b5d9eaeb00b5c881a673eded5c1e548fa6f56778eab2a52bba0419fed4", "1.50.0--r42hdfd78af_0": "sha256:ba535c79577d626ef19af1dd699eb6d6903088c3862a727a4f7e36a7fd3c246a", "1.52.0--r43hdfd78af_0": "sha256:8985fbbf898b0e1fcd1083f4f0981904a3d7520d519f5f4a92d945a122acc7ce", "1.54.0--r43hdfd78af_0": "sha256:ba1a76b35f81cf56e0285d3a44329ac36103f6acc3e3736ee9fa044c7e8ccc0c"}, "docker": "quay.io/biocontainers/bioconductor-medips"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-medips.
shpc-registry automated BioContainers addition for bioconductor-medips
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-medips
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-medips:1.54.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-medips/1.54.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-medips/1.54.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-medips-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-medips-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-medips-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-medips-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-medips-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-medips-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-medips

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