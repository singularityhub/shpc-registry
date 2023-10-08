---
layout: container
name:  "quay.io/biocontainers/bioconductor-phenstat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phenstat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phenstat/container.yaml"
updated_at: "2023-10-08 02:28:37.875707"
latest: "2.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phenstat"

versions:
 - "2.30.0--r41hdfd78af_0"
 - "2.34.0--r42hdfd78af_0"
 - "2.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phenstat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phenstat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phenstat", "latest": {"2.36.0--r43hdfd78af_0": "sha256:58bc0a1592ce1baa0a70e7f34e4505b7fac9046e4d786a400162c2e6fe715003"}, "tags": {"2.30.0--r41hdfd78af_0": "sha256:3a8d3d094c1f9f9fe74641d893511151e08b8df783c226920299d01f888a7604", "2.34.0--r42hdfd78af_0": "sha256:1c2f5389693a8a84ab0e2b02907dd99a0748ff836cf80a9f21fac1d1d0da5d56", "2.36.0--r43hdfd78af_0": "sha256:58bc0a1592ce1baa0a70e7f34e4505b7fac9046e4d786a400162c2e6fe715003"}, "docker": "quay.io/biocontainers/bioconductor-phenstat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phenstat.
shpc-registry automated BioContainers addition for bioconductor-phenstat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phenstat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phenstat:2.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phenstat/2.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phenstat/2.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phenstat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenstat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenstat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phenstat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phenstat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phenstat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phenstat

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