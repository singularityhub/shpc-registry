---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhesuscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhesuscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhesuscdf/container.yaml"
updated_at: "2024-12-10 03:06:41.375556"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rhesuscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rhesuscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhesuscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhesuscdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:a0ed2aec13960bbf8af82d0a3f2df7bfcf27e5b393c507ff864367e75ff8b927"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:ff03234e9ed27392458e337f2fc50794e8ac1949d52754d591a2f4f531eed38d", "2.18.0--r42hdfd78af_10": "sha256:c1c41059f31e5865d9bb6b7e2d14f82e80f1903f38f5e4139e8bc7fa47a74581", "2.18.0--r43hdfd78af_11": "sha256:3a636ab7fcde1460b94988fed881b6e140b107370356b660f10cda34d24d61b4", "2.18.0--r43hdfd78af_12": "sha256:a0ed2aec13960bbf8af82d0a3f2df7bfcf27e5b393c507ff864367e75ff8b927"}, "docker": "quay.io/biocontainers/bioconductor-rhesuscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhesuscdf.
shpc-registry automated BioContainers addition for bioconductor-rhesuscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhesuscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhesuscdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhesuscdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rhesuscdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhesuscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhesuscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhesuscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhesuscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhesuscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhesuscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rhesuscdf

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