---
layout: container
name:  "quay.io/biocontainers/bioconductor-csdr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-csdr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-csdr/container.yaml"
updated_at: "2025-06-24 03:40:16.196021"
latest: "1.12.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-csdr"

versions:
 - "1.0.0--r41hc247a5b_2"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
 - "1.8.0--r43hf17093f_0"
 - "1.12.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-csdr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-csdr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-csdr", "latest": {"1.12.0--r44he5774e6_0": "sha256:7750a8aa73984e9c74575256c6e07ae51afb09aafbe4aa9cb715984aa08b9f7e"}, "tags": {"1.0.0--r41hc247a5b_2": "sha256:4d600ac2a62cdf7f4cd5c9e195c2a91fd3628931ad015d9ace071335239e6806", "1.4.0--r42hc247a5b_0": "sha256:542ff548228da23851e632a5757609018786606ecee84b8a3f5acd9254346b69", "1.4.0--r42hf17093f_1": "sha256:026cab2337579a78a7f43bee06282bff2842863bea65034a5ba6eddb97a61ce1", "1.6.0--r43hf17093f_0": "sha256:8285787abc9ce35413f053178738a237d5af0d925f362508fe3ed58bf534f593", "1.8.0--r43hf17093f_0": "sha256:95fe762153aaed80b434fd6fcfbd2daf5f4cd53444f82e6f008184af553fb343", "1.12.0--r44he5774e6_0": "sha256:7750a8aa73984e9c74575256c6e07ae51afb09aafbe4aa9cb715984aa08b9f7e"}, "docker": "quay.io/biocontainers/bioconductor-csdr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-csdr.
shpc-registry automated BioContainers addition for bioconductor-csdr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-csdr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-csdr:1.12.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-csdr/1.12.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-csdr/1.12.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-csdr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-csdr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-csdr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-csdr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-csdr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-csdr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-csdr

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