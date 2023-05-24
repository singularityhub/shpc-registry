---
layout: container
name:  "quay.io/biocontainers/phipack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phipack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phipack/container.yaml"
updated_at: "2023-05-24 02:45:42.315787"
latest: "1.1--h031d066_4"
container_url: "https://biocontainers.pro/tools/phipack"
aliases:
 - "Phi"
 - "Profile"
versions:
 - "1.1--hec16e2b_2"
 - "1.1--h031d066_4"
description: "shpc-registry automated BioContainers addition for phipack"
config: {"url": "https://biocontainers.pro/tools/phipack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phipack", "latest": {"1.1--h031d066_4": "sha256:e6405c4d06d41949a45c9fc6bdf1e8f27bcb127f2e3330a8fb33f9580ec0e224"}, "tags": {"1.1--hec16e2b_2": "sha256:c9864663c0e2705837d3420dfbbed9af02607f309a7e3292118abc7eb9059e96", "1.1--h031d066_4": "sha256:e6405c4d06d41949a45c9fc6bdf1e8f27bcb127f2e3330a8fb33f9580ec0e224"}, "docker": "quay.io/biocontainers/phipack", "aliases": {"Phi": "/usr/local/bin/Phi", "Profile": "/usr/local/bin/Profile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phipack.
shpc-registry automated BioContainers addition for phipack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phipack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phipack:1.1--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phipack/1.1--h031d066_4
$ module help quay.io/biocontainers/phipack/1.1--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phipack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phipack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phipack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phipack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phipack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phipack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Phi

```bash
$ singularity exec <container> /usr/local/bin/Phi
$ podman run --it --rm --entrypoint /usr/local/bin/Phi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Phi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Profile

```bash
$ singularity exec <container> /usr/local/bin/Profile
$ podman run --it --rm --entrypoint /usr/local/bin/Profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Profile   -v ${PWD} -w ${PWD} <container> -c " $@"
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