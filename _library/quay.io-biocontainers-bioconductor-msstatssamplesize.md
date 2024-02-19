---
layout: container
name:  "quay.io/biocontainers/bioconductor-msstatssamplesize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msstatssamplesize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msstatssamplesize/container.yaml"
updated_at: "2024-02-19 02:50:07.051210"
latest: "1.13.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msstatssamplesize"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.13.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msstatssamplesize"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msstatssamplesize", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msstatssamplesize", "latest": {"1.13.0--r43hdfd78af_0": "sha256:a4a35d0015b820ead67bb04911568194ed404e3fa40c81eb41c660f2cc5782a9"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:4fc5f3aed9346756928bb91171687ec0f87f7783a779a88b19d0f147787b9479", "1.12.0--r42hdfd78af_0": "sha256:923664192a3c3e9bd7b4d1aa0adb23c6b71ec027cb239390dbb27f792e55b785", "1.13.0--r43hdfd78af_0": "sha256:a4a35d0015b820ead67bb04911568194ed404e3fa40c81eb41c660f2cc5782a9"}, "docker": "quay.io/biocontainers/bioconductor-msstatssamplesize"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msstatssamplesize.
shpc-registry automated BioContainers addition for bioconductor-msstatssamplesize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatssamplesize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatssamplesize:1.13.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msstatssamplesize/1.13.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msstatssamplesize/1.13.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msstatssamplesize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatssamplesize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatssamplesize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msstatssamplesize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msstatssamplesize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msstatssamplesize-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msstatssamplesize

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