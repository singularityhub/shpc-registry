---
layout: container
name:  "quay.io/biocontainers/bioconductor-path2ppi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-path2ppi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-path2ppi/container.yaml"
updated_at: "2025-01-22 03:31:18.240151"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-path2ppi"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-path2ppi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-path2ppi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-path2ppi", "latest": {"1.36.0--r44hdfd78af_0": "sha256:0c1f2ca17f2af2a56eb871cfaeeb8dd4cc576e135589717c04f3af684ed85e09"}, "tags": {"1.8.0--r3.4.1_0": "sha256:0030e35f385c6f64e405752fc988403c792a9d7cf70bd6574cfdd73fceacd6ad", "1.24.0--r41hdfd78af_0": "sha256:cbec8e0826b44cd525a3735948317ff6ff4eff622aba2fd30883d938b7fd8ba0", "1.22.0--r41hdfd78af_0": "sha256:841b3fbb226e27238a8eb06bb08f7a9d29b0097f1813ff214a128b0fdb6d14cb", "1.20.0--r40hdfd78af_1": "sha256:22ec7787c89d7278f6504e28f56875267b0ef2fcd9f951033786e2a530b00d2e", "1.18.0--r40_0": "sha256:9811f7b0bbb1ca1b55a7717a54e1e1a2da4b1de885a7b0688ae83fabd621006d", "1.16.0--r36_0": "sha256:85cfe5b04a12264522ad6007ad33a098d967acc5dfbe38afa88fd771f08c8e46", "1.28.0--r42hdfd78af_0": "sha256:02cfc6432491f8aafb33dbd73d91ba04a7bccd6a67325bf0d37975de993d9718", "1.30.0--r43hdfd78af_0": "sha256:4eabc0e2c540b9da701e2966f40cfe3f7e35bb48f8bf4eb542d53037f4b05ce8", "1.32.0--r43hdfd78af_0": "sha256:26fb4ee2ba680ca1ff027300384e1ead1eee78aa62fbfb60b752a6f4b2f3e1d8", "1.36.0--r44hdfd78af_0": "sha256:0c1f2ca17f2af2a56eb871cfaeeb8dd4cc576e135589717c04f3af684ed85e09"}, "docker": "quay.io/biocontainers/bioconductor-path2ppi", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-path2ppi.
shpc-registry automated BioContainers addition for bioconductor-path2ppi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-path2ppi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-path2ppi:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-path2ppi/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-path2ppi/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-path2ppi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-path2ppi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-path2ppi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-path2ppi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-path2ppi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-path2ppi-inspect-deffile:

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