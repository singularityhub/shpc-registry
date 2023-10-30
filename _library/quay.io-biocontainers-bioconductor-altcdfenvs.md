---
layout: container
name:  "quay.io/biocontainers/bioconductor-altcdfenvs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-altcdfenvs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-altcdfenvs/container.yaml"
updated_at: "2023-10-30 02:57:26.062038"
latest: "2.62.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-altcdfenvs"

versions:
 - "2.56.0--r41hdfd78af_0"
 - "2.60.0--r42hdfd78af_0"
 - "2.62.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-altcdfenvs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-altcdfenvs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-altcdfenvs", "latest": {"2.62.0--r43hdfd78af_0": "sha256:a5519cc072def5bfc89951e56f87ac144567b73ff95f7d9f50194837370206cf"}, "tags": {"2.56.0--r41hdfd78af_0": "sha256:e9bc1f4ef3f912f941b569f823a799783a6c51a40f284cc826fb27848b73fac2", "2.60.0--r42hdfd78af_0": "sha256:dcaa7421c450eacd5f6c3d039b22c3306acbc6ac8a1847f3e01c575552655c93", "2.62.0--r43hdfd78af_0": "sha256:a5519cc072def5bfc89951e56f87ac144567b73ff95f7d9f50194837370206cf"}, "docker": "quay.io/biocontainers/bioconductor-altcdfenvs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-altcdfenvs.
shpc-registry automated BioContainers addition for bioconductor-altcdfenvs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-altcdfenvs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-altcdfenvs:2.62.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-altcdfenvs/2.62.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-altcdfenvs/2.62.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-altcdfenvs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-altcdfenvs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-altcdfenvs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-altcdfenvs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-altcdfenvs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-altcdfenvs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-altcdfenvs

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