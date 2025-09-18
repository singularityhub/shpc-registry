---
layout: container
name:  "quay.io/biocontainers/bioconductor-plotgardenerdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plotgardenerdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plotgardenerdata/container.yaml"
updated_at: "2025-09-18 03:35:23.520696"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-plotgardenerdata"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.3.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-plotgardenerdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plotgardenerdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plotgardenerdata", "latest": {"1.12.0--r44hdfd78af_0": "sha256:7a1235cc6a32c509aca8555435a0800555b691ca4f96645c08a3f46cc5faf1ac"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:fe663325de4c2fe3f3fdc77461e171dcfd90ddabaadca5752b50477f884b1352", "1.3.0--r42hdfd78af_0": "sha256:644b9b31b718de3e32914f4396d24b92a12592426d211c55a107d77951673396", "1.6.0--r43hdfd78af_0": "sha256:e50af3282795b525fb60ccb8b8df73d56459c4e38b492c942987807413fb498b", "1.8.0--r43hdfd78af_0": "sha256:217a09487ba8edc2bec0ba783e5e02ba249b8515c2e3964c3243ea5f7dfc73ac", "1.12.0--r44hdfd78af_0": "sha256:7a1235cc6a32c509aca8555435a0800555b691ca4f96645c08a3f46cc5faf1ac"}, "docker": "quay.io/biocontainers/bioconductor-plotgardenerdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plotgardenerdata.
shpc-registry automated BioContainers addition for bioconductor-plotgardenerdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plotgardenerdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plotgardenerdata:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plotgardenerdata/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-plotgardenerdata/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plotgardenerdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plotgardenerdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plotgardenerdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plotgardenerdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plotgardenerdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plotgardenerdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-plotgardenerdata

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