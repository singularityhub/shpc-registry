---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirna10probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirna10probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirna10probe/container.yaml"
updated_at: "2024-03-25 02:56:26.757656"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mirna10probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mirna10probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirna10probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirna10probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:950b3186e6c33a16099bd098b28461489feda8c27799232855e96eed0244fcd5"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f1ae66478cf6313fd4570f556ca99ab5f773c433a068fc88428671e2546bbbc0", "2.18.0--r42hdfd78af_10": "sha256:cd6d7e67ba82e8ca99e22c50b4d28d509fb878dee1c52649f67ab86a310160cb", "2.18.0--r43hdfd78af_11": "sha256:40f39451ec745df25206033c53bbd6c0a14dbad2855ef71d7d4f82ff6d1833af", "2.18.0--r43hdfd78af_12": "sha256:950b3186e6c33a16099bd098b28461489feda8c27799232855e96eed0244fcd5"}, "docker": "quay.io/biocontainers/bioconductor-mirna10probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirna10probe.
shpc-registry automated BioContainers addition for bioconductor-mirna10probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna10probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna10probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirna10probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mirna10probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirna10probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna10probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna10probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirna10probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirna10probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirna10probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirna10probe

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