---
layout: container
name:  "quay.io/biocontainers/bioconductor-toast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-toast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-toast/container.yaml"
updated_at: "2025-09-09 03:25:23.794596"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-toast"

versions:
 - "1.7.1--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-toast"
config: {"url": "https://biocontainers.pro/tools/bioconductor-toast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-toast", "latest": {"1.20.0--r44hdfd78af_0": "sha256:7e39da14cf23b5a27a010d39b353c736747864683493cdce6fa24577dc9bc02d"}, "tags": {"1.7.1--r41hdfd78af_0": "sha256:b8ecf66124f6a42aeeb40f6d9125b9d60889e4e5d1011cf255f6d9686eb1b86c", "1.12.0--r42hdfd78af_0": "sha256:102812a304623a0f41c77e80f548a6f787c1d34ff36dccc83e1973e5c0af6745", "1.14.0--r43hdfd78af_0": "sha256:df18a50d14293f3327703cbb3d1770d642d07fc2e4ad4166de50a43324927b6f", "1.16.0--r43hdfd78af_0": "sha256:0c8600bb42b94cc1f18dde94bd63d00b0c43dac09ff94af9bdf96ae54cfb6629", "1.20.0--r44hdfd78af_0": "sha256:7e39da14cf23b5a27a010d39b353c736747864683493cdce6fa24577dc9bc02d"}, "docker": "quay.io/biocontainers/bioconductor-toast"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-toast.
shpc-registry automated BioContainers addition for bioconductor-toast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-toast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-toast:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-toast/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-toast/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-toast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-toast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-toast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-toast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-toast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-toast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-toast

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