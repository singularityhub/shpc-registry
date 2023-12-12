---
layout: container
name:  "quay.io/biocontainers/bioconductor-yeast2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yeast2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yeast2probe/container.yaml"
updated_at: "2023-12-12 02:55:49.200590"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-yeast2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-yeast2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yeast2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yeast2probe", "latest": {"2.18.0--r43hdfd78af_13": "sha256:d4176aed79fb56a5d95a9a2a28fa7b1f31dc26b0875a6eccce42dcca04ed07f9"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5c4fee88635afc31c8a613c75b24678982f8cfd4b5e79656464cba5c44f0eb3b", "2.18.0--r42hdfd78af_11": "sha256:5e16a61027d41bc93a50d79e9719d03f54fbded84002e8f4cbce1965b06e2b8c", "2.18.0--r43hdfd78af_12": "sha256:ea9b15cc31845dd23205754eae931898f131f997bd39b975ce837eee394eebb8", "2.18.0--r43hdfd78af_13": "sha256:d4176aed79fb56a5d95a9a2a28fa7b1f31dc26b0875a6eccce42dcca04ed07f9"}, "docker": "quay.io/biocontainers/bioconductor-yeast2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yeast2probe.
shpc-registry automated BioContainers addition for bioconductor-yeast2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yeast2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yeast2probe:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yeast2probe/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-yeast2probe/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yeast2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeast2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeast2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yeast2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yeast2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yeast2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-yeast2probe

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