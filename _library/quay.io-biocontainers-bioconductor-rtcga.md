---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtcga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtcga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtcga/container.yaml"
updated_at: "2023-09-03 02:35:50.421563"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtcga"

versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtcga"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtcga", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtcga", "latest": {"1.30.0--r43hdfd78af_0": "sha256:f4da8d42a0a256e0c1801ad517b759f10909d3506afd8adfe9ecefc2f0db20c0"}, "tags": {"1.8.0--r3.4.1_0": "sha256:9112f7e515219ae9880c37a814efe3cb5b6a3dd4cd4f359350f87aedce00a13a", "1.28.0--r42hdfd78af_0": "sha256:1d7aecbad268cc044be332dae77a14b4f5735e60aa1d2a03fc71e56a46df2c9c", "1.24.0--r41hdfd78af_0": "sha256:7bf1c140f44f03a94b9841ed6b939f4ed36e4a8c90ee02362946d7966d984b16", "1.22.0--r41hdfd78af_0": "sha256:ea2aec50ec18dd84152139eb22ea566ce97a02ef767bc46bbe496e57614f7de1", "1.20.0--r40hdfd78af_1": "sha256:892f16cd2623fc99f7a2fa1a5e58d1cfe9faa345cd33d63bf0413962b977dfd4", "1.18.0--r40_0": "sha256:b44dfe37164a920fd72c115b38eb4bbf07dd3f77ce9c5774a644a04bf70d1b1d", "1.30.0--r43hdfd78af_0": "sha256:f4da8d42a0a256e0c1801ad517b759f10909d3506afd8adfe9ecefc2f0db20c0"}, "docker": "quay.io/biocontainers/bioconductor-rtcga"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtcga.
shpc-registry automated BioContainers addition for bioconductor-rtcga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtcga/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtcga/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtcga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtcga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtcga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtcga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtcga

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