---
layout: container
name:  "quay.io/biocontainers/bioconductor-mistyr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mistyr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mistyr/container.yaml"
updated_at: "2025-01-06 03:06:28.152889"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mistyr"

versions:
 - "1.2.1--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.1--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mistyr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mistyr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mistyr", "latest": {"1.14.0--r44hdfd78af_0": "sha256:186b936e8565f114b713b1fc6d19c28f8b106a3912ce7bb77f0df8bb4153ccc9"}, "tags": {"1.2.1--r41hdfd78af_0": "sha256:ae248d9375fb86567d69517564f582f5fbfe8b6e63d6765ec6c55a3219f12f84", "1.6.0--r42hdfd78af_0": "sha256:b43781c084cacbbd642afe2318215e746648c73e1ac2eeb512ce2b941422127d", "1.8.1--r43hdfd78af_0": "sha256:5672413f6a76073184f8cd3680f58565d7450e7d53a6d021c451971097075bdd", "1.10.0--r43hdfd78af_0": "sha256:a54af6444b65b9ec172fdd6e9ba6736fcb3468f333b6bf2a99f4bebe564c082e", "1.14.0--r44hdfd78af_0": "sha256:186b936e8565f114b713b1fc6d19c28f8b106a3912ce7bb77f0df8bb4153ccc9"}, "docker": "quay.io/biocontainers/bioconductor-mistyr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mistyr.
shpc-registry automated BioContainers addition for bioconductor-mistyr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mistyr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mistyr:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mistyr/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mistyr/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mistyr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mistyr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mistyr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mistyr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mistyr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mistyr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mistyr

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