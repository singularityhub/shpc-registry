---
layout: container
name:  "quay.io/biocontainers/bioconductor-drugvsdiseasedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drugvsdiseasedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drugvsdiseasedata/container.yaml"
updated_at: "2024-07-26 03:03:24.460368"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-drugvsdiseasedata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-drugvsdiseasedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drugvsdiseasedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drugvsdiseasedata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:9e236cb23022ff621ed328d1dd61fd6fcafa4d86eae884771774790258acbf85"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:282ed4e9d6fb2345acfeee7141129a89e51387c7878cff74a51caa811bc4300d", "1.34.0--r42hdfd78af_0": "sha256:b74a8145a0058c9ef5790bcf5a0338fd993f0ee459488af819cbe6d5ae66e5a6", "1.33.0--r42hdfd78af_0": "sha256:ab4538d8848a2e4d763823bcea58d5e0e9dc748521c236075d5eca4cfc6277cd", "1.36.0--r43hdfd78af_0": "sha256:5660954c05c796b2d4df28a2229aa0ab6571aed466d86793b961db666f03cbfc", "1.38.0--r43hdfd78af_0": "sha256:9e236cb23022ff621ed328d1dd61fd6fcafa4d86eae884771774790258acbf85"}, "docker": "quay.io/biocontainers/bioconductor-drugvsdiseasedata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drugvsdiseasedata.
shpc-registry automated BioContainers addition for bioconductor-drugvsdiseasedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drugvsdiseasedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drugvsdiseasedata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drugvsdiseasedata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-drugvsdiseasedata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drugvsdiseasedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drugvsdiseasedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drugvsdiseasedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drugvsdiseasedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drugvsdiseasedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drugvsdiseasedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-drugvsdiseasedata

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