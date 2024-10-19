---
layout: container
name:  "quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm/container.yaml"
updated_at: "2024-10-19 03:04:36.760130"
latest: "1.0.1--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-humanomniexpress12v1bcrlmm"

versions:
 - "1.0.1--r41hdfd78af_9"
 - "1.0.1--r42hdfd78af_10"
 - "1.0.1--r43hdfd78af_11"
 - "1.0.1--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-humanomniexpress12v1bcrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-humanomniexpress12v1bcrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-humanomniexpress12v1bcrlmm", "latest": {"1.0.1--r43hdfd78af_12": "sha256:9db7a67fc864f2f4c4de81c0545d52408722edaf578c5b34fe0a379de7b1767f"}, "tags": {"1.0.1--r41hdfd78af_9": "sha256:6cfe710eea97cd806b759559e8244a41e7f478ae6d0a5564fd83f960cb2613bd", "1.0.1--r42hdfd78af_10": "sha256:6468c9735195f0d48696edefe7e537eb2abb1e428ade2206211cfc0a8d682498", "1.0.1--r43hdfd78af_11": "sha256:ecd632b24e943698363b79e460ec7f92e52742b5f0672954d63dbc89b0bfa8f6", "1.0.1--r43hdfd78af_12": "sha256:9db7a67fc864f2f4c4de81c0545d52408722edaf578c5b34fe0a379de7b1767f"}, "docker": "quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm.
shpc-registry automated BioContainers addition for bioconductor-humanomniexpress12v1bcrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm:1.0.1--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm/1.0.1--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-humanomniexpress12v1bcrlmm/1.0.1--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-humanomniexpress12v1bcrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanomniexpress12v1bcrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanomniexpress12v1bcrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-humanomniexpress12v1bcrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-humanomniexpress12v1bcrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-humanomniexpress12v1bcrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-humanomniexpress12v1bcrlmm

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