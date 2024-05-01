---
layout: container
name:  "quay.io/biocontainers/bioconductor-msbackendsql"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msbackendsql/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msbackendsql/container.yaml"
updated_at: "2024-05-01 02:38:27.247173"
latest: "1.2.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msbackendsql"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.1--r43hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-msbackendsql"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msbackendsql", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-msbackendsql", "latest": {"1.2.0--r43hdfd78af_0": "sha256:d0ceb5eeb00f052a4be8a0ce37bc27edcb545e0fefcb3ff2e5295f45f9401c63"}, "tags": {"1.0.1--r43hdfd78af_0": "sha256:69926e6de94bb820121926f6c2073cbce007078dca3b593b42b1ca2b83e0f473", "1.2.0--r43hdfd78af_0": "sha256:d0ceb5eeb00f052a4be8a0ce37bc27edcb545e0fefcb3ff2e5295f45f9401c63"}, "docker": "quay.io/biocontainers/bioconductor-msbackendsql", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msbackendsql.
singularity registry hpc automated addition for bioconductor-msbackendsql
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendsql
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendsql:1.2.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msbackendsql/1.2.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msbackendsql/1.2.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msbackendsql-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendsql-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendsql-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msbackendsql-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msbackendsql-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msbackendsql-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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