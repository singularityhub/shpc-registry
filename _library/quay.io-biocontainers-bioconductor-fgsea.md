---
layout: container
name:  "quay.io/biocontainers/bioconductor-fgsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fgsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fgsea/container.yaml"
updated_at: "2025-01-02 02:59:50.940269"
latest: "1.28.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fgsea"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351hf484d3e_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "1.24.0--r42hf17093f_1"
 - "1.26.0--r43hf17093f_0"
 - "1.28.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fgsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fgsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fgsea", "latest": {"1.28.0--r43hf17093f_0": "sha256:00fe6d2d18c12354c1469922bb5e48c79337aa84cfb3fbc7fecc2a608cb7164a"}, "tags": {"1.8.0--r351hf484d3e_0": "sha256:6764fa3db66be3d214366a836eca06d4ab405e8172e6cf90be504b544b4dc65f", "1.24.0--r42hc247a5b_0": "sha256:8089fda8d4efbaffd5d7d5100bf3be7c5ea48951ad1e9219427ecbad5a6b2125", "1.20.0--r41hc247a5b_2": "sha256:e5ba13f819fa121a77bb37ce262483fbc435c6195eeeaf267da7f742aedf6b92", "1.18.0--r41h399db7b_0": "sha256:b44aa9d249cd804b5ea2ceb777bc2bbaf9ffa2df436445244b4802a3d5dfdf17", "1.16.0--r40h399db7b_1": "sha256:78d59211ed86ddb168d08ae5391650ca7d2c5ebe501e60205bd3421f068f7ec1", "1.14.0--r40h5f743cb_0": "sha256:0e31d732fd7560fa13de09512026b345af61abd53ff1c6fa1af9a3c1bb243294", "1.24.0--r42hf17093f_1": "sha256:f9da7c516ed966b74ce93fcdd50fc4664b187cde3d747844d7359b28450253b2", "1.26.0--r43hf17093f_0": "sha256:6b59c5d7128e3e47f5062ea133c7267c4230650da5abb126296ee6c1f6f89a87", "1.28.0--r43hf17093f_0": "sha256:00fe6d2d18c12354c1469922bb5e48c79337aa84cfb3fbc7fecc2a608cb7164a"}, "docker": "quay.io/biocontainers/bioconductor-fgsea", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fgsea.
shpc-registry automated BioContainers addition for bioconductor-fgsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fgsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fgsea:1.28.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fgsea/1.28.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-fgsea/1.28.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fgsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fgsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fgsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fgsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fgsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fgsea-inspect-deffile:

```bash
$ singularity inspect -d <container>
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