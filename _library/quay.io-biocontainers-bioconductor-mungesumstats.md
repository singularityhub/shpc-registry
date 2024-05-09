---
layout: container
name:  "quay.io/biocontainers/bioconductor-mungesumstats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mungesumstats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mungesumstats/container.yaml"
updated_at: "2024-05-09 02:55:56.435227"
latest: "1.10.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mungesumstats"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mungesumstats"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mungesumstats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mungesumstats", "latest": {"1.10.1--r43hdfd78af_0": "sha256:f2bb0b529d075c74af43bc6b057f9e2c4033875aa98e562615993515b2f5d30a"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:79722dfe89d3b50e2e9724ddea2081e92987efc639fc0cde3e13b8a1ec97a37e", "1.6.0--r42hdfd78af_0": "sha256:faac0a85cf15ade332731bd268e1a518cf55fcc3a8980e0aa662b6d0945e6afe", "1.8.0--r43hdfd78af_0": "sha256:bde640e67410b891afc0e900633107ec7cf51148b200de9323429505bd7f1e4d", "1.10.1--r43hdfd78af_0": "sha256:f2bb0b529d075c74af43bc6b057f9e2c4033875aa98e562615993515b2f5d30a"}, "docker": "quay.io/biocontainers/bioconductor-mungesumstats"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mungesumstats.
shpc-registry automated BioContainers addition for bioconductor-mungesumstats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mungesumstats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mungesumstats:1.10.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mungesumstats/1.10.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mungesumstats/1.10.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mungesumstats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mungesumstats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mungesumstats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mungesumstats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mungesumstats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mungesumstats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mungesumstats

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