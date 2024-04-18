---
layout: container
name:  "quay.io/biocontainers/bioconductor-aroma.light"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aroma.light/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aroma.light/container.yaml"
updated_at: "2024-04-18 02:28:47.550573"
latest: "3.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aroma.light"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "3.8.0--r3.4.1_0"
 - "3.28.0--r42hdfd78af_0"
 - "3.24.0--r41hdfd78af_0"
 - "3.22.0--r41hdfd78af_0"
 - "3.20.0--r40hdfd78af_1"
 - "3.18.0--r40_0"
 - "3.30.0--r43hdfd78af_0"
 - "3.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aroma.light"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aroma.light", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aroma.light", "latest": {"3.32.0--r43hdfd78af_0": "sha256:226e987d405291edcaae4938c12cf52d8918e8824fa8ebcb5ba9ae618b76a1da"}, "tags": {"3.8.0--r3.4.1_0": "sha256:2ea5c76876af860ae73054105b4d754e6a8ce0a04292793f18ba71830b5b4924", "3.28.0--r42hdfd78af_0": "sha256:58cbd4f74438bae7b5986b7527f9e5eaaee9884bac763511a654bb377850f021", "3.24.0--r41hdfd78af_0": "sha256:6f51803d71c4acfb361df60a9b25694e9873bb12d5c7702f52c9eec36824129e", "3.22.0--r41hdfd78af_0": "sha256:bb4e204dc327955a454461f1ee4b0a0da8e0b1d536421c349671e3068b451e0e", "3.20.0--r40hdfd78af_1": "sha256:703e7aa2379bd3b897c20c0211c1727f0afc3224f8aa7a0d7985cfa7ecd78e89", "3.18.0--r40_0": "sha256:996e082e03b45b22f710a56b26783fede2c487791328a7c18bbccd19ff89e21e", "3.30.0--r43hdfd78af_0": "sha256:540f16096f3b7856f95043ee0118e4db4bf249a2434c08095dc8ced96a373fd7", "3.32.0--r43hdfd78af_0": "sha256:226e987d405291edcaae4938c12cf52d8918e8824fa8ebcb5ba9ae618b76a1da"}, "docker": "quay.io/biocontainers/bioconductor-aroma.light", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aroma.light.
shpc-registry automated BioContainers addition for bioconductor-aroma.light
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aroma.light
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aroma.light:3.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aroma.light/3.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-aroma.light/3.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aroma.light-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aroma.light-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aroma.light-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aroma.light-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aroma.light-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aroma.light-inspect-deffile:

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