---
layout: container
name:  "quay.io/biocontainers/bioconductor-deepbluer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deepbluer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deepbluer/container.yaml"
updated_at: "2023-10-02 03:32:34.193092"
latest: "1.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-deepbluer"
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
description: "shpc-registry automated BioContainers addition for bioconductor-deepbluer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deepbluer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deepbluer", "latest": {"1.24.0--r42hdfd78af_0": "sha256:31bb4046c6fefe715f463890391ef80bbd239205898a81720a272b0fa481d099"}, "tags": {"1.8.0--r351_0": "sha256:fda9422a1ae4b343a5f4158d52d619b5fb9cf51e815578a12a87c13dc4054b10", "1.20.0--r41hdfd78af_0": "sha256:a523e524d4f3285519e69c24f7a760b439f35477957554c3ba156f77f9112ac7", "1.18.0--r41hdfd78af_0": "sha256:d45b7e23cdf2a30ba1f56d1970e6bd1e585f36c1a3340117e172defb535f95ad", "1.16.0--r40hdfd78af_1": "sha256:ebf45d3964a896e32dffd6e87b865c1b4d38bae3f1d4fc5fa9687d0d275da994", "1.14.0--r40_0": "sha256:ade8c1ee246a4b01324d562055f5565ec4e0222a6f5bbec5d87f9c38297d98b5", "1.12.0--r36_0": "sha256:0c594696fc785660e64ae81dec16447a56f0cae126bea11db9bc2afd1cf365f8", "1.24.0--r42hdfd78af_0": "sha256:31bb4046c6fefe715f463890391ef80bbd239205898a81720a272b0fa481d099"}, "docker": "quay.io/biocontainers/bioconductor-deepbluer", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deepbluer.
shpc-registry automated BioContainers addition for bioconductor-deepbluer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deepbluer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deepbluer:1.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deepbluer/1.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-deepbluer/1.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deepbluer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deepbluer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deepbluer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deepbluer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deepbluer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deepbluer-inspect-deffile:

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