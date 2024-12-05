---
layout: container
name:  "quay.io/biocontainers/bioconductor-dada2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dada2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dada2/container.yaml"
updated_at: "2024-12-05 03:46:05.611262"
latest: "1.30.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dada2"
aliases:
 - "wget"
versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h5f743cb_0"
 - "1.16.0--r40h5f743cb_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
 - "1.28"
 - "1.20"
description: "shpc-registry automated BioContainers addition for bioconductor-dada2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dada2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dada2", "latest": {"1.30.0--r43hf17093f_0": "sha256:4f7d44074376a21a44963226fe192133c8d7f0831863a2e3bdfe704e280235da"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:7d48ee7fc9ffbcc6d0fd8820db0aa34d01419058a8b203cdd6f874a3458a9e77", "1.26.0--r42hc247a5b_0": "sha256:455e98b4cf5a8681aa8b4e9f06183ac00fadecd17b0690ec97960fcb0cc1ab7f", "1.22.0--r41hc247a5b_2": "sha256:8dc3d468bd9d4a0d13156fbeb9cc8c5125e86755ffce479bdbc91cd5d6bb217d", "1.20.0--r41h399db7b_0": "sha256:80f5b71cc5e3917186831a6871c9a6ec7e2ca88567d79891edef8a306e6d315f", "1.18.0--r40h5f743cb_0": "sha256:d716e2ae6db6cc09b1c4ff9a2211e8256e9cd9cd183941c3769c5c220ac298fa", "1.16.0--r40h5f743cb_0": "sha256:4865fade8ddd1f0168a7ebcfca97a8f08542e6fc9e01d006b45b6cba772618ac", "1.26.0--r42hf17093f_1": "sha256:92498704ba421f1224e6ec98f293f0e7b836ae882263ef9c11b4772e01335c5f", "1.28.0--r43hf17093f_0": "sha256:b215ed2c3485cd2a0d10b5763661905bb78c6e4f2a091a64de5fbe56b4538d4d", "1.30.0--r43hf17093f_0": "sha256:4f7d44074376a21a44963226fe192133c8d7f0831863a2e3bdfe704e280235da", "1.28": "sha256:ef7d0f281d10e6710625d559ab4cdda04ea2eb049a6882190fa2d0d4bc52dd5f", "1.20": "sha256:29f72f1c3883fe6547cc6fe05588d51f0666989cae41c6d7fc6fb6cefe51a230"}, "docker": "quay.io/biocontainers/bioconductor-dada2", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dada2.
shpc-registry automated BioContainers addition for bioconductor-dada2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dada2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dada2:1.30.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dada2/1.30.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-dada2/1.30.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dada2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dada2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dada2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dada2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dada2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dada2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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