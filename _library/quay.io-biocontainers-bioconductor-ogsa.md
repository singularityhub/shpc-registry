---
layout: container
name:  "quay.io/biocontainers/bioconductor-ogsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ogsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ogsa/container.yaml"
updated_at: "2025-02-23 03:10:53.767525"
latest: "1.17.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ogsa"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.17.0--r40_0"
 - "1.16.0--r36_0"
 - "1.14.0--r36_1"
 - "1.12.0--r351_0"
 - "1.10.0--r341_0"
 - "1.10.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ogsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ogsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ogsa", "latest": {"1.17.0--r40_0": "sha256:bae98f5d1d2e14dd54f7409c4cf36d44c56a397be326eda1badeafdc39fb691f"}, "tags": {"1.8.0--r3.4.1_0": "sha256:0b30c897f452c34683787fc83bf2932abc71fb335264e4d60d637f220bc73d92", "1.17.0--r40_0": "sha256:bae98f5d1d2e14dd54f7409c4cf36d44c56a397be326eda1badeafdc39fb691f", "1.16.0--r36_0": "sha256:a41d21915d2d11e57ddd1f304ce3072ef22a924bc7780ba66e5ff5626e042d30", "1.14.0--r36_1": "sha256:d001fc129b4632337dcabe7fbb86c346345038d3841444966e16bf014eb52a6d", "1.12.0--r351_0": "sha256:8bfa5d83bc7cc9f0aad552ce625831235a90b2ea25cbd696e94dab1e4abc596b", "1.10.0--r341_0": "sha256:1af802fe68188f0a45baedbcbb68273a3b8361f1aa3eb48d7ce207695fac49a5", "1.10.0--r351_0": "sha256:33788312b6fb4ec80ff23d15a3de3cc63b30ab51ea1bf509a283588c66197a29"}, "docker": "quay.io/biocontainers/bioconductor-ogsa", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ogsa.
shpc-registry automated BioContainers addition for bioconductor-ogsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ogsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ogsa:1.17.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ogsa/1.17.0--r40_0
$ module help quay.io/biocontainers/bioconductor-ogsa/1.17.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ogsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ogsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ogsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ogsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ogsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ogsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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