---
layout: container
name:  "quay.io/biocontainers/bioconductor-dyebias"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dyebias/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dyebias/container.yaml"
updated_at: "2025-02-10 03:20:45.598086"
latest: "1.66.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dyebias"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.66.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dyebias"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dyebias", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dyebias", "latest": {"1.66.0--r44hdfd78af_0": "sha256:8afe9039e4c9f1c9a93a00e7ada66484bcfcfde735c8f8df7e2942398afddb8d"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:877bf3671d81b59e05891bfab1f859b1ec8944b7d74678743ea466d3815e0d0b", "1.58.0--r42hdfd78af_0": "sha256:775b50fe6342cc43b083f6190ed5f3e911e0287eff7b23e45e55f28b3eb83a7a", "1.60.0--r43hdfd78af_0": "sha256:f7e6a6858a28d77e99fdeda47bdbc7b29670a837f9c3ff55aa90ebb76ce68d08", "1.62.0--r43hdfd78af_0": "sha256:b8c27e2346bad4287e38923c2a8e13016b301d52a0316fb3b0b4b6f0ac1956fb", "1.66.0--r44hdfd78af_0": "sha256:8afe9039e4c9f1c9a93a00e7ada66484bcfcfde735c8f8df7e2942398afddb8d"}, "docker": "quay.io/biocontainers/bioconductor-dyebias"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dyebias.
shpc-registry automated BioContainers addition for bioconductor-dyebias
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dyebias
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dyebias:1.66.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dyebias/1.66.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dyebias/1.66.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dyebias-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dyebias-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dyebias-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dyebias-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dyebias-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dyebias-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dyebias

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