---
layout: container
name:  "quay.io/biocontainers/bioconductor-experimenthubdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-experimenthubdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-experimenthubdata/container.yaml"
updated_at: "2025-05-24 11:15:41.259059"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-experimenthubdata"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-experimenthubdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-experimenthubdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-experimenthubdata", "latest": {"1.32.0--r44hdfd78af_0": "sha256:e6848421e8f44be38a8118521e563d7c6616a2302c12f6fc01e89df6d7a1b7d9"}, "tags": {"1.8.0--r351_0": "sha256:ad7037b109b29c26acf5812988bf3fbfe49c8de53b080a7709602759afeb1c96", "1.20.0--r41hdfd78af_0": "sha256:4ede104f7af994756750a5e571a64c64e685b029df93361aae5de3d241fc4e33", "1.18.0--r41hdfd78af_0": "sha256:f67895ee66da9cba7cec6c9b616177fa90c668ae538825aa947ae0e353725d8a", "1.16.0--r40hdfd78af_1": "sha256:2f67a7a83ae9a6c89ff050fab15901da25b23d7416eebc28c05bd8d7eca05340", "1.14.0--r40_0": "sha256:756eca4bfe7abe1e3107e721f5a339a5e3f32fd9436eb506f6cb53ec945144ad", "1.12.0--r36_0": "sha256:a94a4a504b3f568a5aa3cc8340e67775d368db70f5103505add0ed2da6784c3a", "1.24.0--r42hdfd78af_0": "sha256:2060f5b2ad6d427a5035023ea8e1907cb54f742315c47b1a5cb607ba67b8e585", "1.26.0--r43hdfd78af_0": "sha256:693693df208f97ed98b0720fce471b76134c6beb875d0d27685d49dc43334ef4", "1.28.0--r43hdfd78af_0": "sha256:6a18dd7e14149da83e103ac1d44d9f285611a2a37260302d97e12bf4a1945f75", "1.32.0--r44hdfd78af_0": "sha256:e6848421e8f44be38a8118521e563d7c6616a2302c12f6fc01e89df6d7a1b7d9"}, "docker": "quay.io/biocontainers/bioconductor-experimenthubdata", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-experimenthubdata.
shpc-registry automated BioContainers addition for bioconductor-experimenthubdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-experimenthubdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-experimenthubdata:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-experimenthubdata/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-experimenthubdata/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-experimenthubdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-experimenthubdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-experimenthubdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-experimenthubdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-experimenthubdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-experimenthubdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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