---
layout: container
name:  "quay.io/biocontainers/clincnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clincnv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clincnv/container.yaml"
updated_at: "2025-11-07 03:16:52.549162"
latest: "1.19.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/clincnv"
aliases:
 - "clinCNV.R"
 - "mergeFilesFromFolder.R"
 - "mergeFilesFromFolderDT.R"
 - "x86_64-conda-linux-gnu.cfg"
 - "hb-info"
 - "tjbench"
versions:
 - "1.18.3--hdfd78af_0"
 - "1.19.1--hdfd78af_0"
description: "singularity registry hpc automated addition for clincnv"
config: {"url": "https://biocontainers.pro/tools/clincnv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for clincnv", "latest": {"1.19.1--hdfd78af_0": "sha256:030a19bb4e7df7be962054d0f8afbd7576f1e7ae999e321942ddb616acd49739"}, "tags": {"1.18.3--hdfd78af_0": "sha256:d8fe04cb106c27f7c3b14fefa3db31c9cb7982ea1f26606757cfae1d808ca3ba", "1.19.1--hdfd78af_0": "sha256:030a19bb4e7df7be962054d0f8afbd7576f1e7ae999e321942ddb616acd49739"}, "docker": "quay.io/biocontainers/clincnv", "aliases": {"clinCNV.R": "/usr/local/bin/clinCNV.R", "mergeFilesFromFolder.R": "/usr/local/bin/mergeFilesFromFolder.R", "mergeFilesFromFolderDT.R": "/usr/local/bin/mergeFilesFromFolderDT.R", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clincnv.
singularity registry hpc automated addition for clincnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clincnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clincnv:1.19.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clincnv/1.19.1--hdfd78af_0
$ module help quay.io/biocontainers/clincnv/1.19.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clincnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clincnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clincnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clincnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clincnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clincnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clinCNV.R

```bash
$ singularity exec <container> /usr/local/bin/clinCNV.R
$ podman run --it --rm --entrypoint /usr/local/bin/clinCNV.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinCNV.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeFilesFromFolder.R

```bash
$ singularity exec <container> /usr/local/bin/mergeFilesFromFolder.R
$ podman run --it --rm --entrypoint /usr/local/bin/mergeFilesFromFolder.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeFilesFromFolder.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeFilesFromFolderDT.R

```bash
$ singularity exec <container> /usr/local/bin/mergeFilesFromFolderDT.R
$ podman run --it --rm --entrypoint /usr/local/bin/mergeFilesFromFolderDT.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeFilesFromFolderDT.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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