---
layout: container
name:  "quay.io/biocontainers/bioconductor-clusterstab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clusterstab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clusterstab/container.yaml"
updated_at: "2024-08-02 03:07:54.596476"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clusterstab"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clusterstab"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clusterstab", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clusterstab", "latest": {"1.74.0--r43hdfd78af_0": "sha256:4871565c505f79dc7c4144184cb04dec2f12d55ab5e2e9e2b0e2340c989cbf2d"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:500f3a29035eb0fb305838fb8d0cf2eea3d45f36c12012e46e436a0b55b9f9de", "1.70.0--r42hdfd78af_0": "sha256:883cbe94302238d5aeae8a5c51abf29bde5ca10050e159206f95e7c91cc5e681", "1.72.0--r43hdfd78af_0": "sha256:69f41cf78c8e328af4ae750125753056742993d6c3e92a1e61f1684c71d644d5", "1.74.0--r43hdfd78af_0": "sha256:4871565c505f79dc7c4144184cb04dec2f12d55ab5e2e9e2b0e2340c989cbf2d"}, "docker": "quay.io/biocontainers/bioconductor-clusterstab"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clusterstab.
shpc-registry automated BioContainers addition for bioconductor-clusterstab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clusterstab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clusterstab:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clusterstab/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clusterstab/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clusterstab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clusterstab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clusterstab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clusterstab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clusterstab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clusterstab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clusterstab

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