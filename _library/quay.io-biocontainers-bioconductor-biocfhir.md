---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocfhir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocfhir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocfhir/container.yaml"
updated_at: "2026-01-18 04:05:01.100369"
latest: "1.8.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocfhir"
aliases:
 - "glpsol"
versions:
 - "1.0.0--r42hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.8.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-biocfhir"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocfhir", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-biocfhir", "latest": {"1.8.0--r44hdfd78af_0": "sha256:9b8983e6decd6442aa64cb8e1008a21948e33ea7d0d8a5bd7466d2747401c66f"}, "tags": {"1.0.0--r42hdfd78af_0": "sha256:bfc126eebe85e2ebeb4838a5052e8f9adfc11c396c4cda65db2c4560c8b1830b", "1.2.0--r43hdfd78af_0": "sha256:f2f955522a3cc22f76ba18829f335ad39dd00aa66bdb4880ffc9fb74e2fbbc24", "1.4.0--r43hdfd78af_0": "sha256:e331fbd381a2bf991277aa095fdb524c0e39f2f77136e35fc217f290ed294aa1", "1.8.0--r44hdfd78af_0": "sha256:9b8983e6decd6442aa64cb8e1008a21948e33ea7d0d8a5bd7466d2747401c66f"}, "docker": "quay.io/biocontainers/bioconductor-biocfhir", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocfhir.
singularity registry hpc automated addition for bioconductor-biocfhir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocfhir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocfhir:1.8.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocfhir/1.8.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocfhir/1.8.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocfhir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocfhir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocfhir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocfhir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocfhir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocfhir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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