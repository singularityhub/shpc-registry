---
layout: container
name:  "quay.io/biocontainers/bioconductor-adimpute"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adimpute/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adimpute/container.yaml"
updated_at: "2024-12-04 03:18:52.400509"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-adimpute"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-adimpute"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adimpute", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-adimpute", "latest": {"1.12.0--r43hdfd78af_0": "sha256:45f2c7599695002a536b1aeacc89c30c87ceb74bb70098f21d48016b9f42d386"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:ebcf5db69ec9401d810212cc32f7e584f4c76f70a5eb0394ea60beb61c1b5772", "1.8.0--r42hdfd78af_0": "sha256:5055a64eb040e9e13877a0e618edca610b8b0e32f7291f8907689d758cdaaf3a", "1.10.0--r43hdfd78af_0": "sha256:18cd4693bae530302ca45ce2b85c4bbfa22a6de3c738af297f7e3d670800fbcb", "1.12.0--r43hdfd78af_0": "sha256:45f2c7599695002a536b1aeacc89c30c87ceb74bb70098f21d48016b9f42d386"}, "docker": "quay.io/biocontainers/bioconductor-adimpute"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adimpute.
shpc-registry automated BioContainers addition for bioconductor-adimpute
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adimpute
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adimpute:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adimpute/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-adimpute/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adimpute-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adimpute-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adimpute-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adimpute-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adimpute-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adimpute-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-adimpute

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