---
layout: container
name:  "quay.io/biocontainers/bioconductor-matchbox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-matchbox/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-matchbox/container.yaml"
updated_at: "2024-06-27 03:20:42.648405"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-matchbox"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-matchbox"
config: {"url": "https://biocontainers.pro/tools/bioconductor-matchbox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-matchbox", "latest": {"1.44.0--r43hdfd78af_0": "sha256:f4ec53a522155fd401aee61768637090568ef7359c40333be9ffd8f575fda2d0"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:d7766c1f070451cba15401e2cd6555149efef8f41eba4dca94f95a6157d2f7a9", "1.40.0--r42hdfd78af_0": "sha256:0101eb54f8e7c4bf6779b4ba6a366e4414af85316a078e8448cf3ec3fc3ca51c", "1.42.0--r43hdfd78af_0": "sha256:d338d9c48c66cf28dc231fc1043e159f93e15895e173852f9e455975b708d6e1", "1.44.0--r43hdfd78af_0": "sha256:f4ec53a522155fd401aee61768637090568ef7359c40333be9ffd8f575fda2d0"}, "docker": "quay.io/biocontainers/bioconductor-matchbox"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-matchbox.
shpc-registry automated BioContainers addition for bioconductor-matchbox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-matchbox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-matchbox:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-matchbox/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-matchbox/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-matchbox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matchbox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matchbox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-matchbox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-matchbox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-matchbox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-matchbox

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