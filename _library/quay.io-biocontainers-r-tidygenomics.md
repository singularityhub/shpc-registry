---
layout: container
name:  "quay.io/biocontainers/r-tidygenomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-tidygenomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-tidygenomics/container.yaml"
updated_at: "2025-12-18 04:09:54.514149"
latest: "0.1.2--r44h40dc89f_8"
container_url: "https://biocontainers.pro/tools/r-tidygenomics"

versions:
 - "0.1.2--r41hecf12ef_4"
 - "0.1.2--r42hecf12ef_5"
 - "0.1.2--r42h21a89ab_6"
 - "0.1.2--r43h21a89ab_7"
 - "0.1.2--r44h40dc89f_8"
description: "shpc-registry automated BioContainers addition for r-tidygenomics"
config: {"url": "https://biocontainers.pro/tools/r-tidygenomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-tidygenomics", "latest": {"0.1.2--r44h40dc89f_8": "sha256:ee29e872f8a64b1bd157f7f67a973df68656a5a758c8e040a64f689cfc8e43f8"}, "tags": {"0.1.2--r41hecf12ef_4": "sha256:70e1ed47252e8ef02292e6ba26fc347ad224d6325b2341237258771f57f8a383", "0.1.2--r42hecf12ef_5": "sha256:fec2c28a6b782cee687bd8c357716e4bcd572d295daa08a536e779a59e78b2e0", "0.1.2--r42h21a89ab_6": "sha256:9e7632a799d6c86ff483d00fdc77fe75551cc4549959fdbbcb754b87a31d50fe", "0.1.2--r43h21a89ab_7": "sha256:1474e25040f12203ab796b8d8c0098e77c009b3adcc4ba3102cbdc8c7a2ceed0", "0.1.2--r44h40dc89f_8": "sha256:ee29e872f8a64b1bd157f7f67a973df68656a5a758c8e040a64f689cfc8e43f8"}, "docker": "quay.io/biocontainers/r-tidygenomics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-tidygenomics.
shpc-registry automated BioContainers addition for r-tidygenomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-tidygenomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-tidygenomics:0.1.2--r44h40dc89f_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-tidygenomics/0.1.2--r44h40dc89f_8
$ module help quay.io/biocontainers/r-tidygenomics/0.1.2--r44h40dc89f_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-tidygenomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-tidygenomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-tidygenomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-tidygenomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-tidygenomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-tidygenomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-tidygenomics

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