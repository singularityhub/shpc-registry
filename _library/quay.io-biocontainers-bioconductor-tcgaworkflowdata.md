---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgaworkflowdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgaworkflowdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgaworkflowdata/container.yaml"
updated_at: "2025-09-07 03:31:53.399483"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgaworkflowdata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_1"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcgaworkflowdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgaworkflowdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgaworkflowdata", "latest": {"1.30.0--r44hdfd78af_0": "sha256:f6e39c2a31f015c84d08a0d62058f4a0859698886d5f6d50700fe0a900ea3806"}, "tags": {"1.8.0--r36_1": "sha256:c5bb6aaf6c06378f008b5fd3c0f2cfbf845076a185aeb5f33a8932cb4949be81", "1.22.0--r42hdfd78af_0": "sha256:72e31e2f53bcb4209610761e5a268884a19cef02fb35b46a64364d3aedd01943", "1.18.0--r41hdfd78af_1": "sha256:e82c756963751e8f1c2edd58487cead1d2f1cc772e3e61d6fa45fcb7d464853d", "1.16.0--r41hdfd78af_0": "sha256:081ca21d2e4d80a4fbe8da395e4ab1fc0f9fb93e00fe897964fa2ae4698cf7ff", "1.14.0--r40hdfd78af_1": "sha256:ee3fabc5a318a417a3718c165ced577af5d90d85be28a901bfd52ec6604be070", "1.12.0--r40_0": "sha256:4f9ee05ee8caeb84e6523d9900d03b15e07c5647025b3f76d345265fd97357a2", "1.24.0--r43hdfd78af_0": "sha256:5260612a840148ac2c8790de9225dddbe84d81d5752be6d5b47dad6a3db3f586", "1.26.0--r43hdfd78af_0": "sha256:1d277a17b30c352c4853696958ccb6a5c724b09722be7be2d4c1cc9f35af9db9", "1.30.0--r44hdfd78af_0": "sha256:f6e39c2a31f015c84d08a0d62058f4a0859698886d5f6d50700fe0a900ea3806"}, "docker": "quay.io/biocontainers/bioconductor-tcgaworkflowdata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgaworkflowdata.
shpc-registry automated BioContainers addition for bioconductor-tcgaworkflowdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgaworkflowdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgaworkflowdata:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgaworkflowdata/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcgaworkflowdata/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgaworkflowdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgaworkflowdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgaworkflowdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgaworkflowdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgaworkflowdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgaworkflowdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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