---
layout: container
name:  "quay.io/biocontainers/bioconductor-redisparam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-redisparam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-redisparam/container.yaml"
updated_at: "2024-09-18 03:10:51.883414"
latest: "1.4.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-redisparam"

versions:
 - "1.0.0--r42hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-redisparam"
config: {"url": "https://biocontainers.pro/tools/bioconductor-redisparam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-redisparam", "latest": {"1.4.0--r43hdfd78af_0": "sha256:40f6de79349064d707cf6b1fb1415da20150b146193f76c6e686504575245434"}, "tags": {"1.0.0--r42hdfd78af_0": "sha256:82fd94aeb5c4683d4c45306ddbe6ad179adf1f3640c76e9c7aa12c7c43686cec", "1.2.0--r43hdfd78af_0": "sha256:d660b14da32e54e846f17b10f0e68588b6b67631eb32e8769d23fa1adab46498", "1.4.0--r43hdfd78af_0": "sha256:40f6de79349064d707cf6b1fb1415da20150b146193f76c6e686504575245434"}, "docker": "quay.io/biocontainers/bioconductor-redisparam"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-redisparam.
singularity registry hpc automated addition for bioconductor-redisparam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-redisparam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-redisparam:1.4.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-redisparam/1.4.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-redisparam/1.4.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-redisparam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-redisparam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-redisparam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-redisparam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-redisparam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-redisparam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-redisparam

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