---
layout: container
name:  "quay.io/biocontainers/bioconductor-rdrtoolbox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rdrtoolbox/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rdrtoolbox/container.yaml"
updated_at: "2025-04-09 03:23:04.184070"
latest: "1.56.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rdrtoolbox"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.48.0--r42hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.56.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rdrtoolbox"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rdrtoolbox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rdrtoolbox", "latest": {"1.56.0--r44hdfd78af_0": "sha256:d49d44630e7695b1bb163c24d3ec0825c48e06983d3678d44de9c9db809536ef"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:e7722b9ad7a03f80bbd55e2248af3c88bfec8a1ce10ee7fb0e2e6f6bd1495fdb", "1.48.0--r42hdfd78af_0": "sha256:5857aa904960b6f4c7c07b3a903c48830dfdc5642ab6fde688a58602d2904bf8", "1.50.0--r43hdfd78af_0": "sha256:742b5f14b747638421abd57796e66c139eff4bfb59e9be0415c06e7fc6adda97", "1.52.0--r43hdfd78af_0": "sha256:b995ede360fad7e3bc2231958b38e70ae1263d24b1427420cd44c8832de9812c", "1.56.0--r44hdfd78af_0": "sha256:d49d44630e7695b1bb163c24d3ec0825c48e06983d3678d44de9c9db809536ef"}, "docker": "quay.io/biocontainers/bioconductor-rdrtoolbox"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rdrtoolbox.
shpc-registry automated BioContainers addition for bioconductor-rdrtoolbox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rdrtoolbox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rdrtoolbox:1.56.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rdrtoolbox/1.56.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rdrtoolbox/1.56.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rdrtoolbox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdrtoolbox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdrtoolbox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rdrtoolbox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rdrtoolbox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rdrtoolbox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rdrtoolbox

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