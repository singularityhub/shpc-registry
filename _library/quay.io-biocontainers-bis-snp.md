---
layout: container
name:  "quay.io/biocontainers/bis-snp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bis-snp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bis-snp/container.yaml"
updated_at: "2024-10-06 03:35:32.674236"
latest: "1.0.1--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bis-snp"

versions:
 - "1.0.1--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bis-snp"
config: {"url": "https://biocontainers.pro/tools/bis-snp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bis-snp", "latest": {"1.0.1--hdfd78af_3": "sha256:b9d9f81f78209bcc25d9ab2dc13712c0acb6e4cd5b777eb64ded1371f3af8157"}, "tags": {"1.0.1--hdfd78af_3": "sha256:b9d9f81f78209bcc25d9ab2dc13712c0acb6e4cd5b777eb64ded1371f3af8157"}, "docker": "quay.io/biocontainers/bis-snp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bis-snp.
shpc-registry automated BioContainers addition for bis-snp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bis-snp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bis-snp:1.0.1--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bis-snp/1.0.1--hdfd78af_3
$ module help quay.io/biocontainers/bis-snp/1.0.1--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bis-snp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bis-snp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bis-snp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bis-snp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bis-snp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bis-snp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bis-snp

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