---
layout: container
name:  "quay.io/biocontainers/bioconductor-stjudem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-stjudem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-stjudem/container.yaml"
updated_at: "2024-01-13 02:44:16.045697"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-stjudem"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.37.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-stjudem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-stjudem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-stjudem", "latest": {"1.42.0--r43hdfd78af_0": "sha256:48c1f9454213c920ac6756d08b028250adc32572f349d38e45b08c1e9f4570a9"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:8b5cf4cdc102b992f320f1808289f6250dde3ab3788babf066b3528adb8889d3", "1.37.0--r42hdfd78af_0": "sha256:bb61f813e41199ee26eae76afead0438d94c0b165244079fc13addde27a09a5a", "1.40.0--r43hdfd78af_0": "sha256:b1b0dc527146e0ddb7b58db258ca00f12a5f9706eab84f4439a297aaf6e35d91", "1.42.0--r43hdfd78af_0": "sha256:48c1f9454213c920ac6756d08b028250adc32572f349d38e45b08c1e9f4570a9"}, "docker": "quay.io/biocontainers/bioconductor-stjudem"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-stjudem.
shpc-registry automated BioContainers addition for bioconductor-stjudem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-stjudem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-stjudem:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-stjudem/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-stjudem/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-stjudem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stjudem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stjudem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-stjudem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-stjudem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-stjudem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-stjudem

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