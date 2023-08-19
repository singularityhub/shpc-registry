---
layout: container
name:  "quay.io/biocontainers/genomepy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomepy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genomepy/container.yaml"
updated_at: "2023-08-19 02:24:15.470976"
latest: "0.16.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/genomepy"

versions:
 - "0.9.3--py_0"
 - "0.14.0--pyh7cba7a3_1"
 - "0.13.1--pyhdfd78af_0"
 - "0.12.0--pyhdfd78af_0"
 - "0.11.1--pyhdfd78af_0"
 - "0.10.0--pyhdfd78af_0"
 - "0.14.0--pyh7cba7a3_2"
 - "0.15.0--pyh7cba7a3_0"
 - "0.16.0--pyh7cba7a3_0"
 - "0.16.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for genomepy"
config: {"url": "https://biocontainers.pro/tools/genomepy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genomepy", "latest": {"0.16.1--pyh7cba7a3_0": "sha256:1753d2ae0cf3d77cab331fdcbf6d89f7c1d305bf5151ac2b45ac0032bb5b0f17"}, "tags": {"0.9.3--py_0": "sha256:07de9012b90c84b3905b3ec85773936f7c9cc68712672acd2bd61ca621de8dae", "0.14.0--pyh7cba7a3_1": "sha256:a5a9a61ae0c5e266deea1aee53bb85376df459c49391c940e4e53a0780a0be93", "0.13.1--pyhdfd78af_0": "sha256:ab261f633b9c009290e97944ece38071b83a8dd2fd79926e4840e9526b85e8b3", "0.12.0--pyhdfd78af_0": "sha256:0b33cfd6ba31f913f7a6343ad48c186b016cdb7cc18d62cca9c609b3ae0fd4a7", "0.11.1--pyhdfd78af_0": "sha256:decf50a6370afeb35db4f1baa9b36cab019fc22eb53d945291e1d06294739ba7", "0.10.0--pyhdfd78af_0": "sha256:0c0b430b060487a753521d930d95f398827e50610081f97cf55cc80ed99650da", "0.14.0--pyh7cba7a3_2": "sha256:e49efd140a481ff8a9627b8ec3c18823c42e5dc5962ce286e56424b6921bd743", "0.15.0--pyh7cba7a3_0": "sha256:0c2a2a388c432454a442274aab7837090bef5868d42939a51eac85b05055253d", "0.16.0--pyh7cba7a3_0": "sha256:12a4a3c72bce68af8dd0e7a9d64444207bc430f7a8149d8b967d29adaa2fc4d9", "0.16.1--pyh7cba7a3_0": "sha256:1753d2ae0cf3d77cab331fdcbf6d89f7c1d305bf5151ac2b45ac0032bb5b0f17"}, "docker": "quay.io/biocontainers/genomepy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomepy.
shpc-registry automated BioContainers addition for genomepy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomepy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomepy:0.16.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomepy/0.16.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/genomepy/0.16.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomepy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomepy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomepy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomepy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomepy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomepy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### genomepy

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