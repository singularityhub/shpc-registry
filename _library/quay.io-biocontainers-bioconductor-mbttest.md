---
layout: container
name:  "quay.io/biocontainers/bioconductor-mbttest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mbttest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mbttest/container.yaml"
updated_at: "2025-05-20 03:19:38.748771"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mbttest"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.1--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mbttest"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mbttest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mbttest", "latest": {"1.34.0--r44hdfd78af_0": "sha256:e96a557b978ffdbe296a181f3bbf83177e73ee72577899ac5cd6052ff0ec5119"}, "tags": {"1.8.1--r341_0": "sha256:4b53074fd66ec647cb8159caf201ed978f6d21918e6c7b54b909383a86623a59", "1.26.0--r42hdfd78af_0": "sha256:bd1618b9b95215f687974ce3142e4eb308fe2516982f4920208d27026f10d18a", "1.22.0--r41hdfd78af_0": "sha256:778dd5c6ec26e735bcb07e19e3782527785a5b66a8249feed72564b695edb37e", "1.20.0--r41hdfd78af_0": "sha256:c4654fde0e783a55061ec52c3bc7da5719afb2814ab296c8fba433440ac94e12", "1.18.0--r40hdfd78af_1": "sha256:2ed3528024cee28ce84b664648911234f7129bf5735957b614089d50f45e6b8d", "1.16.0--r40_0": "sha256:3676ba61703515dc0dc4759ee810eaecd799cd523e5a29e541fcf8a5b98e092f", "1.28.0--r43hdfd78af_0": "sha256:42a5312fc553b749ff431586f00dd95f9169981d480554882a3c87f6d5d19848", "1.30.0--r43hdfd78af_0": "sha256:d0203626a2001c7d7a73eefbbbf9376f677a197b80c1eece630db5bdf06354fa", "1.34.0--r44hdfd78af_0": "sha256:e96a557b978ffdbe296a181f3bbf83177e73ee72577899ac5cd6052ff0ec5119"}, "docker": "quay.io/biocontainers/bioconductor-mbttest", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mbttest.
shpc-registry automated BioContainers addition for bioconductor-mbttest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mbttest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mbttest:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mbttest/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mbttest/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mbttest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbttest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbttest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mbttest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mbttest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mbttest-inspect-deffile:

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