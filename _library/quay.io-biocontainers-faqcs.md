---
layout: container
name:  "quay.io/biocontainers/faqcs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/faqcs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/faqcs/container.yaml"
updated_at: "2025-09-11 05:39:35.990017"
latest: "2.12--r44h077b44d_0"
container_url: "https://biocontainers.pro/tools/faqcs"
aliases:
 - "FaQCs"
versions:
 - "2.10--r41hd03093a_3"
 - "2.10--r42hd03093a_4"
 - "2.10--r42hdcf5f25_6"
 - "2.10--r43hdcf5f25_7"
 - "2.10--r44h077b44d_8"
 - "2.12--r44h077b44d_0"
 - "2.11--r44h077b44d_0"
description: "shpc-registry automated BioContainers addition for faqcs"
config: {"url": "https://biocontainers.pro/tools/faqcs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for faqcs", "latest": {"2.12--r44h077b44d_0": "sha256:d5efd89e5fe0b08e2b8b94029216e307dd68483cf43d8030a8a00c0256a3d645"}, "tags": {"2.10--r41hd03093a_3": "sha256:41f3f43b38fa6d32523380fe05ce5ce9a78ab669bdecf9bd56fe42e9444dff56", "2.10--r42hd03093a_4": "sha256:25653970a1f3709cc25c27dbe9170df2afbcc0a8445d3a1ebbebd3ee7ec6ba30", "2.10--r42hdcf5f25_6": "sha256:55cab9e1769c1ca580ad91bd4561a8a7f2e150820dcbbd6421759bff6939a793", "2.10--r43hdcf5f25_7": "sha256:fe3c82aa141647a7bb544f958adec2b156d56afbe9fe2ca499fa390ca6f58ed9", "2.10--r44h077b44d_8": "sha256:d515b9baa86d5dadcee5468cd9542eef5e3f60fbcb349c6051ad07212f0fd768", "2.12--r44h077b44d_0": "sha256:d5efd89e5fe0b08e2b8b94029216e307dd68483cf43d8030a8a00c0256a3d645", "2.11--r44h077b44d_0": "sha256:26c86b5efcbd1c876a60051b480310478a1eb54b65a540c8e29069eeaf21c8b2"}, "docker": "quay.io/biocontainers/faqcs", "aliases": {"FaQCs": "/usr/local/bin/FaQCs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/faqcs.
shpc-registry automated BioContainers addition for faqcs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/faqcs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/faqcs:2.12--r44h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/faqcs/2.12--r44h077b44d_0
$ module help quay.io/biocontainers/faqcs/2.12--r44h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### faqcs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### faqcs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### faqcs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### faqcs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### faqcs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### faqcs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FaQCs

```bash
$ singularity exec <container> /usr/local/bin/FaQCs
$ podman run --it --rm --entrypoint /usr/local/bin/FaQCs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FaQCs   -v ${PWD} -w ${PWD} <container> -c " $@"
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