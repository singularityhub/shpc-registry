---
layout: container
name:  "quay.io/biocontainers/bioconductor-dnabarcodes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dnabarcodes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dnabarcodes/container.yaml"
updated_at: "2024-05-03 02:57:37.017059"
latest: "1.32.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-dnabarcodes"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hc247a5b_0"
 - "1.24.0--r41hc247a5b_2"
 - "1.22.0--r41h399db7b_0"
 - "1.20.0--r40h399db7b_1"
 - "1.18.0--r40h5f743cb_0"
 - "1.28.0--r42hf17093f_2"
 - "1.30.0--r43hf17093f_0"
 - "1.32.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-dnabarcodes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dnabarcodes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dnabarcodes", "latest": {"1.32.0--r43hf17093f_1": "sha256:d6d0ee90d59205021c0a83bc7711a3ef1540669fe8571de08905c545ddc57a89"}, "tags": {"1.8.0--r3.4.1_0": "sha256:7676bc361d846ccfdd8f8aaec5da009c468a6f1409b6be6bb0b78f1c5861213d", "1.28.0--r42hc247a5b_0": "sha256:68df6cdc7524578bc292aded12a4f29ca01316b8d348315f04e91339b2a35bcc", "1.24.0--r41hc247a5b_2": "sha256:4822767822dffea33ac78478d878158fc7c91067659c86b5859fb93ebb0f1948", "1.22.0--r41h399db7b_0": "sha256:515c661be7d2e57a78257d671cdc0e987d73a6cf29507a60e94eeddf70a15fcf", "1.20.0--r40h399db7b_1": "sha256:edbcde9c8c1e978e2c3377ad2857c2588fe4511c35463940d19d8150e9e1136c", "1.18.0--r40h5f743cb_0": "sha256:ee1b4b75ef9bc1490b0ff4ae3ec7c27706020af146f4f99e47c2f1fc41d24242", "1.28.0--r42hf17093f_2": "sha256:c89cf770e6fef010ee9b0135cd88e7bc52da105f0bda5f8acb2acfe3efbd3b32", "1.30.0--r43hf17093f_0": "sha256:a275d9d354fded870c0ab877be966c311e8feeaa985ca60c83d285463aa0e1ce", "1.32.0--r43hf17093f_1": "sha256:d6d0ee90d59205021c0a83bc7711a3ef1540669fe8571de08905c545ddc57a89"}, "docker": "quay.io/biocontainers/bioconductor-dnabarcodes", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dnabarcodes.
shpc-registry automated BioContainers addition for bioconductor-dnabarcodes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dnabarcodes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dnabarcodes:1.32.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dnabarcodes/1.32.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-dnabarcodes/1.32.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dnabarcodes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dnabarcodes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dnabarcodes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dnabarcodes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dnabarcodes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dnabarcodes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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