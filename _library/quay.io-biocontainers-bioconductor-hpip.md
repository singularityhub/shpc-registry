---
layout: container
name:  "quay.io/biocontainers/bioconductor-hpip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hpip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hpip/container.yaml"
updated_at: "2023-12-15 02:44:54.182010"
latest: "1.8.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-hpip"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-hpip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hpip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hpip", "latest": {"1.8.0--r43hdfd78af_1": "sha256:f9cdc8eb808c3dd93043cb0237c375cfe1e68787deea3d8dfbe6764fe1f296fc"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:87fb2ee592f4529e845ed87f875796adccba43e759ed026eb92f175355c098d8", "1.4.0--r42hdfd78af_0": "sha256:e2662573bd49e0962493c12c8ed04061f1508eb8ef4d1474653d805c1686748c", "1.6.0--r43hdfd78af_0": "sha256:ad01e4a7d60600ed11f2b84adf21846a8639e587501ffa3161a17876d20b0488", "1.8.0--r43hdfd78af_1": "sha256:f9cdc8eb808c3dd93043cb0237c375cfe1e68787deea3d8dfbe6764fe1f296fc"}, "docker": "quay.io/biocontainers/bioconductor-hpip"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hpip.
shpc-registry automated BioContainers addition for bioconductor-hpip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hpip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hpip:1.8.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hpip/1.8.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-hpip/1.8.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hpip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hpip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hpip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hpip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hpip

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