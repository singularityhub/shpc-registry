---
layout: container
name:  "quay.io/biocontainers/snakemake"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake/container.yaml"
updated_at: "2024-05-27 03:02:40.272518"
latest: "8.11.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake"

versions:
 - "5.4.0--0"
 - "8.9.0--hdfd78af_0"
 - "8.8.0--hdfd78af_0"
 - "8.7.0--hdfd78af_0"
 - "8.6.0--hdfd78af_0"
 - "8.5.5--hdfd78af_0"
 - "8.10.8--hdfd78af_0"
 - "8.11.3--hdfd78af_0"
 - "8.10.8--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for snakemake"
config: {"url": "https://biocontainers.pro/tools/snakemake", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snakemake", "latest": {"8.11.3--hdfd78af_0": "sha256:5ab936e53c7c229521da3e5f70b855ec3dc203c9f23057c184688f46793c1c95"}, "tags": {"5.4.0--0": "sha256:babe98d0fe1badf8bca64df76b48af8d9d5595d96a23d8ec2ff6560e30f98181", "8.9.0--hdfd78af_0": "sha256:b64ef7f0647049d227f350406879e450d9a8a5f1e120e588bdfced0d094891f1", "8.8.0--hdfd78af_0": "sha256:fe71bfb1525ba30c79ddb6529b4b84734b374f4e8deaee62cb11effbaf2ad585", "8.7.0--hdfd78af_0": "sha256:af5ebbce2da9d5f5ad9a68ba7d5e050c219c8d9562710a46384ab0e1e2715db1", "8.6.0--hdfd78af_0": "sha256:10ea50c0ec1508e998b2e1a987c043dbeaa71ad5e808629ba7d5fd34d72bb969", "8.5.5--hdfd78af_0": "sha256:1b51b49baa71fcc34c9071f61c5b7fff397ce0f63a7a5035a87fc4320efc3a97", "8.10.8--hdfd78af_0": "sha256:43a958a4b12da111fcef111887379e3031e068e1a9670e84dd92b2c15f2465c9", "8.11.3--hdfd78af_0": "sha256:5ab936e53c7c229521da3e5f70b855ec3dc203c9f23057c184688f46793c1c95", "8.10.8--hdfd78af_1": "sha256:559cd7433f004bdd6f2f3e1464a8c423a7773e9a97ce5112a922e91db85cca52"}, "docker": "quay.io/biocontainers/snakemake"}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake.
shpc-registry automated BioContainers addition for snakemake
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake:8.11.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake/8.11.3--hdfd78af_0
$ module help quay.io/biocontainers/snakemake/8.11.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### snakemake

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