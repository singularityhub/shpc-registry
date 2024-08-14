---
layout: container
name:  "quay.io/biocontainers/bioconductor-linkhd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-linkhd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-linkhd/container.yaml"
updated_at: "2024-08-14 03:00:36.529523"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-linkhd"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-linkhd"
config: {"url": "https://biocontainers.pro/tools/bioconductor-linkhd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-linkhd", "latest": {"1.16.0--r43hdfd78af_0": "sha256:63d3b126cf98fec18cbed3413512cbb3442adea121999840d8e99ea9f0d0dd7e"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:eaf0cd0ebf812345bda474b880cdaba019462b8455c86b0a61ffdfe712ab105a", "1.12.0--r42hdfd78af_0": "sha256:89ca82e4f3a60eab67a00756844d48915a83965bbc391fa11249097d9de6518f", "1.14.0--r43hdfd78af_0": "sha256:66d254a8ff57d769130c3735f04dd9c2818bc184f8f834962d1b7f9b1e7f2f22", "1.16.0--r43hdfd78af_0": "sha256:63d3b126cf98fec18cbed3413512cbb3442adea121999840d8e99ea9f0d0dd7e"}, "docker": "quay.io/biocontainers/bioconductor-linkhd"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-linkhd.
shpc-registry automated BioContainers addition for bioconductor-linkhd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-linkhd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-linkhd:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-linkhd/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-linkhd/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-linkhd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-linkhd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-linkhd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-linkhd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-linkhd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-linkhd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-linkhd

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