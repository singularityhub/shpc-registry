---
layout: container
name:  "quay.io/biocontainers/bacgwasim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bacgwasim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bacgwasim/container.yaml"
updated_at: "2024-10-02 02:55:24.665652"
latest: "2.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bacgwasim"
aliases:
 - "BacGWASim"
 - "SimBac"
 - "gcta64"
 - "plink"
 - "snp-sites"
 - "stone"
 - "dendropy-format"
 - "x86_64-conda-linux-gnu-pkg-config"
 - "pulptest"
 - "Magick++-config"
 - "MagickCore-config"
 - "MagickWand-config"
 - "animate"
 - "composite"
versions:
 - "2.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for bacgwasim"
config: {"url": "https://biocontainers.pro/tools/bacgwasim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bacgwasim", "latest": {"2.1.1--pyhdfd78af_0": "sha256:4b06901ae551a2f2fba28bd82a4bbda2d4046698f939e66cdfe3f303dc910847"}, "tags": {"2.1.1--pyhdfd78af_0": "sha256:4b06901ae551a2f2fba28bd82a4bbda2d4046698f939e66cdfe3f303dc910847"}, "docker": "quay.io/biocontainers/bacgwasim", "aliases": {"BacGWASim": "/usr/local/bin/BacGWASim", "SimBac": "/usr/local/bin/SimBac", "gcta64": "/usr/local/bin/gcta64", "plink": "/usr/local/bin/plink", "snp-sites": "/usr/local/bin/snp-sites", "stone": "/usr/local/bin/stone", "dendropy-format": "/usr/local/bin/dendropy-format", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "pulptest": "/usr/local/bin/pulptest", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config", "animate": "/usr/local/bin/animate", "composite": "/usr/local/bin/composite"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bacgwasim.
shpc-registry automated BioContainers addition for bacgwasim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bacgwasim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bacgwasim:2.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bacgwasim/2.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/bacgwasim/2.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bacgwasim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bacgwasim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bacgwasim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bacgwasim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bacgwasim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bacgwasim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BacGWASim

```bash
$ singularity exec <container> /usr/local/bin/BacGWASim
$ podman run --it --rm --entrypoint /usr/local/bin/BacGWASim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BacGWASim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SimBac

```bash
$ singularity exec <container> /usr/local/bin/SimBac
$ podman run --it --rm --entrypoint /usr/local/bin/SimBac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SimBac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcta64

```bash
$ singularity exec <container> /usr/local/bin/gcta64
$ podman run --it --rm --entrypoint /usr/local/bin/gcta64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcta64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plink

```bash
$ singularity exec <container> /usr/local/bin/plink
$ podman run --it --rm --entrypoint /usr/local/bin/plink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp-sites

```bash
$ singularity exec <container> /usr/local/bin/snp-sites
$ podman run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Magick++-config

```bash
$ singularity exec <container> /usr/local/bin/Magick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickCore-config

```bash
$ singularity exec <container> /usr/local/bin/MagickCore-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickWand-config

```bash
$ singularity exec <container> /usr/local/bin/MagickWand-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### animate

```bash
$ singularity exec <container> /usr/local/bin/animate
$ podman run --it --rm --entrypoint /usr/local/bin/animate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/animate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### composite

```bash
$ singularity exec <container> /usr/local/bin/composite
$ podman run --it --rm --entrypoint /usr/local/bin/composite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/composite   -v ${PWD} -w ${PWD} <container> -c " $@"
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