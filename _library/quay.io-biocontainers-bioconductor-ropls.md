---
layout: container
name:  "quay.io/biocontainers/bioconductor-ropls"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ropls/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ropls/container.yaml"
updated_at: "2026-01-26 04:42:22.935296"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ropls"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.26.0--r41hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r40hdfd78af_1"
 - "1.20.0--r40_0"
 - "1.18.0--r36_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ropls"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ropls", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ropls", "latest": {"1.38.0--r44hdfd78af_0": "sha256:e3de5670360fd36ecb45c6c3692a6b6cf439636b76856738faf64181487a01e1"}, "tags": {"1.8.0--r3.4.1_0": "sha256:c68d39fe8f18f6bdecbcf008883a58bbb07e1d7732ff98f280f944799e478f7c", "1.26.0--r41hdfd78af_0": "sha256:8e44a03188ca6bca95c7f50f52120c507b4e981fb6ebcef4519409d8261c28f6", "1.24.0--r41hdfd78af_0": "sha256:f0cf203abd54783917d9fed814bf3afac07b33a1db32ee8bdaed0b2d0eaec706", "1.22.0--r40hdfd78af_1": "sha256:548c29bc2b2fa9a94024f5650a4ac023c600966aab3841dea40cde6fb1d8117e", "1.20.0--r40_0": "sha256:acb66757bb4a1ba52b3a3b7582852b29970725bfbbd2e60e321b566e75bb4f5b", "1.18.0--r36_0": "sha256:6456f90dab9421596d80696dd984ebcde9d19253cd529047a64faa0614018bcc", "1.30.0--r42hdfd78af_0": "sha256:23f6640b45db107b1fc1df85a8e0433d7c0da3f3c0ebeab21e95b43d3b58b036", "1.32.0--r43hdfd78af_0": "sha256:42b4be91624b06bfbbb9d6f737752305fd25d188720ae5199c0239a6b251c6a9", "1.34.0--r43hdfd78af_0": "sha256:fa38ce1472f4472d30d073a465d5b07514b90eb4e6668481b04dd11648a91cf9", "1.38.0--r44hdfd78af_0": "sha256:e3de5670360fd36ecb45c6c3692a6b6cf439636b76856738faf64181487a01e1"}, "docker": "quay.io/biocontainers/bioconductor-ropls", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ropls.
shpc-registry automated BioContainers addition for bioconductor-ropls
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ropls
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ropls:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ropls/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ropls/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ropls-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ropls-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ropls-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ropls-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ropls-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ropls-inspect-deffile:

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