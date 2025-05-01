---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocsingular"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocsingular/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocsingular/container.yaml"
updated_at: "2025-05-01 07:00:12.393731"
latest: "1.22.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocsingular"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
 - "1.22.0--r44he5774e6_0"
 - "1.18.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-biocsingular"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocsingular", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocsingular", "latest": {"1.22.0--r44he5774e6_0": "sha256:08c652746690d5617760cbf5c709c6259b647d542f1ba7dc66d2cc8854e4fbf6"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:fd3b32f137b53bc0b80de3e228eb3b0ada7ed3b44874d2a758ea25c260400ce0", "1.14.0--r42hc247a5b_0": "sha256:7dc3c235d53c2d055e5e07b10dc34623ce34a9ee827d2c3eee76cc11761ea9ec", "1.10.0--r41hc247a5b_2": "sha256:3d886422d26b941dc8dd8a2294b82625400d32f54eeb09d65ce8a56ca2aadcbf", "1.14.0--r42hf17093f_1": "sha256:2a4e4d0870a1db91d93b9a4b628c075bb90893c952975496c4d86129bccc7c32", "1.16.0--r43hf17093f_0": "sha256:8b5f054675cc838b5547efe4cbf1a8997e64c32e83c6010613ae208b7f53067c", "1.18.0--r43hf17093f_0": "sha256:546e23c2c35519446a4692020eb8f70c5ef79f2b6372544c7f51406cd1751889", "1.22.0--r44he5774e6_0": "sha256:08c652746690d5617760cbf5c709c6259b647d542f1ba7dc66d2cc8854e4fbf6", "1.18.0--r43hf17093f_1": "sha256:028be9a62568e7a431f758e0269de3fcb31f60a1c1ba5dc6d160a2c48188a8ec"}, "docker": "quay.io/biocontainers/bioconductor-biocsingular", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocsingular.
shpc-registry automated BioContainers addition for bioconductor-biocsingular
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocsingular
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocsingular:1.22.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocsingular/1.22.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-biocsingular/1.22.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocsingular-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocsingular-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocsingular-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocsingular-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocsingular-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocsingular-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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