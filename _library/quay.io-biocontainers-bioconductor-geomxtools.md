---
layout: container
name:  "quay.io/biocontainers/bioconductor-geomxtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geomxtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geomxtools/container.yaml"
updated_at: "2025-02-20 02:58:05.405807"
latest: "3.10.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geomxtools"

versions:
 - "2.0.0--r41hdfd78af_0"
 - "3.2.0--r42hdfd78af_0"
 - "3.4.0--r43hdfd78af_0"
 - "3.5.0--r43hdfd78af_0"
 - "3.10.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geomxtools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geomxtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geomxtools", "latest": {"3.10.0--r44hdfd78af_0": "sha256:667f69a3b20acfe3d9924469e0d910da8abe2541ec20669fef5f93f9f2db3cdd"}, "tags": {"2.0.0--r41hdfd78af_0": "sha256:8d1f370ad13bb6f12719ac2030c1989a4ca60131839839763b9f9840c9573c5f", "3.2.0--r42hdfd78af_0": "sha256:278156e6b51e08f5fbef2b28e957fa4b6917b392e5b2ef8d09c21f6a0c215ef8", "3.4.0--r43hdfd78af_0": "sha256:1071851af3f5bd8223ed58909525243d24308218d4cafb1c7d571760e1c920e4", "3.5.0--r43hdfd78af_0": "sha256:6c80323014000f40f36d3452caf5fbb33f3cb032e277518505dff48f88a1f4d8", "3.10.0--r44hdfd78af_0": "sha256:667f69a3b20acfe3d9924469e0d910da8abe2541ec20669fef5f93f9f2db3cdd"}, "docker": "quay.io/biocontainers/bioconductor-geomxtools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geomxtools.
shpc-registry automated BioContainers addition for bioconductor-geomxtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geomxtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geomxtools:3.10.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geomxtools/3.10.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geomxtools/3.10.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geomxtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geomxtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geomxtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geomxtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geomxtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geomxtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geomxtools

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