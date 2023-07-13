---
layout: container
name:  "quay.io/biocontainers/nseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nseg/container.yaml"
updated_at: "2023-07-13 03:51:24.799243"
latest: "1.0.1--h031d066_4"
container_url: "https://biocontainers.pro/tools/nseg"
aliases:
 - "nmerge"
 - "nseg"
versions:
 - "1.0.1--hec16e2b_2"
 - "1.0.1--hec16e2b_3"
 - "1.0.1--h031d066_4"
description: "shpc-registry automated BioContainers addition for nseg"
config: {"url": "https://biocontainers.pro/tools/nseg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nseg", "latest": {"1.0.1--h031d066_4": "sha256:7fc8b63329fe94d80458514e53699e17f9085349913a16868d4d3fd7f372cf3c"}, "tags": {"1.0.1--hec16e2b_2": "sha256:ecb65fda2abb6f2e61debff988b14eaaecc09fa340e960b69a10fb3102b35af1", "1.0.1--hec16e2b_3": "sha256:0bdbbbaed595facafbdf0f9ab4ba264fda38febb9663e9b507ab0ea0e979f4fd", "1.0.1--h031d066_4": "sha256:7fc8b63329fe94d80458514e53699e17f9085349913a16868d4d3fd7f372cf3c"}, "docker": "quay.io/biocontainers/nseg", "aliases": {"nmerge": "/usr/local/bin/nmerge", "nseg": "/usr/local/bin/nseg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nseg.
shpc-registry automated BioContainers addition for nseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nseg:1.0.1--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nseg/1.0.1--h031d066_4
$ module help quay.io/biocontainers/nseg/1.0.1--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nseg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nmerge

```bash
$ singularity exec <container> /usr/local/bin/nmerge
$ podman run --it --rm --entrypoint /usr/local/bin/nmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nseg

```bash
$ singularity exec <container> /usr/local/bin/nseg
$ podman run --it --rm --entrypoint /usr/local/bin/nseg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nseg   -v ${PWD} -w ${PWD} <container> -c " $@"
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