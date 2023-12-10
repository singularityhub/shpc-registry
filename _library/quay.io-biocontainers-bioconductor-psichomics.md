---
layout: container
name:  "quay.io/biocontainers/bioconductor-psichomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-psichomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-psichomics/container.yaml"
updated_at: "2023-12-10 02:39:06.392069"
latest: "1.26.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-psichomics"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351hf484d3e_0"
 - "1.20.2--r41hc247a5b_0"
 - "1.18.1--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.13.1--r40h5f743cb_0"
 - "1.12.0--r36he1b5a44_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.24.0--r42hf17093f_1"
 - "1.26.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-psichomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-psichomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-psichomics", "latest": {"1.26.0--r43hf17093f_0": "sha256:3e3bddec8ab3e651d96eb434bd5c8a2e8e741d6cd745e004eb2f21ea293f9978"}, "tags": {"1.8.1--r351hf484d3e_0": "sha256:b163cdc3837ace65e841e675949727823aa6f26d2539b0600da6ae602dd51ba4", "1.20.2--r41hc247a5b_0": "sha256:559c8e285296201aa44890289fec4e96c89c8d15ea36c27a54a3e8fb32188572", "1.18.1--r41h399db7b_0": "sha256:1fb8c219f7c688c54553841a1fac085cb47f2b2adf5cc2aa47585e4e78f690b6", "1.16.0--r40h399db7b_1": "sha256:d76617f5d2c000a558cf28ed41fd10f8a74d62bc5a5f6ff6991026391ef5ef72", "1.13.1--r40h5f743cb_0": "sha256:0c8f515fbe5e7e04a2ebb59cda49269357a6fd29877588622a040ead25504862", "1.12.0--r36he1b5a44_0": "sha256:8dbcd55508bc54dc5602a226602ce9b08dc933d1eda4fa19da0f5efc03310d11", "1.24.0--r42hc247a5b_0": "sha256:5fb490f37bbe60ab7048ec19019e59849ac6ef8d4851208db81d51b51bd7890d", "1.24.0--r42hf17093f_1": "sha256:a2e34ecac623e4fa3ed0e35846e39279b8e01e17d1bab1fba1ddb211dd1afd7c", "1.26.0--r43hf17093f_0": "sha256:3e3bddec8ab3e651d96eb434bd5c8a2e8e741d6cd745e004eb2f21ea293f9978"}, "docker": "quay.io/biocontainers/bioconductor-psichomics", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-psichomics.
shpc-registry automated BioContainers addition for bioconductor-psichomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-psichomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-psichomics:1.26.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-psichomics/1.26.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-psichomics/1.26.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-psichomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-psichomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-psichomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-psichomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-psichomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-psichomics-inspect-deffile:

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