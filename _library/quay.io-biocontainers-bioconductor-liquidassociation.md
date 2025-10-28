---
layout: container
name:  "quay.io/biocontainers/bioconductor-liquidassociation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-liquidassociation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-liquidassociation/container.yaml"
updated_at: "2025-10-28 03:32:12.675598"
latest: "1.60.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-liquidassociation"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
 - "1.60.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-liquidassociation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-liquidassociation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-liquidassociation", "latest": {"1.60.0--r44hdfd78af_0": "sha256:ca948560105eaad915c54723b7d5b1cda31e49a8654b5da42bf77c76f874817a"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:26e2244fea75d1b51d36f0fd1865869aa02d753247b6e50ed62a8d10bdccc6af", "1.52.0--r42hdfd78af_0": "sha256:ed8d8e94fb8077e67bfb657f953ead3a17b14973047353c1f6e1efc53ec9a7c1", "1.54.0--r43hdfd78af_0": "sha256:23ed225d2fc94ecd6cd1d80d47f3927053d292890b522e8157b566871230065d", "1.56.0--r43hdfd78af_0": "sha256:708c67c0e412c32b5253819d6c6d9a892c76542801489ced43de62e4adbe278e", "1.60.0--r44hdfd78af_0": "sha256:ca948560105eaad915c54723b7d5b1cda31e49a8654b5da42bf77c76f874817a"}, "docker": "quay.io/biocontainers/bioconductor-liquidassociation"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-liquidassociation.
shpc-registry automated BioContainers addition for bioconductor-liquidassociation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-liquidassociation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-liquidassociation:1.60.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-liquidassociation/1.60.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-liquidassociation/1.60.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-liquidassociation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-liquidassociation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-liquidassociation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-liquidassociation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-liquidassociation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-liquidassociation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-liquidassociation

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