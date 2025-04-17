---
layout: container
name:  "quay.io/biocontainers/bioconductor-fobitools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fobitools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fobitools/container.yaml"
updated_at: "2025-04-17 04:45:07.279190"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fobitools"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fobitools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fobitools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fobitools", "latest": {"1.14.0--r44hdfd78af_0": "sha256:d8f6d0e9a9b343afde25b1579cd6566a1051063f460a75adeba343f9202de20f"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:780f29e27ec8fff00a25bd22b045fa8bd73bed4386b5f02bf36992d4cf5b1946", "1.6.0--r42hdfd78af_0": "sha256:d231c8f92f9a64cc9a16ce43be63df4aca08006aa8ad23620cf3be149b13bcd3", "1.8.0--r43hdfd78af_0": "sha256:959ec33b78e4d0dcb20d33890f60cacc92ba51dbf80006fb105e944b6b136778", "1.10.0--r43hdfd78af_0": "sha256:ab3a024bb3cf73768bd80edd1ab22c6ffb6e118d60f4a7470560838f03b7e29d", "1.14.0--r44hdfd78af_0": "sha256:d8f6d0e9a9b343afde25b1579cd6566a1051063f460a75adeba343f9202de20f"}, "docker": "quay.io/biocontainers/bioconductor-fobitools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fobitools.
shpc-registry automated BioContainers addition for bioconductor-fobitools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fobitools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fobitools:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fobitools/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fobitools/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fobitools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fobitools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fobitools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fobitools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fobitools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fobitools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fobitools

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